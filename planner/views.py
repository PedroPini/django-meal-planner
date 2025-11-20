from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .data import MEALS
# Create your views here.

def index(request):
    return render(request, "planner/index.html")


def meal(request, week_day):
     meal_types = {
        "1": "Breakfast",
        "2": "Lunch",
        "3": "Dinner",
        "4": "Snacks",
    }
     context = {
        'day': week_day,
        "meal_types": meal_types,
        'meals': MEALS
        }
     return render(request, "planner/index.html", context)


def delete_meal(request, meal_id):
    global MEALS
    # Find the meal first to get its week_day
    meal_to_delete = next((m for m in MEALS if m['id'] == meal_id), None)
    if meal_to_delete:
        week_day = meal_to_delete['week_day']  # save week_day
        # Remove the meal from the list
        MEALS = [m for m in MEALS if m['id'] != meal_id]
        # Redirect back to the same day
        return redirect('planner:meal', week_day=week_day)
    # If meal not found, just redirect to some default
    return redirect('planner:meal', week_day='monday')