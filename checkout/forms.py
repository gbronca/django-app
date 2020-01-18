from django import forms
import datetime

class PaymentForm(forms.Form):
    now = datetime.datetime.now()
    current_year = now.year

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(current_year, current_year + 10)]
    
    credit_card_number = forms.CharField(
                         label='Credit Card number',
                         required=True,
                         max_length=16)
    cvv = forms.CharField(label='Security code(CVV)', required=True, max_length=3,min_length=3)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
