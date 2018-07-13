# Imports
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Views: logic, requires mapping with a URL to call, and hence URL config
def index(request):
    # View that generates a simple Http Response
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # used earlier: output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    # used earlier: return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Question Number {}".format(question_id))

def results(request, question_id):
    return HttpResponse("Results of Question Number {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("Voting on Question Number {}".format(question_id))
