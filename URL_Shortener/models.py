from datetime import datetime
from .extensions import db

class Link_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(512))
    shortened_url = db.Column(db.String(6), unique=True)
    total_visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    
