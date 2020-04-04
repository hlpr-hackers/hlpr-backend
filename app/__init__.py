from flask import Flask
from config import Config

app = Flask(__name__)


def create_app(config_class=Config):
    pass