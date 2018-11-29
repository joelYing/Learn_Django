from django.conf.urls import url, include
from firstapp.views import index, book

urlpatterns = [
    url('^index/$', index),
    url('^(\d+)/$', book)
]