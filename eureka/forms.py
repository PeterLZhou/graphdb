from django import forms

class QueryForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a Question'}))
