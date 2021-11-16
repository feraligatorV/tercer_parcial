import graphene
from graphene import relay, ObjectType
from graphene import types
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from typescards.models import Category, Types
from typescards.models import Types


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'cards']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class CardsNode(DjangoObjectType):
    class Meta:
        model = Types
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'year': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    types = relay.Node.Field(CardsNode)
    all_types = DjangoFilterConnectionField(CardsNode)
