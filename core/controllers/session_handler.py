import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session

from core.config import postgres_uri

engine = sqlalchemy.create_engine(postgres_uri())
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def dbconnect(func):
    def inner(*args, **kwargs):
        session = Session()
        try:
            value = func(*args, **kwargs)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            Session.remove()
        return value
    return inner
