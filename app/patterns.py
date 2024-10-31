from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import CountryModel, CityModel, TargetTypeModel, MissionModel, TargetModel
import graphene as g


class TargetPattern(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (g.relay.Node, )

class TargetTypePattern(SQLAlchemyObjectType):
    targets = g.List(TargetPattern)
    class Meta:
        model = TargetTypeModel
        interfaces = (g.relay.Node, )

class MissionPattern(SQLAlchemyObjectType):
    targets = g.List(TargetPattern)
    class Meta:
        model = MissionModel
        interfaces = (g.relay.Node, )

class CityPattern(SQLAlchemyObjectType):
    targets = g.List(TargetPattern)
    class Meta:
        model = CityModel
        interfaces = (g.relay.Node, )

class CountryPattern(SQLAlchemyObjectType):
    cities = g.List(CityPattern)
    class Meta:
        model = CountryModel
        interfaces = (g.relay.Node, )








