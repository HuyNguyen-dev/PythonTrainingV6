from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@127.0.0.1:3306/mydb" % quote_plus("12345678x@X")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy()
db.init_app(app)

from app.controllers import index
from app.models import models