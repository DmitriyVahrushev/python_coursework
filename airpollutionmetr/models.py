from datetime import datetime
from airpollutionmetr import db

class Pollution(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pollution_rate = db.Column(db.Float, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    region = db.Column(db.String(20), nullable = False,  default = 'Russia')

    def __repr__(self):
        return f"Measurment('{self.pollution_rate}', '{self.city}', '{self.region}')"