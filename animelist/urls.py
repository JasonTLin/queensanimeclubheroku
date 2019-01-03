from django.urls import path
from . import views as animelist_views

urlpatterns = [
    path('', animelist_views.animelist, name='animelist'),
    path('results/', animelist_views.search, name="results")
]
