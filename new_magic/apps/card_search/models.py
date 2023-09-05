from django.db import models

class Card(models.Model):
	name = models.CharField(max_length=50)
	power = models.IntegerField(null=True)
	toughness = models.IntegerField(null=True)
	cmc = models.IntegerField(null=True)
	rarity = models.ForeignKey(Rarity, related_name="cards", on_delete=models.CASCADE)
	scryfall_id = models.CharField(max_length=100)
	digital = models.ForeignKey(Digital, related_name="cards", on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	reserved = models.ForeignKey(Reserved, related_name="cards", on_delete=models.CASCADE)
	flavor_text = models.CharField(max_length=255)
	collector_number = models.CharField(max_length=10)
	card_set = models.ForeignKey(CardSet, related_name="cards", on_delete=models.CASCADE)
	oracle_text = models.CharField(max_length=200)
	image_small = models.URLField()
	image_normal = models.URLField()
	image_large = models.URLField()
	layout = models.ForeignKey(Layout, related_name="cards", on_delete=models.CASCADE)
	legality = models.ForeignKey(Legality, related_name="cards", on_delete=models.CASCADE)
	type_line = models.CharField()

class Color(models.Model):
	color = models.CharField(max_length=3)
	cards = models.ManyToManyField(Card, related_name="colors")

class ColorIdentity(models.Model):
	color_identity = models.CharField(max_length=3)
	cards = models.ManyToManyField(Card, related_name="color_identities")

class Rarity(models.Model):
	rarity = models.CharField(max_length=10)

class Layout(models.Model):
	layout = models.CharField(max_length=20)

class Digital(models.Model):
	digital = models.BooleanField()

class Reserved(models.Model):
	reserved = models.BooleanField()

class CardSet(models.Model):
	name = models.CharField(max_length=50)
	set_code = models.CharField(max_length=20)

class Keyword(models.Model):
	name = models.CharField(max_length=20)
	cards = models.ManyToManyField(Card, related_name="keywords")

class GameType(models.Model):
	game_type = models.CharField(max_length=20)

class Legality(models.Model):
	legal = models.BooleanField()
	game_type = models.ForeignKey(GameType, related_name="legalities",on_delete=models.CASCADE)

# id DONE
# name DONE
# layout DONE
# image_uris DONE
	# small
	# normal
	# large
	# png
	# art_crop
	# border_crop
# mana_cost HOW DO I IMPLEMENT THIS?
# cmc DONE
# type_line
# oracle_text DONE
# power DONE
# toughness DONE
# colors DONE
# color_identity DONE
# keywords DONE
# legalities DONE
# reserved DONE
# set DONE
# set_name DONE
# collector_number DONE
# digital DONE
# rarity DONE
# flavor_text DONE
