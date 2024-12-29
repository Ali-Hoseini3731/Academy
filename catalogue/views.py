from django.shortcuts import render
from django.http import HttpResponse


def list_catalogue(request):
    return HttpResponse("list of catalogue")
