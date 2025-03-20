from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to access backend

@app.route("/")
def home():
    return jsonify({"message": "ROI Calculator API is running!"})

@app.route("/calculate", methods=["POST"])
def calculate_roi():
    data = request.json
    # Example: Extract values from request
    investment = data.get("investment", 0)
    revenue = data.get("revenue", 0)

    if investment == 0:
        return jsonify({"error": "Investment cannot be zero"}), 400

    roi = ((revenue - investment) / investment) * 100
    return jsonify({"roi": roi})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
