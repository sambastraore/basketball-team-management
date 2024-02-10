from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Player(models.Model) : 
    POSTE_CHOICES = [
        ('PG', 'Meneur'),
        ('SG', 'Arrière'),
        ('SF', 'Ailier'),
        ('PF', 'Ailier fort'),
        ('C', 'Pivot'),
    ]   
    prenom = models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    age = models.IntegerField()
    poste = models.CharField(max_length=2, choices=POSTE_CHOICES)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='photos/')
    games = models.ManyToManyField('Game', through='Stats')
    
    

    def __str__(self):
        return f"{self.prenom} {self.nom}"



class Game(models.Model) : 
    date = models.DateField()
    adversaire = models.CharField(max_length=15)
    victoire = models.BooleanField(default=False)
    ourscore = models.IntegerField(null=True,validators=[MinValueValidator(0), MaxValueValidator(200)])
    opp_score = models.IntegerField(null=True,validators=[MinValueValidator(0), MaxValueValidator(200)])
    players = models.ManyToManyField('Player', through='Stats')
    def __str__(self):
        return f"match du {self.date} "


class Stats(models.Model) : 
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    rebounds = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    assists = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    steals = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    blocks = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])

    class Meta:
        unique_together = ('game', 'player')


    def __str__(self):
        return f" Stats de {self.player} pour le {self.game}"

    


