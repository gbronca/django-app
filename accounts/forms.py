from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        email = forms.EmailField()
        self.fields['date_joined'].widget.attrs.update({'disabled':True, 'readonly':True})
        self.fields['date_joined'].required = False

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined']
        # fields['date_joined'] = forms.CharField(widget=forms.TextInput(attrs={'disabled': True}))
