from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at the results of question %s." %question)

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)

