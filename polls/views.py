from django.shortcuts import render
from .models import Skill, Slot, Visitor

def index(request):
    skills = Skill.objects.all()
    return render(request, 'polls/index.html', {'skills': skills})

def display_skills(request):
    skills = Skill.objects.all()
    return render(request, 'polls/skills.html', {'skills': skills})

def display_slots(request):
    slots = Slot.objects.all()
    return render(request, 'polls/slots.html', {'slots': slots})