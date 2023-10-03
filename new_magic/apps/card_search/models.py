from django.db import models


class Cmc(models.Model):
	cmc = models.DecimalField(decimal_places=1, max_digits=9, null=True)
	def __str__(self):
		return str(self.cmc)

class Power(models.Model):
	power = models.IntegerField(blank=True,null=True)
	def __str__(self):
		return str(self.power)
class Toughness(models.Model):
	toughness = models.IntegerField(blank=True,null=True)
	def __str__(self):
		return str(self.toughness)
class Rarity(models.Model):
	rarity = models.CharField(max_length=10)
	def __str__(self):
		return str(self.rarity)
class Layout(models.Model):
	layout = models.CharField(max_length=20)
	def __str__(self):
		return str(self.layout)
class Digital(models.Model):
	digital = models.BooleanField()
	def __str__(self):
		return str(self.digital)
class Reserved(models.Model):
	reserved = models.BooleanField()
	def __str__(self):
		return str(self.reserved)
class CardSet(models.Model):
	name = models.CharField(max_length=50)
	set_code = models.CharField(max_length=20)
	def __str__(self):
		return "Name of set:" + str(name) + "Set Code/Acronym:" + str(set_code)
class GameType(models.Model):
	game_type = models.CharField(max_length=20)
	def __str__(self):
		return str("Game/Format type:"+game_type)
class Legality(models.Model):
	legality = models.CharField(max_length=20)
	game_type = models.ForeignKey(GameType, related_name="legalities",on_delete=models.CASCADE)
	def __str__(self):
		
class ManaCost(models.Model):
	mana_cost = models.CharField(max_length=20)

class Card(models.Model):
	name = models.CharField(max_length=50)
	power = models.ForeignKey(Power, related_name="cards", on_delete=models.CASCADE, null=True)
	toughness = models.ForeignKey(Toughness, related_name="cards", on_delete=models.CASCADE, null=True)
	cmc = models.ForeignKey(Cmc, related_name="cards", on_delete=models.CASCADE)
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
	image_small = models.URLField(null=True)
	image_normal = models.URLField(null=True)
	image_large = models.URLField(null=True)
	layout = models.ForeignKey(Layout, related_name="cards", on_delete=models.CASCADE)
	legality = models.ManyToManyField(Legality, related_name="cards")
	type_line = models.CharField(max_length=100)
	mana_cost = models.ForeignKey(ManaCost, related_name="cards", on_delete=models.CASCADE)

class Color(models.Model):
	color = models.CharField(max_length=3)
	cards = models.ManyToManyField(Card, related_name="colors")

class ColorIdentity(models.Model):
	color_identity = models.CharField(max_length=3)
	cards = models.ManyToManyField(Card, related_name="color_identities")

class Keyword(models.Model):
	keyword = models.CharField(max_length=20)
	cards = models.ManyToManyField(Card, related_name="keywords")