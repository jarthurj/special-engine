from django.db import models
from apps.card_search.models import Card
from django.contrib.auth.models import User

class Deck(models.Model):
	card = models.ManyToManyField(Card, related_name='cards')
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=100)
	user = models.ManyToManyField(User, related_name='users')