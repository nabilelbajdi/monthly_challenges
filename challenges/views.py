from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "January",
    "february": "February",
    "march": "March",
    "april": "April",
    "may": "May",
    "june": "June",
    "july": "July",
    "august": "August",
    "september": "September",
    "october": "October",
    "november": "November",
    "december": "December"

}


# Create your views here.


def monthly_challenge_by_number(requests, month):
    months = list(monthly_challenges.keys())

    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(requests, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

# So, when you type /challenges/january, Django:
# - Routes to challenges.urls to interpret the january part as month.
# - Calls monthly_challenge with month="january".
# - The view then finds the relevant message for "january" and displays it.
