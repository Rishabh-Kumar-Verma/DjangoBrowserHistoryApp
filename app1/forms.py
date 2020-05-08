from django import forms

class SearchField(forms.Form):
    url=forms.CharField(label="",max_length=200)