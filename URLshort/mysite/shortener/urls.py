from django.urls import path, include
from . import views
from django.urls import re_path
from shortener.views import short_redirect_view, home

urlpatterns = [
    path(r'', home.as_view()),
    re_path(r'^(?P<shortcode>[\w-]+)$', short_redirect_view),
]
