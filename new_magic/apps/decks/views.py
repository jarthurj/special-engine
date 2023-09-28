from django.shortcuts import render, HttpResponse
from .forms import DeckForm
from .models import Deck
def decks(request):
	context = {
		'decks':Deck.objects.filter(User.objects.filter(email=request.user).first()),
		'form':DeckForm(),
	}
	return render(request, 'decks/decks.html',context)