from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('reviews/', views.reviews, name='reviews'),
  path('sports/', views.index, name='index'),
  path('sports/new/', views.create_sport, name='create_sport'),
  path('sports/<int:sport_id>/', views.detail, name='detail'),
  path('sports/<int:sport_id>/delete/', views.delete_sport, name='delete_sport'),
  path('sports/<int:sport_id>/edit/', views.update_sport, name='update_sport'),
  path('sports/<int:sport_id>/add_athlete/', views.add_athlete, name='add_athlete'),
  path('sports/<int:sport_id>/delete_athlete/<int:athlete_id>/', views.delete_athlete, name='delete_athlete'),
  path('accounts/signup/', views.signup, name='signup'),
  
  
  path('athlete/<int:athlete_id>/', views.athlete_detail, name='athlete_detail'),
  path('athlete/sponsers/', views.assoc_sponser, name='assoc_sponser')

  # path('athletes/<int:athlete_id>/sponsers/<int:sponser_id>/', views.assoc_sponser, name='assoc_sponser'),
#   path('athlete/sponsers/', views_assoc_sponser, name='assoc_sponser')
#   path('sports/<int:athlete_id>/sponsers/', views.assoc_sponser, name='assoc_sponser'),
#   path('athletes/<int:athlete_id>/sponsers/<int:sponser_id>/remove', views.remove_sponser, name='remove_sponser'),
]


# path('sports/<int:sport_id>/delete_athlete/', views.delete_athlete, name='delete_athlete'),
  # path('sports/<int:sport_id>/athlete/<int:athlete_id>/', views.delete_athlete, name='delete_athlete'),
  # path('sports/<int:sport_id>/athletes/<int:athletes_id>/', views.assoc_athlete, name='assoc_athlete')