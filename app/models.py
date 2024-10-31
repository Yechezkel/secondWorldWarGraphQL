from sqlalchemy import Column , Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class CountryModel(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)  # , autoincrement=True
    country_name = Column(String)

