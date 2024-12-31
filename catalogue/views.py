from django.http import HttpResponse


def catalogue_list(request):
    return HttpResponse("catalogue list page")
