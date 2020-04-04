"""
This file stores a class which holds app configuration. Attributes of the class
are values for configuration
"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.flaskenv'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-unsecure-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///{}'.\
        format(os.path.join(basedir, 'app.db'))
