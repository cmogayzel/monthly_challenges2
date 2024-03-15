from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


#Dictionary
monthly_challenges = {
    "january": "Eat no meat for entire month new year",
    "february": "Eat no meat for entire month February",
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

# Redirecting based on interger being entered in the address bar.
def number_month(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid")
    else:
        forward_month = months[month - 1] # subtract one dictonary key because it starts at index 0 in the dictionary.
        redirect_path = reverse("month-challenge",args=[forward_month]) #Reverse function for URLs
        #return HttpResponseRedirect("/challenges/"+ forward_month)
        return HttpResponseRedirect(redirect_path)


def monthly_challenge(reqeust,month):
    
    try: 
        #test = monthly_challenges[month]
        month_text = monthly_challenges[month]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
  