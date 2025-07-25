
import datetime 
from django.http import HttpResponse 
from .models import Question
from django.template import loader 
from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice , Question 
from django.db.models import F 
from django.views import generic 
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    print("Question:", question)
    print("Choices:", list(question.choice_set.all()))
    return render(request, "polls/detail.html", {"question": question}) 

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print("Question:", question)
    print("Request POST data:", request.POST)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        print("Selected choice:", selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(f"/polls/{question.id}/results/")