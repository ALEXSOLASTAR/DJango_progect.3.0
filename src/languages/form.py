import attrs as attrs
from django import forms

from languages.models import program_language


class HtmlForm(forms.Form):
    name = forms.CharField(label='Мова')


class LanguagesForm(forms.ModelForm):
    name = forms.CharField(label='Мова', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ведіть мову прогрвмування'
    }))

    class Meta:
        model = program_language
        fields = ('name',)