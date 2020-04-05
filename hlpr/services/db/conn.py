from sqlalchemy import create_engine
import sys


def db_connect():
    try:
        engine = create_engine(
            "sqlite:///hlpr-backend/hlpr/services/db/helpr.db", echo=True
        )
        connection = engine.connect()
        return connection, engine
        print(f"Connected to: {connection}")
    except Exception as e:
        print(f"connection failed {e}")
        sys.exit(1)
