# server/app.py
#!/usr/bin/env python3

# Import utilities and dependencies
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db, Earthquake

# Create Flask app and configure the database location
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///earthquakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Connect the db and migration tool to the Flask app 
migrate = Migrate(app, db)
db.init_app(app)

# Define the homepage index route
@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Define the /earthquakes/<id> route
@app.route('/earthquakes/<int:id>')
def get_earthquakes_by_id():
    # Search the database for the earthquake with the matching id 
    earthquake = db.session.get(Earthquake, id)

    # Perform error handling if no earthquake is found, return data in JSON form with 200 status
    if not earthquake:
        return jsonify({"message": f"Earthquake {id} not found."}), 404
    return jsonify({
        "id": earthquake.id,
        "magnitude": earthquake.magnitude,
        "location": earthquake.location,
        "year": earthquake.year
    }), 200

# Define the /earthquakes/magnitude/<magnitude> route
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    # Filter out earthquakes with magnitudes >= to a specific value 
    earthquakes = Earthquake.query.filter(
        Earthquake.magnitude >= magnitude
    ).all()

    # Create a list of dicts to store data
    earthquake_list = [
        {
            "id": eq.id,
            "magnitude": eq.magnitude,
            "location": eq.location,
            "year": eq.year 
        }
        for eq in earthquakes
    ]

    # Provide data in JSON format
    return jsonify({
        "count": len(earthquake_list),
        "quakes": earthquake_list
    }), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
