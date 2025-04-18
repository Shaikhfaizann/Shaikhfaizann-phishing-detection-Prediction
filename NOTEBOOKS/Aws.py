from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load(r"C:\Users\Dell\Downloads\DEPLOYMENT\NOTEBOOKS\model.pkl")

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        # Convert incoming values to a NumPy array
        input_values = np.array([list(data.values())])
        prediction = model.predict(input_values)[0]
        return jsonify({"prediction": str(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
