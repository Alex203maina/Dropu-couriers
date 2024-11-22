from django import forms

class LogisticsSearchForm(forms.Form):
    location = forms.CharField(
        label='Search for a Location',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location name'}),
    )
