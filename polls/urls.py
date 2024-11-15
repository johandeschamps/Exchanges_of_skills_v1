from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('skills/', views.display_skills, name='skills'),
    path('slots/', views.display_slots, name='slots'),
]