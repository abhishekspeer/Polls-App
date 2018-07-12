# Imports
from django.shortcuts import render
from django.http import HttpResponse

# Views: logic, requires mapping with a URL to call, and hence URL config
def index(request):
    # View that generates a simple Http Response
    return HttpResponse("Welcome to the Polls Index")
