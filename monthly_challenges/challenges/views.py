from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

#Dictionary
monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "Eat no meat for entire month",
    "march": "Eat no meat for entire month",
    "april": "Eat no meat for entire month",
    "may": "Eat no meat for entire may",
    "june": "Eat no meat for entire month",
    "july": "Birthday month!",
    "august": "Eat no meat for entire month",
    "september": "Eat no meat for entire month",
    "october": "Eat no meat for entire October",
    "november": "Eat no meat for entire month",
    "december": "Eat no meat for entire month"

}

# Create your views here.
def home(request):
    return HttpResponse("Hello, King Chuck!")

#def index(request):
 #   return HttpResponse("Hello, Chuck")

#def february(request):
    #return HttpResponse("Hello, February")


def number_month(request,month):
    return HttpResponse(month)


def monthly_challenge(reqeust,month):
    
    try: 
        #test = monthly_challenges[month]
        month_text = monthly_challenges[month]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
  