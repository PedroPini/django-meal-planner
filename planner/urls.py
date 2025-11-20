from django.urls import path

from . import views

app_name = "planner"

urlpatterns = [
    # http://127.0.0.1:8000/meal/
    path("", views.index, name="index"), 
]