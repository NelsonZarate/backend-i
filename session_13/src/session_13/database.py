import os
from pytest import Session
from sqlmodel import SQLModel, create_engine
from session_13.models import Task

def get_engine():
    DB_USER = os.getenv("DB_USER",None) 
    DB_PASSWORD = os.getenv("DB_PASSWORD",None)
    DB_HOST = os.getenv("DB_HOST",None)
    DB_PORT = os.getenv("DB_PORT",None)
    DB_NAME = os.getenv("DB_NAME",None)
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    return engine 

def get_session()-> Session:
    return Session(get_engine)
    
def create_task(task:Task):
    assert task
    with get_session() as session:
        session.add(task)
        session.commit()