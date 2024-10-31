import graphene as g
from database import db_session
from patterns import CountryPattern, CityPattern, TargetTypePattern, MissionPattern, TargetPattern
from models import CountryModel, CityModel, TargetTypeModel, MissionModel, TargetModel


# Mutations

class CreateMission(g.Mutation):
    class Arguments:
        mission_date = g.Date(required=True)
        aircraft_lost = g.Int()
        aircraft_damaged = g.Int()
        aircraft_failed = g.Int()
        aircraft_returned = g.Int()
        bombing_aircraft = g.Int()
        attacking_aircraft = g.Int()
        airborne_aircraft = g.Int()
    mission = g.Field(lambda: MissionPattern)
    def mutate(self, info, mission_date, aircraft_lost=0, aircraft_damaged=0, aircraft_failed=0,
               aircraft_returned=0, bombing_aircraft=0, attacking_aircraft=0, airborne_aircraft=0):
        new_mission = MissionModel(
            mission_id = 0,  # כאן אני צריך להוסיף לוגיקה איך למשוך את הid הגבוה ביותר ואז לתת לכל משימה חדשה שנוצרת id ייחודי שלא קיים עדיין בטבלה של הדאטה בייס
            mission_date=mission_date,
            aircraft_lost=aircraft_lost,
            aircraft_damaged=aircraft_damaged,
            aircraft_failed=aircraft_failed,
            aircraft_returned=aircraft_returned,
            bombing_aircraft=bombing_aircraft,
            attacking_aircraft=attacking_aircraft,
            airborne_aircraft=airborne_aircraft
        )
        db_session.add(new_mission)
        db_session.commit()
        return CreateMission(mission=new_mission)



class Mutation(g.ObjectType):
    create_mission = CreateMission.Field()