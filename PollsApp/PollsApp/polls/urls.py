# Notes
## NOTE: manually created, so that we can first map all the urls of the app here.
## NOTE: we'll link it to the project's url.py to map all the urls of the app to the project.

# Imports
from django.conf.urls import url
from . import views # imports views defined inside polls/views.py


# URLpatterns: mapping of views to URLs
app_name = 'polls' # Namespacing
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



# References
"""
# NOTE: referencing from the official documnetation:

The way this works is by looking up the URL definition as specified in the
polls.urls module. You can see exactly where the URL name of ‘detail’ is
defined below:
    ...
    # the 'name' value as called by the {% url %} template tag
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    ...

If you want to change the URL of the polls detail view to something else,
perhaps to something like polls/specifics/12/ instead of doing it in the template
(or templates) you would change it in polls/urls.py:
    ...
    # added the word 'specifics'
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

"""












# Pre-Requisites
""" $ and ^ are regular expression characters that have a special meaning:
the caret means “require that the pattern matches the start of the string,” and the dollar sign means “require that the pattern matches the end of the string.”
For example consider the  following url pattern:
    urlpatterns = patterns('',
        url(r'^hello/$', hello), )
Without the dollar sign at the end it will match any url starting with hello like
hello/satish, hello/gandham/, hello/satish/123/pqr """
