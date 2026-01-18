from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def detail(request,q_id):
    try:
        question=Question.objects.get(pk=q_id)
    except Question.DoesNotExist:
         raise Http404("Question not found")
    return render(request,"polls/detail.html",{"question":question})


def results(request,q_id):
        response="you are looking the results of %s"
        return HttpResponse(response %q_id)
def index(request):
     latest_questions=Question.objects.order_by("-pub_date")[:5]
     template=loader.get_template("polls/index.html")
     context={"latest_question_list": latest_questions}
     return HttpResponse(template.render(context,request))