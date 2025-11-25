from django.urls import path

from . import views

app_name = "planner"

urlpatterns = [
    # http://127.0.0.1:8000/meal/
    path("", views.index, name="index"),
    path("/meal/<str:week_day>", views.meal, name="meal"),
    path("/meal/delete/<int:meal_id>", views.delete_meal, name="delete_meal"),  
    path("/meal/edit/<int:meal_id>", views.edit_meal, name="edit_meal"),  
    path("/meal/add/", views.add_meal, name="add_meal"),  
     
]