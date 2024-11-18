from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('slots/', views.display_slots, name='slots'),
    path('skills/<int:skill_id>/', views.skill_slots, name='skill_slots'),
]