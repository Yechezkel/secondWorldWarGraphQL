import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from database import db_session
from models import CountryModel


class Country(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    country_by_id = graphene.Field(Country, id=graphene.Int(required=True))

    def resolve_country_by_id(self, info, id):
        return db_session.query(CountryModel).get(id)


schema = graphene.Schema(query=Query)