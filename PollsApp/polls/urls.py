# Notes
## NOTE: manually created, so that we can first map all the urls of the app here.
## NOTE: we'll link it to the project's url.py to map all the urls of the app to the project.

# Imports
from django.conf.urls import url
from . import views # imports views defined inside polls/views.py


# URLpatterns: mapping of views to URLs
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]
















# Pre-Requisites
""" $ and ^ are regular expression characters that have a special meaning:
the caret means “require that the pattern matches the start of the string,” and the dollar sign means “require that the pattern matches the end of the string.”
For example consider the  following url pattern:
    urlpatterns = patterns('',
        url(r'^hello/$', hello), )
Without the dollar sign at the end it will match any url starting with hello like
hello/satish, hello/gandham/, hello/satish/123/pqr """
