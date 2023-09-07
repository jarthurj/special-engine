from django import forms

COLOR_CHOICES = (
	('blue','Blue'),
	('black','Black'),
	('white','White'),
	('red','Red'),
	('green','Green'))

EXACT = (
	('1','Exactly these colors'),
	('2','Contains these colors')
	)

class CardSearch(forms.Form):
	card_name = forms.CharField(max_length=50)
	colors = forms.MultipleChoiceField(
				widget=forms.CheckboxSelectMultiple,
				choices=COLOR_CHOICES)
	exactly_or_not = forms.MultipleChoiceField(
				widget=forms.SelectMultiple,
				choices=EXACT)
	