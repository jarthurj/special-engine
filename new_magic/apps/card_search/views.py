from django.shortcuts import render, HttpResponse, redirect
from .forms import CardSearch
from .models import *
from django.db.models.query import QuerySet
def index(request):
	context = {
		'search_form':CardSearch()
	}
	return render(request, "card_search/index.html",context)

def search(request):
	# for key, value in request.GET.items():
	# 	print(key, value)
	
	name_cards = Card.objects.filter(name__contains=request.GET['card_name']).all()

	# matching_cards = empty_set.intersection(name_cards).all()
	context = {
			'cards':name_cards,
		}
	return render(request, 'card_search/cards.html', context)
