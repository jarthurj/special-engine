from django.db import models
from apps.card_search.models import Card


class Deck(models.Model):
	card = models.ManyToManyField(Card, related_name='cards')