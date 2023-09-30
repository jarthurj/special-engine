from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import DeckForm
from .models import Deck, CardDeck
from django.contrib.auth.models import User
from apps.card_search.models import Card
def decks(request):
	user_decks = Deck.objects.none()
	# print(request.user.id)
	# print(User.objects.get(id=request.user.id))
	print()
	if len(Deck.objects.filter(user=User.objects.get(id=request.user.id))) > 0:
		user_decks = Deck.objects.filter(user=User.objects.get(id=request.user.id))
	context = {
		'decks':user_decks,
		'form':DeckForm(),
	}
	return render(request, 'decks/decks.html',context)

def add_deck(request):
	d = Deck.objects.create(name=request.POST['deck_name'], desc=request.POST['deck_description'])
	d.user.add(User.objects.get(id=request.user.id))
	return redirect('decks')

def add_card(request):
	for key, value in request.POST.items():
		print(key, value, type(value))
	d = Deck.objects.get(id=request.POST['deck_id'])
	c = Card.objects.get(id=request.POST['card_id'])
	for x in range(0, int(request.POST['quantity'])):
		CardDeck.objects.create(card=c,deck=d)
	url_redirect="/card/"+str(c.id)
	return redirect(url_redirect)

def deck_detail(request, deck_id):
	histo = {}
	histo_id = {}
	histo2 = {}
	lister = []
	for card in Deck.objects.get(id=deck_id).card.all():
		histo[card.name] = histo.get(card.name, 0) + 1
		histo_id[card.name] = card.id
	for key, value in histo.items():
		lister.append({'name':key,'quantity':value,'id':histo_id[key]})
	for x in range(0,len(lister)):
		histo2[str(x)] = lister[x]
	print(histo2)
	# data = serializers.serialize('json', lister)
	context = {
		'cards':lister,
		'deck_id':deck_id,
	}
	return render(request, "decks/deck_detail.html", context)

def remove_card(request):
	for x in range(0, int(request.POST['quantity'])):
		cd = CardDeck.objects.filter(card=request.POST['card_id'], 
			deck=request.POST['deck_id']).first()
		cd.delete()
	url_redirect="/decks/deck_detail/"+request.POST['deck_id']
	return redirect(url_redirect)
