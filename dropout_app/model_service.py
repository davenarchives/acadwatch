import pickle
import warnings

import numpy as np

from .fields import FEATURE_FIELDS


class PredictionService:
    """Loads the model bundle and returns dashboard-ready predictions."""

    def __init__(self, model_path):
        self.model_path = model_path
        self.bundle = None
        self.error = None
        self._load_bundle()

    def _load_bundle(self):
        try:
            self.bundle = self._read_bundle()
        except (OSError, pickle.PickleError, ValueError) as exc:
            self.error = str(exc)

    def _read_bundle(self):
        with self.model_path.open("rb") as model_file:
            bundle = pickle.load(model_file)

        if not isinstance(bundle, dict):
            raise ValueError("dropout_model.pkl must contain a dictionary.")

        required_keys = {"scaler", "model"}
        missing_keys = required_keys - set(bundle)
        if missing_keys:
            missing = ", ".join(sorted(missing_keys))
            raise ValueError(f"dropout_model.pkl is missing required keys: {missing}.")

        expected_features = [field["name"] for field in FEATURE_FIELDS]
        scaler_features = list(getattr(bundle["scaler"], "feature_names_in_", []))
        if scaler_features and scaler_features != expected_features:
            raise ValueError(
                "Predictor feature order does not match the fitted scaler."
            )

        return bundle

    def predict(self, form_data):
        """Validate input, run scaler/model, and return a UI-ready result."""
        if self.bundle is None:
            return None, (
                "Model is not available. Place dropout_model.pkl in the "
                "project root and restart the app."
            ), dict(form_data)

        values, form_values, error = parse_form_values(form_data)
        if error:
            return None, error, form_values

        input_data = np.array(values, dtype=float).reshape(1, -1)
        scaler = self.bundle["scaler"]
        model = self.bundle["model"]

        try:
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    "ignore",
                    message="X does not have valid feature names.*",
                    category=UserWarning,
                )
                scaled_data = scaler.transform(input_data)
            prediction = model.predict(scaled_data)
        except ValueError as exc:
            return None, f"Prediction failed: {exc}", form_values

        score = round(dropout_probability(model, scaled_data, prediction), 1)
        level = risk_level(score)
        factors = contributing_factors(form_values)

        return {
            "label": result_text(prediction),
            "risk_level": level,
            "confidence": score,
            "factors": factors,
            "actions": suggested_actions(level, factors),
        }, None, form_values


def parse_form_values(form_data):
    """Return model-ready numeric values or a human-readable validation error."""
    values = []
    form_values = {}

    for field in FEATURE_FIELDS:
        raw_value = str(form_data.get(field["name"], "")).strip()
        form_values[field["name"]] = raw_value

        if raw_value == "":
            return None, form_values, f"{field['label']} is required."

        try:
            numeric_value = float(raw_value)
        except ValueError:
            return None, form_values, f"{field['label']} must be a number."

        minimum = field.get("min")
        maximum = field.get("max")
        if minimum is not None and numeric_value < minimum:
            return None, form_values, f"{field['label']} must be at least {minimum}."
        if maximum is not None and numeric_value > maximum:
            return None, form_values, f"{field['label']} must be no more than {maximum}."

        values.append(numeric_value)

    return values, form_values, None


def result_text(raw_prediction):
    """Normalize common model outputs into the two UI labels."""
    prediction = np.asarray(raw_prediction).ravel()[0]

    if isinstance(prediction, str):
        normalized = prediction.strip().lower()
        if "dropout" in normalized and "non" not in normalized:
            return "Likely to Dropout"
        return "Likely to Stay"

    return "Likely to Dropout" if int(prediction) == 1 else "Likely to Stay"


def dropout_probability(model, scaled_data, prediction):
    """Return dropout probability as a percentage when the model exposes it."""
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(scaled_data)[0]
        classes = list(getattr(model, "classes_", []))

        if 1 in classes:
            return float(probabilities[classes.index(1)] * 100)

        for index, class_name in enumerate(classes):
            if str(class_name).strip().lower() == "dropout":
                return float(probabilities[index] * 100)

    return 82.0 if result_text(prediction) == "Likely to Dropout" else 18.0


def risk_level(score):
    """Convert dropout probability into a supportive risk level."""
    if score >= 67:
        return "High"
    if score >= 34:
        return "Medium"
    return "Low"


def contributing_factors(form_values):
    """Surface simple, explainable factors for educators."""
    factors = []

    first_grade = float(form_values.get("Curricular units 1st sem (grade)", 0))
    second_grade = float(form_values.get("Curricular units 2nd sem (grade)", 0))
    first_approved = float(form_values.get("Curricular units 1st sem (approved)", 0))
    second_approved = float(form_values.get("Curricular units 2nd sem (approved)", 0))
    debtor = form_values.get("Debtor") == "1"
    tuition_current = form_values.get("Tuition fees up to date") == "1"
    scholarship = form_values.get("Scholarship holder") == "1"

    if min(first_grade, second_grade) < 10:
        factors.append("Low semester grade average")
    if first_approved <= 2 or second_approved <= 2:
        factors.append("Few approved curricular units")
    if debtor or not tuition_current:
        factors.append("Tuition or debt pressure")
    if not scholarship:
        factors.append("No scholarship support recorded")

    if not factors:
        factors.append("Stable academic and financial profile")

    return factors[:4]


def suggested_actions(level, factors):
    """Return concise actions that match the current risk level."""
    if level == "High":
        return [
            "Recommend academic counseling",
            "Review tuition or debt support options",
            "Schedule a follow-up with the program advisor",
        ]

    if level == "Medium":
        return [
            "Monitor upcoming evaluations",
            "Offer tutoring or study planning",
            "Check for administrative blockers",
        ]

    if "Stable academic and financial profile" in factors:
        return [
            "Continue routine advising",
            "Encourage current academic habits",
        ]

    return [
        "Keep progress under light review",
        "Share support resources proactively",
    ]
