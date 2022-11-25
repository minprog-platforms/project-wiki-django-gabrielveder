from django.urls import path

from . import views

# list of urls for the 'encyclopedia' app

""" For each desired URL, add an item to the urlpatterns list that contains a call to 
the path function with two or three arguments: (1) A string representing the URL path, (2) a function from
views.py that we wish to call when that URL is visited, and (3) (optionally) a name for that path. """

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_title>", views.entry, name="entry_title"),
]
