# Imports
from django.shortcuts import render, get_object_or_404 #get_object_or_404 not used
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
# Views: logic, requires mapping with a URL to call, and hence URL config
def index(request):
    # View that generates a simple Http Response
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # used earlier #1: output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    # used earlier #1: return HttpResponse(output)
    return HttpResponse(template.render(context, request))
"""
    # The Same index function using render() A shortcut
    # The render() function takes the request object as its first argument,a template
    name as its second argument and a dictionary as its optional third argument.
    It returns an HttpResponse object of the given template rendered with the given
    context.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

"""

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # The view raises the Http404 exception if a question with the requested ID doesn’t exist.
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
"""
    get_object_or_404() shortcut:
    instead of using try & except, we can use s standard get_object_or_404() to get the same.

    from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# WARNING: Need to import that from django.shortcuts module first!!!
"""

# NOTE: Used Earlier #1
"""
def detail(request, question_id):
    return HttpResponse("Question Number {}".format(question_id))
"""



def results(request, question_id):
    # Used earlier: return HttpResponse("Results of Question Number {}".format(question_id))
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

    # used earlier:  return HttpResponse("Voting on Question Number {}".format(question_id))
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # NOTE:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
