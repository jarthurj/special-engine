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
	for key, value in request.POST.items():
		print(key, value, type(value))
	all_cards = Card.objects.all()

	name_cards = name_query(request.POST['card_name'])

	color_cards = color_query(request.POST.getlist('colors'),
		request.POST['exactly_or_not'])

	color_identity_cards = color_identity_query(request.POST.getlist('colors_identity'))

	rarity_cards = rarity_query(request.POST.getlist('rarity'))

	mpt_cards = mpt_query(request.POST['mpt'],
							request.POST['mpt_condition'],
							request.POST['mpt_parameter'])

	lrb_cards = lrb_query(request.POST['lrb'],request.POST['game_types'])
	all_text_cards = all_text_query(request.POST['any_text'])
	type_cards = type_query(request.POST['type_line'])

	all_queries = [name_cards, color_cards,color_identity_cards,
						rarity_cards, mpt_cards, lrb_cards, 
						all_text_cards, type_cards]

	matching_queries = []

	for query in all_queries:
		if query != Card.objects.none():
			matching_queries.append(query)

	matching_cards = matching_queries[0].intersection(*matching_queries)
	matching_cards_ids = []
	for x in matching_cards:
		matching_cards_ids.append(x.id)
	request.session['card_ids'] = matching_cards_ids
	# context = {
	# 		'cards':matching_cards,
	# 	}
	# return render(request, 'card_search/cards.html', context)
	return redirect('cards',page=1)

def card_pages(request,page):
	if page ==1:
		cards = request.session['card_ids'][:60]
	else:
		cards = request.session['card_ids'][60*page:(60*page)+60]
	to_union = []
	for x in cards:
		to_union.append(Card.objects.filter(id=x))
	page_cards = to_union[0].union(*to_union)
	page_one = False
	if page == 1:
		page_one = True
	context = {
		'cards':page_cards,
		'page':page,
		'page_one':page_one,
		'prev_page':page-1,
		'next_page':page+1,
	}
	return render(request, 'card_search/cards.html', context)

def single_card(request,card_id):
	card = Card.objects.filter(id=card_id).first()
	context = {
		'card':card,
	}
	return render(request,'card_search/single_card.html', context)
