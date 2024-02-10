from django.shortcuts import render, get_object_or_404, redirect
from . models import Player, Game, Stats
from . forms import GameForm, GameForm1, StatsForm
from django.forms import inlineformset_factory
from itertools import zip_longest
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
import pushy 


players = Player.objects.all()
StatsFormSet = inlineformset_factory(Game, Stats, fields=('player', 'points', 'rebounds', 'assists', 'steals', 'blocks'), extra=len(players), can_delete=False)



def accueil_view(request) : 
    context = {}
    
    return render(request,'accueil.html',context)

@login_required(login_url='not_authenticated')
def agenda_view(request) : 
    data = Game.objects.annotate(stats_count=Count('stats'))
    return render(request,'agenda.html',{'data' : data})


def players_view(request) : 
    players_data = Player.objects.all()
    return render(request,'joueurs.html',{'players' : players_data})


def performances_view(request) : 
    matches = Game.objects.all()
    context = {'matches' : matches}
    return render(request,'performances.html',context)


def login_view(request) : 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')  
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def logout_view(request) : 
    logout(request)
    return redirect('accueil')


def player_details_view(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    context = {
        'player': player
    }
    
    return render(request, 'oneplayer.html', context)


def addgame_view(request):
    form = GameForm(request.POST)
    if form.is_valid() : 
        form.save()
        return redirect('agenda')
    else : 
        form = GameForm()
    return render(request, 'addgame.html', {'form' : form})


def game_details_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    

    if request.method == 'POST':
        form_game = GameForm1(request.POST, instance=game)
        formset_stats = StatsFormSet(request.POST, instance=game)
        if form_game.is_valid() and formset_stats.is_valid():
            form_game.save()
            
            formset_stats.save()
            return redirect('agenda')

    else:
        form_game = GameForm1(instance=game)
        formset_stats = StatsFormSet(instance=game)

    context = {
        'game': game,
        'form_game': form_game,
        'formset_stats': formset_stats,
    }

    return render(request, 'onegame.html', context)


def match_stats_view(request, game_id):
    match = Game.objects.get(id=game_id)
    stats = Stats.objects.filter(game=match)
    return render(request, 'match_stats.html', {'match': match, 'stats': stats})


def not_authenticated_view(request):
    return render(request, 'not_auth.html')
