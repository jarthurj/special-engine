from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import DeckForm
from .models import Deck
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
	for x in range(0, int(request.POST['quantity'])):
		d.card.add(Card.objects.get(id=request.POST['card_id']))
	url_redirect="/card/"+str(str(request.POST['card_id']))
	return redirect(url_redirect)