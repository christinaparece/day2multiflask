import os
class Config():
    REGISTERED_USERS = {
        'christinaparece@gmail.com':{"name":"christina","password":"1234"}
        
    }
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI= os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=("QLALCHEMY_TRACK_MODIFICATIONS")