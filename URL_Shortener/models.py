import string
from datetime import datetime
from random import choices
from .extensions import db

class Link_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(512))
    shortened_url = db.Column(db.String(6), unique=True)
    total_visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortened_url = self.short_link_generator()

    def short_link_generator(self):
        characters = string.digits + string.ascii_letters
        shortened_url = ''.join(choices(characters, k=6))

        link = self.query.filter_by(shortened_url=shortened_url).first()

        if link:
            return self.short_link_generator()
        
        return shortened_url



