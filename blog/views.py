from django.http import HttpResponse


def post_list(request, post_title=None, post_slug=None, post_uuid=None, post_int=None):
    if post_title is not None:
        return HttpResponse(f"post list page --> title: {post_title}")
    elif post_slug is not None:
        return HttpResponse(f"post list page ---> slug: {post_slug}")
    elif post_uuid is not None:
        return HttpResponse(f"post list page --> uuid {post_uuid}")
    elif post_int is not None:
        return HttpResponse(f"post list page ---> int:  {post_int}")
    else:
        return HttpResponse("post list page")


def category_list(request, year=None, month=None):
    if month is not None:
        return HttpResponse(f"category list page --> {year}/{month}")
    elif year is not None:
        return HttpResponse(f"category list page ---> {year}")
    else:
        return HttpResponse("category list page")
