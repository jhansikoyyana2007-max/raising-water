from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and feature names
model = joblib.load("models/flood_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")


@app.route("/")
def home():
    return render_template("index.html", features=feature_names)


@app.route("/predict", methods=["POST"])
def predict():

    try:
        values = []

        for feature in feature_names:
            values.append(float(request.form[feature]))

        values = np.array(values).reshape(1, -1)

        prediction = model.predict(values)[0]

        # Confidence score
        confidence = model.predict_proba(values)[0]

        flood_probability = confidence[1] * 100

        if prediction == 1:
            risk = "High Flood Risk"
            color = "danger"
        else:
            risk = "Low Flood Risk"
            color = "success"

        return render_template(
            "result.html",
            prediction=risk,
            probability=round(flood_probability, 2),
            color=color
        )

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
   