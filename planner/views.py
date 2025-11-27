from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .data import MEALS
# Create your views here.

def index(request):
    return render(request, "planner/index.html")


def meal(request, week_day, meal_id=None):

     
     context = {
        'day': week_day,
     
        'meals': MEALS,
        'meal': {"id": meal_id}
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

def edit_meal(request, meal_id):
    global MEALS
    meal_to_edit = next((m for m in MEALS if m['id'] == meal_id), None)

    if request.POST:
        week_day = request.POST.get("week_day", meal_to_edit['week_day'])

        # Update fields from POST
        meal_to_edit['name'] = request.POST.get("name", meal_to_edit['name'])
        meal_to_edit['week_day'] = week_day
        meal_to_edit['type'] = request.POST.get("type", meal_to_edit['type'])
        meal_to_edit['taste'] = request.POST.get("taste", meal_to_edit['taste'])
        meal_to_edit['servings'] = request.POST.get("servings", meal_to_edit['servings'])
        meal_to_edit['notes'] = request.POST.get("notes", meal_to_edit['notes'])

        # (OPTIONAL) Prevent week_day editing — but if you want it editable,
        # uncomment the line below:
        # meal_to_edit['week_day'] = request.POST.get("week_day", meal_to_edit['week_day'])

        return redirect('planner:meal', week_day=week_day)
    

    if meal_to_edit:
        context = {
            'id': meal_to_edit['id'],
            'name': meal_to_edit['name'],
            'week_day': meal_to_edit['week_day'],
            'type': meal_to_edit['type'],
            'taste': meal_to_edit['taste'],
            'servings': meal_to_edit['servings'],
            'notes': meal_to_edit['notes'],
        }

        return render(request, "planner/edit.html", {'meal': context})
    
    return redirect('planner:meal', week_day='monday')

def edit2_meal(request, meal_id):
    global MEALS

    meal_to_edit = next((m for m in MEALS if m['id'] == meal_id), None)

    if meal_to_edit:
        # Keep original week_day for redirect
        week_day = meal_to_edit['week_day']

        # Update fields from POST
        meal_to_edit['name'] = request.POST.get("name", meal_to_edit['name'])
        meal_to_edit['type'] = request.POST.get("meal_type", meal_to_edit['meal_type'])
        meal_to_edit['taste'] = request.POST.get("taste", meal_to_edit['taste'])
        meal_to_edit['servings'] = request.POST.get("servings", meal_to_edit['servings'])
        meal_to_edit['notes'] = request.POST.get("notes", meal_to_edit['notes'])

        # (OPTIONAL) Prevent week_day editing — but if you want it editable,
        # uncomment the line below:
        # meal_to_edit['week_day'] = request.POST.get("week_day", meal_to_edit['week_day'])

        return redirect('planner:meal', week_day=week_day)

    return redirect('planner:meal', week_day='monday')

def add_meal(request):
    global MEALS

    name = request.POST["name"]
    week_day = request.POST["week_day"]
    meal_type = request.POST["meal_type"]
    taste = request.POST["taste"]
    servings = request.POST["servings"]
    notes = request.POST["notes"]

    # Auto-generate ID
    new_id = max([m["id"] for m in MEALS], default=0) + 1

    new_meal = {
        "id": new_id,
        "name": name,
        "week_day": week_day.lower(),
        "type": meal_type,
        "taste": taste,
        "servings": servings,
        "notes": notes,
    }

    MEALS.append(new_meal)

    print(f"Added meal: {new_meal}")

    return redirect("planner:meal", week_day=week_day)