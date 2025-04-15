from flask import Flask, jsonify, request, render_template, url_for  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from flask_cors import CORS  # type: ignore

app = Flask(__name__, template_folder='template', static_folder='static')

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hbcu_tool.db'
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Student or Staff

def init_db():
    with app.app_context():
        db.create_all()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API Endpoints
@app.route('/housing', methods=['GET'])
def get_housing():
    return jsonify({"available_units": 10, "waitlist": 5})

@app.route('/financial_aid', methods=['GET'])
def get_financial_aid():
    return jsonify({"status": "Processing", "next_steps": "Submit additional documents"})

@app.route('/test', methods=['GET'])
def test_api():
    return jsonify({"message": "API is working correctly!"})

# Run server
if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5002)
