from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CountryModel(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)  # , autoincrement=True
    country_name = Column(String)
    cities = relationship("CityModel", back_populates="country")

class CityModel(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.country_id'))  # , autoincrement=True
    country = relationship('CountryModel', back_populates='cities')
    longitude = Column(Integer)
    latitude = Column(Integer)
    targets = relationship("TargetModel", back_populates="city")


class TargetTypeModel(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)
    targets = relationship("TargetModel", back_populates="target_type")

class MissionModel(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date)
    aircraft_lost = Column(Integer)
    aircraft_damaged = Column(Integer)
    aircraft_failed = Column(Integer)
    aircraft_returned = Column(Integer)
    bombing_aircraft = Column(Integer)
    attacking_aircraft = Column(Integer)
    airborne_aircraft = Column(Integer)
    targets = relationship("TargetModel", back_populates="mission")


class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    mission = relationship('MissionModel', back_populates='targets')
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    city = relationship('CityModel', back_populates='targets')
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_type = relationship('TargetTypeModel', back_populates='targets')
    target_priority = Column(Integer)



