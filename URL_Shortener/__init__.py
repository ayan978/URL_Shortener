from flask import Flask
from .extensions import db
from .routes import short


app = Flask(__name__)
config_file = 'settings.py'
app.config.from_pyfile(config_file)
db.init_app(app)
app.register_blueprint(short)

