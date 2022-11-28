from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "eat no meat for the entire month",
    "february": "walk for at least 20 minutes everyday",
    "match": "learn django for at least 20 minutes everyday",
    "april": "eat no meat for the entire month",
    "may": "walk for at least 20 minutes everyday",
    "june": "learn django for at least 20 minutes everyday",
    "july": "eat no meat for the entire month",
    "august": "walk for at least 20 minutes everyday",
    "september": "learn django for at least 20 minutes everyday",
    "october": "eat no meat for the entire month",
    "november": "walk for at least 20 minutes everyday",
    "december": "diet for the entire month"
}
# Create your views here.

# def jan(request):
#     return HttpResponse("eat no meat for the entire month")

# def feb(request):
#     return HttpResponse("walk for at least 20 minutes everyday")

def index(request):
    l_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capital = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        l_items += f"<li><a href=\"{month_path}\">{capital}</a></li>"
        
    response_data = f"<ul>{l_items}</ul>"
    return HttpResponse(response_data)

def monthly_challengeN(request, month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("ERROR")
    fd_month = months[month-1]
    redirect_url = reverse("month-challenge", args=[fd_month])
    return HttpResponseRedirect(redirect_url)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })        
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Error</h1>")
    