# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from urllib.parse import quote_plus
# from flask_cors import CORS


# app = Flask(__name__)
# app.config.from_object('config')
# CORS(app)

# db = SQLAlchemy()
# db.init_app(app)

# from app.models import models
# from app.routes import api_routes
# from app.routes import site_routes

# app.register_blueprint(api_routes.api_routes)
# app.register_blueprint(site_routes.site_routes)