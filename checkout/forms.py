from django import forms
import datetime

class PaymentForm(forms.Form):
    now = datetime.datetime.now()
    current_year = now.year

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(current_year, current_year + 10)]
    
    name = forms.CharField(label='Name on Credit Card',
                                       max_length=200)
    credit_card_number = forms.CharField(label='Credit Card number',
                                         required=False,
                                         max_length=19,
                                         min_length=14)
    cvv = forms.CharField(label='Security code(CVV)',
                          required=False,
                          max_length=4,
                          min_length=3)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
