from django import forms
from .models import Person, Referral

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',  
                'placeholder': 'YYYY-MM-DD',
                'class': 'form-control',
                'style': 'width: 314px'
            }),
        }

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['person', 'referral_date', 'referrer_name', 'referral_reason', 'note']

        widgets = {
            'person': forms.Select(attrs={
                'class': 'form-control'
            }),
            'referral_date': forms.DateInput(attrs={
                'type': 'date',  
                'placeholder': 'YYYY-MM-DD',
                'class': 'form-control',
                'style': 'width: 314px'
            })
        }
