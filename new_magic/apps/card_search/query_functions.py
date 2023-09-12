from django.db.models.query import QuerySet
from .models import *


def name_query(card_name):
	name_cards = Card.objects.filter(name__contains=card_name).all()
	return name_cards

def color_query(colors_list,exact_or_not):
	if exact_or_not == 'contains':
		cards_list = []
		all_cards = Card.objects.all()
		for color in colors_list:
			cards_list.append(Color.objects.filter(color=color).first().cards.all())
		return all_cards.intersection(*cards_list)
	else:
		difference_colors = []
		for c in ['R','W','B','U','G']:
			if c not in colors_list:
				difference_colors.append(c)
		cards_list = []
		all_cards = Card.objects.all()
		no_cards = QuerySet()
		for color in colors_list:
			cards_list.append(Color.objects.filter(color=color).first().cards.all())
		cards_list_intersection = all_cards.intersection(*cards_list)
		difference_cards = []
		for color in difference_colors:
			difference_cards.append(Color.objects.filter(color=color).first().cards.all())
		no_cards = no_cards.union(*difference_cards)
		print(no_cards)
		return no_cards.difference(cards_list_intersection)