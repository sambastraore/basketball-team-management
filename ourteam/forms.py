from django import forms
from . models import Game, Stats

class GameForm(forms.ModelForm):
    
    class Meta:
        model = Game
        fields=['date','adversaire']


class GameForm1(forms.ModelForm):
    victoire = forms.BooleanField(required=False)
    class Meta:
        model = Game
        fields=['victoire']

class StatsForm(forms.ModelForm) : 
    class Meta : 
        model = Stats
        exclude = ['game']