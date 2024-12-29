from django.urls import path
from catalogue.views import list_catalogue

urlpatterns = [
    path('list/', list_catalogue),
]
