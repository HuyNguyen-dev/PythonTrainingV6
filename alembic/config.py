from urllib.parse import quote_plus

#Connect DB
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:%s@127.0.0.1:3306/mydb" % quote_plus("12345678x@X")
SQLALCHEMY_TRACK_MODIFICATIONS = True