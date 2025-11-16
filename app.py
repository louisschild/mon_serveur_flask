from flask import Flask, jsonify  # importe Flask et jsonify
import os
from main import get_presentations  # importe la fonction depuis main.py

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello depuis Flask sur Render !"

@app.route("/main")
def main_page():
    presentations = get_presentations()
    return jsonify(presentations)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

