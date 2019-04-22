from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup
import requests
import json
# Create your views here.


def index(request):
    return HttpResponse("Success")

def showQuestions(request):
    questions = Question.objects.all()
    return render(request,'stackapi/home.html',{'questions':questions})


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def latest(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")

        soup = BeautifulSoup(res.text, "html.parser")
        txt = ""
        tag = []
        questions = soup.select(".question-summary")
        Question.objects.all().delete()
        for que in questions:
            q = que.select_one('.question-hyperlink').getText()
            vote_count = que.select_one('.vote-count-post').getText()
            views = que.select_one('.views').attrs['title']
            tags = [i.getText() for i in (que.select('.post-tag'))]
            tag = que.select_one('.question-hyperlink').attrs['href']
            hlink = tag

            question = Question()
            question.question = q
            question.vote_count = vote_count
            question.views = views
            question.tags = tags
            question.hlink = hlink
            question.save()

        

        qs = Question.objects.all().order_by('views')
        return render(request,'stackapi/home.html',{'qs':qs})
    except e as Exception:
        return HttpResponse("Failed {e}")
