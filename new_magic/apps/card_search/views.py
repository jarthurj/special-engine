from django.shortcuts import render, HttpResponse, redirect
from .forms import CardSearch
from .models import *
from django.db.models.query import QuerySet
from .query_functions import *
def index(request):
	context = {
		'search_form':CardSearch()
	}
	return render(request, "card_search/index.html",context)

def search(request):
	# for key, value in request.POST.items():
	# 	print(key, value, type(key), type(value))
	all_cards = Card.objects.all()
	name_cards = name_query(request.POST['card_name'])
	color_cards = color_query(request.POST.getlist('colors'),request.POST['exactly_or_not'])
	# matching_cards = all_cards.intersection(name_cards, color_cards)
	context = {
			'cards':color_cards,
		}
	return render(request, 'card_search/cards.html', context)
