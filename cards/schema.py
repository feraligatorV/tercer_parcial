import graphene

import typescards.schema


class Query(typescards.schema.Query, graphene.ObjectType):
    # Esta clase heredara de multiples consultas
    # segun vayamos agregando aplicaciones a nuestro proyecto
    pass

schema = graphene.Schema(query=Query)