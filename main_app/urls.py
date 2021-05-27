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
  path('sports/<int:sport_id>/athletes/<int:athletes_id>/', views.assoc_athlete, name='assoc_athlete')
]