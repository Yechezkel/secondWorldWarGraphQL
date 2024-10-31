import graphene as g
from database import db_session
from patterns import CountryPattern, CityPattern, TargetTypePattern, MissionPattern, TargetPattern
from models import CountryModel, CityModel, TargetTypeModel, MissionModel, TargetModel


class Query(g.ObjectType):

    # country by id
    country_by_id = g.Field(CountryPattern, id=g.Int(required=True))
    def resolve_country_by_id(self, info, id):
        return db_session.query(CountryModel).get(id)

    # city by id
    city_by_id = g.Field(CityPattern, id=g.Int(required=True))
    def resolve_city_by_id(self, info, id):
        return db_session.query(CityModel).get(id)

    # target type by id
    target_type_by_id = g.Field(TargetTypePattern, id=g.Int(required=True))
    def resolve_target_type_by_id(self, info, id):
        return db_session.query(TargetTypeModel).get(id)

    # mission by id
    mission_by_id = g.Field(MissionPattern, id=g.Int(required=True))
    def resolve_mission_by_id(self, info, id):
        return db_session.query(MissionModel).get(id)

    # target by id
    target_by_id = g.Field(TargetPattern, id=g.Int(required=True))
    def resolve_target_by_id(self, info, id):
        return db_session.query(TargetModel).get(id)


# query number 2

    missions_by_date_range = g.List(MissionPattern, date_start = g.Date(required=True), date_end = g.Date(required=True))
    def resolve_missions_by_date_range(self, info, date_start, date_end):
        return db_session.query(MissionModel).filter(MissionModel.mission_date >= date_start ,MissionModel.mission_date <= date_end).all()

# query number 3

    # פחות יעיל אבל עובד (האם הוא מוחק כפילויות של משימה שיש לה שני מטרות שמקושרות אליה או שהיא תגיע פעמיים?)
    # mission_by_country_name = g.List(MissionPattern, name=g.String(required=True))
    # def resolve_mission_by_country_name(self, info, name):
    #     targets = db_session.query(TargetModel).join(CityModel).join(CountryModel).filter(CountryModel.country_name == name).all()
    #     return [target.mission for target in targets if target.mission] if targets else []

    # למה זה יוצר שגיאה מה זה שונה מהקודם, בכל אופן הוא לא יעיל בדיוק כמו הקודם
    # mission_by_country_name = g.List(MissionPattern, name=g.String(required=True))
    # def resolve_mission_by_country_name(self, info, name):
    #     targets = db_session.query(TargetModel).filter(TargetModel.city.country.has(CountryModel.country_name == name)).all()
    #     return [target.mission for target in targets if target.mission] if targets else []

    missions_by_country_name = g.List(MissionPattern, name=g.String(required=True))
    def resolve_missions_by_country_name(self, info, name):
        return db_session.query(MissionModel).join(TargetModel).join(CityModel).join(CountryModel).filter(CountryModel.country_name == name).all()

# query number 4
    missions_by_target_industry = g.List(MissionPattern, industry=g.String(required=True))
    def resolve_missions_by_target_industry(self, info, industry):
        return db_session.query(MissionModel).join(TargetModel).filter(TargetModel.target_industry == industry).all()

# query number 6
    targets_by_target_type = g.List(TargetPattern, type_name=g.String(required=True))
    def resolve_targets_by_target_type(self, info, type_name):
        return db_session.query(TargetModel).join(TargetTypeModel).filter(TargetTypeModel.target_type_name == type_name).all()




# others, some examples

    # country_by_name = g.List(CountryPattern, name = g.String(required=True))
    # def resolve_country_by_name(self, info, name):
    #     country = db_session.query(CountryModel).filter_by(country_name=name).first()
    #     return [country] if country else []

    # cities_by_country_id_a = g.List(CityPattern, id=g.Int(required=True))
    # def resolve_cities_by_country_id_a(self, info, id):
    #     country = db_session.query(CountryModel).get(id)
    #     return country.cities if country else []
    #
    # cities_by_country_id_b = g.List(CityPattern, id=g.Int(required=True))
    # def resolve_cities_by_country_id_b(self, info, id):
    #     return db_session.query(CityModel).filter_by(country_id=id).all()

    # cities_by_country_name = g.List(CityPattern, name=g.String(required=True))
    # def resolve_cities_by_country_name_a(self, info, name):
    #     return db_session.query(CityModel).filter(CityModel.country.has(CountryModel.country_name == name)).all() # .filter(CityModel.country.has(country_name=name)).all()
    #
