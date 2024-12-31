from django.urls import path, re_path, register_converter
from blog.utils import FourDigitsYear
from blog.views import post_list, category_list

register_converter(FourDigitsYear, "four")

urlpatterns = [
    path('list/', post_list),
    path('list/<str:post_title>/', post_list),
    path('list/<slug:post_slug>/', post_list),
    path('list/<uuid:post_uuid>/', post_list),
    path('list/<int:post_id>/', post_list),
    path('category/list/', category_list),
    path("archive/<four:year>/", category_list),
    # path('archive/<int:year>/', category_list),
    # re_path(r'archive/(?P<year>[0-9]{2,4})/', category_list),
    path('archive/<int:year>/<int:month>/', category_list),
]
