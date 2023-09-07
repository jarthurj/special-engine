from django.shortcuts import render, HttpResponse
from .forms import CardSearch
def index(request):
	context = {
		'search_form':CardSearch()
	}
	return render(request, "card_search/index.html",context)
