from flask import Blueprint, render_template
from app.controllers.index import home, about, login

site_routes = Blueprint('site_routes', __name__)

site_routes.add_url_rule(rule='/',view_func=home, methods = ['GET'])
site_routes.add_url_rule(rule='/about',view_func=about, methods = ['GET'])
site_routes.add_url_rule(rule='/login',view_func=login, methods = ['GET'])