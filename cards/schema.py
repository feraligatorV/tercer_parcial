""" import graphene
import carlist.schema
class Query(carlist.schema.Query, graphene.ObjectType):
    # Esta clase heredara de multiples consultas
    # segun vayamos agregando aplicaciones a nuestro proyecto
    pass
schema = graphene.Schema(query=Query) """
import graphene
from graphene import types
from graphene_django import DjangoObjectType
#como estamos dentro de la carpeta cookbook, pero los modelos estan en la carpetea ingredients
#necesitamos regresar un nivel de carpete por eso agregamos el ".."  al path actual
import sys
sys.path.append("..")
from typescards.models import Category, Types

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "cards")

class CardsType(DjangoObjectType):
    class Meta:
        model = Types
        fields = ("id", "name", "description", "year", "category")

class Query(graphene.ObjectType):
    all_cards = graphene.List(CardsType)
    all_categories = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_categories(root,info):
        return Category.objects.all()
    def resolve_all_cards(root, info):
        # We can easily optimize query count in the resolve method
        return Types.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)