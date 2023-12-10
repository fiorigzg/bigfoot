import json
from flask import Flask, render_template, request, jsonify
from analyze import get_statistic
from flask_cors import CORS


app = Flask(__name__, static_folder="assets", template_folder="dist")
CORS(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/research")
def research():
    return render_template('research.html')

@app.route("/statistic", methods=['POST'])
def statistic():
    data = request.get_json()
    data = get_statistic(data)
    return jsonify(data)
