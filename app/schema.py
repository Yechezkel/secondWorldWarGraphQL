import graphene as g
from database import db_session
from Patterns import CountryPattern, CityPattern, TargetTypePattern, MissionPattern, TargetPattern
from models import CountryModel, CityModel, TargetTypeModel, MissionModel, TargetModel


class Query(g.ObjectType):

    country_by_id = g.Field(CountryPattern, id=g.Int(required=True))
    def resolve_country_by_id(self, info, id):
        return db_session.query(CountryModel).get(id)

    city_by_id = g.Field(CityPattern, id=g.Int(required=True))
    def resolve_city_by_id(self, info, id):
        return db_session.query(CityModel).get(id)

    target_type_by_id = g.Field(TargetTypePattern, id=g.Int(required=True))
    def resolve_target_type_by_id(self, info, id):
        return db_session.query(TargetTypeModel).get(id)

    mission_by_id = g.Field(MissionPattern, id=g.Int(required=True))
    def resolve_mission_by_id(self, info, id):
        return db_session.query(MissionModel).get(id)

    target_by_id = g.Field(TargetPattern, id=g.Int(required=True))
    def resolve_target_by_id(self, info, id):
        return db_session.query(TargetModel).get(id)


schema = g.Schema(query=Query)





