from django.urls import path

from . import views


urlpatterns = [
    path('quoteapihome.html', views, name='home'), ]