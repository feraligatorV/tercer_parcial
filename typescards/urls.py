from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_new, name='card_new'),
]