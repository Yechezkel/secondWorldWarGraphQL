from queries import Query
from mutations import Mutation
import graphene as g

schema = g.Schema(query=Query, mutation=Mutation)








