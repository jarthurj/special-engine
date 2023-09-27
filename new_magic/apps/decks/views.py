from django.shortcuts import render, HttpResponse

def decks(request):
	context = {
		'decks':'plaechodlerzsdzß',
	}
	return render(request, 'decks/decks.html',context)