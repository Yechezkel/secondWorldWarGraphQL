from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



connection_string = "postgresql://admin:1234@localhost:5437/missions_db"
engine = create_engine(connection_string)
db_session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind=engine))
