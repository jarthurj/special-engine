from django import forms

class DeckForm(forms.Form):
	deck_name = forms.CharField(max_length=100)
	deck_description = forms.CharField(max_length=100)

class AddCardForm(forms.Form):
	deck_name = forms.SelectMultiple()