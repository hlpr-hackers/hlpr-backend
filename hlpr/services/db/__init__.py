"""Module that manages database connection."""
import os
from sqlalchemy_wrapper import SQLAlchemy


# Connect to the database
connection = SQLAlchemy(os.environ['DATABASE_URL'])


