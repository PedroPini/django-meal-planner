from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .data import MEALS
from .models import Meal

# Create your views here.

def index(request):
    return render(request, "planner/index.html")


def meal(request, week_day, meal_id=None):
     meal = Meal.objects.order_by("type")
    
     context = {
        'day': week_day,
        'meals': meal,
        'meal': {"id": meal_id}
        }
     return render(request, "planner/index.html", context)


def delete_meal(request, meal_id):
    meal_to_delete = Meal.objects.get(id=meal_id)
    if meal_to_delete:
        week_day = meal_to_delete.week_day  # save week_day
        # Remove the meal from the list
        meal_to_delete.delete()
        # Redirect back to the same day
        return redirect('planner:meal', week_day=week_day)
    # If meal not found, just redirect to some default
    return redirect('planner:meal', week_day='monday')

def edit_meal(request, meal_id):
    meal_to_edit = Meal.objects.get(id=meal_id)
    print(f"MEAL PROPERTIES {meal_to_edit}")
    if request.POST:
        week_day = request.POST.get("week_day", meal_to_edit.week_day)

        # Update fields from POST
        meal_to_edit.name = request.POST.get("name", meal_to_edit.name)
        meal_to_edit.week_day = week_day
        meal_to_edit.type = request.POST.get("type", meal_to_edit.type)
        meal_to_edit.taste = request.POST.get("taste", meal_to_edit.taste)
        meal_to_edit.servings = request.POST.get("servings", meal_to_edit.servings)
        meal_to_edit.notes = request.POST.get("notes", meal_to_edit.notes)

        meal_to_edit.save()
        return redirect('planner:meal', week_day=week_day)
    

    if meal_to_edit:
        context = {
            'id': meal_to_edit.id,
            'name': meal_to_edit.name,
            'week_day': meal_to_edit.week_day,
            'type': meal_to_edit.type,
            'taste': meal_to_edit.taste,
            'servings': meal_to_edit.servings,
            'notes': meal_to_edit.notes,
        }

        return render(request, "planner/edit.html", {'meal': context})
    
    return redirect('planner:meal', week_day='monday')

def add_meal(request):

    name = request.POST["name"]
    week_day = request.POST["week_day"]
    meal_type = request.POST["meal_type"]
    taste = request.POST["taste"]
    servings = request.POST["servings"]
    notes = request.POST["notes"]

    new_meal = {
        "name": name,
        "week_day": week_day.lower(),
        "type": meal_type,
        "taste": taste,
        "servings": servings,
        "notes": notes,
    }

    Meal.objects.create(**new_meal)

    print(f"Added meal: {new_meal}")

    return redirect("planner:meal", week_day=week_day)