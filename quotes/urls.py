from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_quote, name='random_quote'),
    path('toggle_favourite/<int:quote_id>/', views.toggle_favourite, name='toggle_favourite'),
    path('favourite_quotes/', views.favourite_quotes, name='favourite_quotes'),
    path('remove_favourite/<int:favourite_id>/', views.remove_favourite, name='remove_favourite'),

]
