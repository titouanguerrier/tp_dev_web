from flask import Flask

# Create database connection object
from flask_sqlalchemy import SQLAlchemy
app = Flask ( __name__ )
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

db = SQLAlchemy(app)
db.init_app(app)