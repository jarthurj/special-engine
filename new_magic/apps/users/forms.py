from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	username =forms.CharField(max_length=50, 
				required=False,
				widget=forms.TextInput(attrs={'class':'',
						'placeholder':'Any words in the name ex."Fire"'}),
				label="Card Name:")
	class Meta:
		model = User
		fields = ['username', 'email']