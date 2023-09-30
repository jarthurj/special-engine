# from .models import Deck
# from django.contrib.auth.models import User

# def user_decks():
# 	decks = Deck.objects.filter(user=User.objects.filter(email=request.user).first())
# 	lister = []
# 	for d in decks:
# 		lister.append((d.id,d.name))
# 	return tuple(lister)