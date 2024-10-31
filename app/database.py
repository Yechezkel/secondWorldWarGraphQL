from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from models import *


connection_string = "postgresql://admin:1234@localhost:5437/missions_db"
                  # 'postgresql://omermunk:1234@db:5432/users_subjects_db'
engine = create_engine(connection_string, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind=engine))

# def init_db():
#     import models  #  why??
#     Base.metadata.create_all(bind = engine)