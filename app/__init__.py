from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


#needs to be at bottom
from app import routes