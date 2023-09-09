from django import forms

from languages.models import program_language
from progects.models import Progect


class ProgectForm(forms.ModelForm):
    name = forms.CharField(label='Назва проекту', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введіть назву проекту'
    }))
    progect_progres = forms.IntegerField(label='Прогрес',
                                         widget=forms.NumberInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Прогрес'
    }))
    from_language = forms.ModelChoiceField(
        label='З якої мови', queryset=program_language.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        ))
    to_language = forms.ModelChoiceField(
        label='На яку мову', queryset=program_language.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        ))

    class Meta:
        model = Progect
        fields = '__all__'