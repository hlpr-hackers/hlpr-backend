from sqlalchemy import create_engine


def _connect():
    try:
        engine = create_engine('sqlite:///my.db', echo=True)
        conn = engine.connect()
        print(f'Connected to: {conn}')
        return conn
    except Exception as e:
        print(f"connection failed {e}")