from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Awesome job guys! This is the index page of our polls applications')

def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" % question_id )

def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
