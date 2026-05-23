# Import utilities and dependencies
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model):
    # Create table name for the database
    __tablename__ = "earthquakes"

    # Create primary key column with a unique ID for each record 
    id = db.Column(db.Integer, primary_key=True)

    # Store the magnitude of the earthquakes as a float 
    magnitude = db.Column(db.Float)

    # Store the location of where the incident occured as a string 
    location = db.Column(db.String)

    # Store the year of the earthquake as a integer
    year = db.Column(db.Integer)

    # Return earthquake data
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
