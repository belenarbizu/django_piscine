from django import forms


class SearchForm(forms.Form):
    min_date = forms.DateField(required=True)
    max_date = forms.DateField(required=True)
    diameter = forms.IntegerField(required=True)
    gender = forms.CharField(required=True)