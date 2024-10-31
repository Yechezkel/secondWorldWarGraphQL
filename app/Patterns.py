import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import CountryModel, CityModel, TargetTypeModel, MissionModel, TargetModel
import graphene as g



class CountryPattern(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (g.relay.Node, )

class CityPattern(SQLAlchemyObjectType):
    class Meta:
        model = CityModel
        interfaces = (g.relay.Node, )

class TargetTypePattern(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypeModel
        interfaces = (g.relay.Node, )

class MissionPattern(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (g.relay.Node, )

class TargetPattern(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (g.relay.Node, )

