from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('reviews/', views.reviews, name='reviews'),
  path('sports/', views.index, name='index'),
  path('sports/<int:sport_id>/', views.detail, name='detail')
]