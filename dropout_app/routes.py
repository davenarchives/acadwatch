from flask import Blueprint, current_app, jsonify, render_template, request

from .fields import default_form_values, grouped_fields


dashboard_bp = Blueprint("dashboard", __name__)


def template_context(result, error, form_values):
    """Build shared context for full page renders."""
    return {
        "error": error,
        "form_values": form_values,
        "result": result,
        "sections": grouped_fields(),
    }


@dashboard_bp.route("/", methods=["GET"])
def index():
    form_values = default_form_values()
    service = current_app.prediction_service
    result, error, form_values = service.predict(form_values)

    return render_template(
        "index.html",
        **template_context(result, error or service.error, form_values),
    )


@dashboard_bp.route("/predict", methods=["POST"])
def predict():
    service = current_app.prediction_service
    result, error, form_values = service.predict(request.form)

    return render_template(
        "index.html",
        **template_context(result, error, form_values),
    )


@dashboard_bp.route("/api/predict", methods=["POST"])
def predict_api():
    payload = request.get_json(silent=True) or {}
    result, error, _ = current_app.prediction_service.predict(payload)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(result)
