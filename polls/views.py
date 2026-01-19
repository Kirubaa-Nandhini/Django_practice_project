from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question
from django.db.models import F
from  django.urls import reverse
from django.template import loader
from django.views import generic

def index(request):
     latest_questions=Question.objects.order_by("-pub_date")[:5]
     template=loader.get_template("polls/index.html")
     context={"latest_question_list": latest_questions}
     return HttpResponse(template.render(context,request))
     
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
         raise Http404("Question not found")
    return render(request,"polls/detail.html",{"question":question})


def results(request,question_id):
        question=get_object_or_404(Question,pk=question_id)
        return render(request,"polls/results.html",{"question":question})

def votes(request,question_id):
     question=get_object_or_404(Question,pk=question_id)
     try:
          selected_choice=question.choice_set.get(pk=request.POST["choice"])
     except(keyError,choice.DoesNotExist):
          return render(request,
                        "polls/detail.html",
                      {
               "question":question_text,
               "error_message":"please select a choice"
          }
          )
     else:
         selected_choice.votes=F("votes")+1
         selected_choice.save()
         return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))