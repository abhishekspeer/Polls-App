# NOTE:Views - the logic or actual database-driven content

from django.views.generic.base import TemplateView
# IMPORTS TemplateView, a built in Django funciton, displays our template content.

class HomeView(TemplateView):
    # HomeView being the actual view and we use TemplateView to specify the use of our index.html file.
    template_name = 'index.html'
