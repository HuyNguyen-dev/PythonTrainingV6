from urllib.parse import quote_plus

#Connect DB
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:%s@127.0.0.1:3306/mydb" % quote_plus("12345678x@X")
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

SECRET_KEY = "fb3461446ae87cd4161ad358993f3f33dea24d94462cf7046ff8356f93a0b25a"