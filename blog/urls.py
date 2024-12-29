from django.urls import path
from blog.views import list

urlpatterns = [
    path('list/', list),
]
