from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5f64d35c74cd3842cb8712752bc683b'
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes