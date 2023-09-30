from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.decks, name='decks'),
    path('add_deck/', views.add_deck, name="add_deck"),
    path('add_card/', views.add_card, name="add_card"),
    path('deck_detail/<int:deck_id>/', views.deck_detail, name="deck_detail"),
    path('remove_card/', views.remove_card, name="remove_card"),
]
