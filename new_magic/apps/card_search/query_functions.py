from .models import *


def name_query(card_name):
	name_cards = Card.objects.filter(name__contains=card_name).all()
	return name_cards

def color_query(colors_list,exact_or_not):
	if exact_or_not == 'contains':
		cards_list = []
		all_cards = Card.objects.all()
		for color in colors_list:
			cards_list.append(Color.objects.filter(color=color).first().cards.all())
		return all_cards.intersection(*cards_list)
	else:
		difference_colors = []
		for c in ['R','W','B','U','G']:
			if c not in colors_list:
				difference_colors.append(c)
		print(difference_colors)
		cards_list = []
		all_cards = Card.objects.all()
		for color in colors_list:
			cards_list.append(Color.objects.filter(color=color).first().cards.all())
		cards_list_intersection = all_cards.intersection(*cards_list)

		difference_cards_list = []
		for color in difference_colors:
			difference_cards_list.append(Color.objects.filter(color=color).first().cards.all())

		difference_cards = Card.objects.none().union(*difference_cards_list)
		return_cards = cards_list_intersection.difference(cards_list_intersection.intersection(difference_cards))
		return return_cards

def rarity_query(rarity_list):
	empty_rarity_cards = Card.objects.none()
	for rarity in rarity_list:
		empty_rarity_cards = empty_rarity_cards.union(Rarity.objects.filter(rarity=rarity).first().cards)
	return empty_rarity_cards.all()

def mpt_query(mpt,mpt_cond,mpt_param):
	if mpt=='mana':
		if mpt_cond == 'equal':
			return Card.objects.filter(cmc=Cmc.objects.get(cmc=int(mpt_param)))
		elif mpt_cond == 'gt':
			return Card.objects.filter(cmc__gt=Cmc.objects.get(cmc=int(mpt_param)))
		elif mpt_cond == 'lt':
			return Card.objects.filter(cmc__lt=Cmc.objects.get(cmc=int(mpt_param)))
		elif mpt_cond == 'lte':
			return Card.objects.filter(cmc__lte=Cmc.objects.get(cmc=int(mpt_param)))
		elif mpt_cond == 'gte':
			return Card.objects.filter(cmc__gte=Cmc.objects.get(cmc=int(mpt_param)))
		elif mpt_cond == 'nte':
			gt = Card.objects.filter(cmc__gt=Cmc.objects.get(cmc=int(mpt_param)))
			lt = Card.objects.filter(cmc__lt=Cmc.objects.get(cmc=int(mpt_param)))
			return gt.union(lt)
	elif mpt=='power':
		if mpt_cond == 'equal':
			return Card.objects.filter(power=Power.objects.get(power=int(mpt_param)))
		elif mpt_cond == 'gt':
			return Card.objects.filter(power__gt=Power.objects.get(power=int(mpt_param)))
		elif mpt_cond == 'lt':
			return Card.objects.filter(power__lt=Power.objects.get(power=int(mpt_param)))
		elif mpt_cond == 'lte':
			return Card.objects.filter(power__lte=Power.objects.get(power=int(mpt_param)))
		elif mpt_cond == 'gte':
			return Card.objects.filter(power__gte=Power.objects.get(power=int(mpt_param)))
		elif mpt_cond == 'nte':
			gt = Card.objects.filter(power__gt=Power.objects.get(power=int(mpt_param)))
			lt = Card.objects.filter(power__lt=Power.objects.get(power=int(mpt_param)))
			return gt.union(lt)
	elif mpt=='toughness':
		if mpt_cond == 'equal':
			return Card.objects.filter(toughness=Toughness.objects.get(toughness=int(mpt_param)))
		elif mpt_cond == 'gt':
			return Card.objects.filter(toughness__gt=Toughness.objects.get(toughness=int(mpt_param)))
		elif mpt_cond == 'lt':
			return Card.objects.filter(toughness__lt=Toughness.objects.get(toughness=int(mpt_param)))
		elif mpt_cond == 'lte':
			return Card.objects.filter(toughness__lte=Toughness.objects.get(toughness=int(mpt_param)))
		elif mpt_cond == 'gte':
			return Card.objects.filter(toughness__gte=Toughness.objects.get(toughness=int(mpt_param)))
		elif mpt_cond == 'nte':
			gt = Card.objects.filter(toughness__gt=Toughness.objects.get(toughness=int(mpt_param)))
			lt = Card.objects.filter(toughness__lt=Toughness.objects.get(toughness=int(mpt_param)))
			return gt.union(lt)
	elif mpt=='none':
		return Card.objects.none()


def lrb_query(lrb, game_type):
	legals =  Legality.objects.get(legality=lrb,
								game_type=GameType.objects.get(game_type=game_type))
	return legals.cards.all()
