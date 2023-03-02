from flask import Blueprint
from app.controllers.user_controller import getalldata,insertdata,updatedata

api_routes = Blueprint('api_routes', __name__,url_prefix='/api/user')
api_routes.add_url_rule(rule='/getalldata',view_func=getalldata, methods = ['GET'])
api_routes.add_url_rule(rule='/insertdata',view_func=insertdata, methods = ['POST'])
api_routes.add_url_rule(rule='/insertdata/nativequery',view_func=insertdata, methods = ['POST'])
api_routes.add_url_rule(rule='/updatedata/<int:user_id>',view_func=updatedata, methods = ['PUT'])
api_routes.add_url_rule(rule='/updatedata/nativequery/<int:user_id>',view_func=updatedata, methods = ['PUT'])