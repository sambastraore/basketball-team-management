from django.urls import path
from . views import accueil_view, agenda_view, players_view, performances_view, login_view, logout_view, player_details_view, addgame_view, game_details_view, match_stats_view, not_authenticated_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('home', accueil_view, name='accueil'),
    path('agenda', agenda_view, name='agenda'),
    path('players', players_view, name='players'),
    path('performances', performances_view, name='performances'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('players/<int:player_id>/', player_details_view, name='player_details'),
    path('addgame', addgame_view, name='addgame'),
    path('game_details/<int:game_id>/', game_details_view, name='details_game'),
    path('match_stats/<int:game_id>/', match_stats_view, name='match_stats'),
    path('not_authenticated', not_authenticated_view, name='not_authenticated'),
    

] 



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)