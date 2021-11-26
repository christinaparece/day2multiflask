import os
class Config():
    REGISTERED_USERS = {
        'christinaparece@gmail.com':{"name":"Christina","password":"abc123"}
        
    }
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
