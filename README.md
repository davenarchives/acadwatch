# Student Dropout Prediction Flask App

This project is a small Flask runtime app for student dropout prediction. It
does not train a model at runtime. The app loads the prebuilt
`dropout_model.pkl` file directly.

## Project Structure

```text
dropoutprediction/
|-- app.py
|-- dropout_model.pkl
|-- requirements.txt
|-- README.md
|-- dropout_app/
|   |-- __init__.py
|   |-- config.py
|   |-- fields.py
|   |-- model_service.py
|   `-- routes.py
|-- static/
|   |-- css/
|   |   `-- dashboard.css
|   `-- js/
|       `-- dashboard.js
`-- templates/
    |-- index.html
    `-- components/
        |-- error_banner.html
        |-- field_card.html
        |-- header.html
        |-- insight_panel.html
        `-- section_card.html
```

## Architecture

- `app.py` is only the Flask entry point.
- `dropout_app/__init__.py` creates the Flask app and registers routes.
- `dropout_app/fields.py` owns form sections, labels, options, defaults, and UI metadata.
- `dropout_app/model_service.py` loads `dropout_model.pkl`, validates input, scales data, predicts, and builds insight output.
- `dropout_app/routes.py` contains page and API routes.
- `templates/components/` contains reusable Jinja UI components.
- `static/css/dashboard.css` and `static/js/dashboard.js` contain dashboard styling and live interactions.

## Model Contract

`dropout_model.pkl` must be a pickle file containing this dictionary:

```python
{
    "scaler": fitted_scaler,
    "model": fitted_model,
    # optional metadata such as "model_name" is allowed
}
```

The `/predict` route converts form values into a NumPy array, runs
`scaler.transform(...)`, then calls `model.predict(...)`. The 29 submitted
feature names and order are driven by `dropout_app/fields.py` and must match
the CSV feature columns before `Target`.

The dashboard also uses `/api/predict` for real-time risk updates as educators
adjust the form controls.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open the app at:

```text
http://127.0.0.1:5000
```
