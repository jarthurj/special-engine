from django import forms

COLOR_CHOICES = (
	('blue','Blue'),
	('black','Black'),
	('white','White'),
	('red','Red'),
	('green','Green'))
EXACT = (
	('exact','Exactly these colors'),
	('contains','Contains these colors'))
RARITY = (
	('mythic','mythic'),
	('rare','rare'),
	('uncommon','uncommon'),
	('common','common'))
MPT = (
	('mana', 'Converted Mana Cost'),
	('power', 'Power'),
	('toughness', 'Toughness'),)
MPTCONS = (
	("equal","equal to"),
	("gt","greater than to"),
	("lt","less than to"),
	("lte","less than or equal to"),
	("gte","greater than or equal to"),
	("nte","not equal to"),)
LRB = (
	("banned","Banned"),
	("restricted","Restricted"),
	("legal","Legal"),)
GAME_TYPES=(
	('standard',"Standard"),
	('historic',"Historic"),
	('pioneer',"Pioneer"),
	('premodern',"Premodern"),
	('paupercommander',"Paupercommander"),
	('duel',"Duel"),
	('oldschool',"Oldschool"),
	('modern',"Modern"),
	('brawl',"Brawl"),
	('pauper',"Pauper"),
	('predh',"Predh"),
	('future',"Future"),
	('vintage',"Vintage"),
	('legacy',"Legacy"),
	('oathbreaker',"Oathbreaker"),
	('historicbrawl',"Historicbrawl"),
	('penny',"Penny"),
	('alchemy',"Alchemy"),
	('commander',"Commander"),
	('gladiator',"Gladiator"),
	('explorer',"Explorer"),)


class CardSearch(forms.Form):
	card_name = forms.CharField(max_length=50)
	colors = forms.MultipleChoiceField(
				widget=forms.CheckboxSelectMultiple,
				choices=COLOR_CHOICES)
	colors_identity = forms.MultipleChoiceField(
				widget=forms.CheckboxSelectMultiple,
				choices=COLOR_CHOICES)
	exactly_or_not = forms.MultipleChoiceField(
				widget=forms.SelectMultiple,
				choices=EXACT)
	rarity = forms.MultipleChoiceField(
				widget=forms.CheckboxSelectMultiple,
				choices=RARITY)
	#mpt = mana power toughness
	mpt = forms.MultipleChoiceField(
				widget=forms.Select,
				choices=MPT)
	mpt_condition = forms.MultipleChoiceField(
				widget=forms.Select,
				choices=MPTCONS)
	mpt_parameter = forms.CharField(max_length=10)
	lrb = forms.MultipleChoiceField(
				widget=forms.Select,
				choices=LRB)
	game_types = forms.MultipleChoiceField(
				widget=forms.Select,
				choices=GAME_TYPES)
	type_line = forms.CharField(max_length=50)
	any_text = forms.CharField(max_length=50)