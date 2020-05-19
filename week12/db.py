from sqlalchemy import (Column, Integer, String, CheckConstraint)
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_NAME = 'urls.db'

engine = create_engine(f"sqlite:///{DB_NAME}")
Base = declarative_base()
Session = sessionmaker(bind=engine, expire_on_commit=False)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def create_tables():
    Base.metadata.create_all(engine)


class Url(Base):
    __tablename__ = "urls"
    url_id = Column(Integer, primary_key=True)
    url = Column(String(300), nullable=False, unique=True)
    add_all_children = Column(String(5), CheckConstraint('add_all_children = "True" or add_all_children = "False"'))
