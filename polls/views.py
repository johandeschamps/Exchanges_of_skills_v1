from django.shortcuts import render, get_object_or_404
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

def skill_slots(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    slots = Slot.objects.filter(required_competence=skill)
    return render(request, 'polls/skill_slots.html', {'skill': skill, 'slots': slots})