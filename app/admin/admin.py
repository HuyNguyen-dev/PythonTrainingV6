from app import app,db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models.models import User

admin = Admin(app=app, name="Admin page", template_mode='bootstrap4')

class UserView(ModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['username','full_name']
    column_filters = ['email','phone_number']

admin.add_view(UserView(User,db.session))