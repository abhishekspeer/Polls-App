# Notes
## NOTE: manually created, so that we can first map all the urls of the app here.
## NOTE: we'll link it to the project's url.py to map all the urls of the app to the project.

# Imports
from django.conf.urls import url
from . import views # imports views defined inside polls/views.py


# URLpatterns: mapping of views to URLs
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
















# Pre-Requisites
""" $ and ^ are regular expression characters that have a special meaning:
the caret means “require that the pattern matches the start of the string,” and the dollar sign means “require that the pattern matches the end of the string.”
For example consider the  following url pattern:
    urlpatterns = patterns('',
        url(r'^hello/$', hello), )
Without the dollar sign at the end it will match any url starting with hello like
hello/satish, hello/gandham/, hello/satish/123/pqr """
