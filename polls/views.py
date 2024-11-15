from django.shortcuts import render, get_object_or_404
from .models import Skill, Slot, Visitor

def index(request):
    """
    Vue pour la page d'accueil.

    Récupère toutes les compétences et les passe au template 'polls/index.html'.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'polls/index.html' et les compétences.
    """
    skills = Skill.objects.all()
    return render(request, 'polls/index.html', {'skills': skills})

def display_skills(request):
    """
    Vue pour afficher toutes les compétences.

    Récupère toutes les compétences et les passe au template 'polls/skills.html'.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'polls/skills.html' et les compétences.
    """
    skills = Skill.objects.all()
    return render(request, 'polls/skills.html', {'skills': skills})

def display_slots(request):
    """
    Vue pour afficher tous les créneaux.

    Récupère tous les créneaux et les passe au template 'polls/slots.html'.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'polls/slots.html' et les créneaux.
    """
    slots = Slot.objects.all()
    return render(request, 'polls/slots.html', {'slots': slots})

def skill_slots(request, skill_id):
    """
    Vue pour afficher les créneaux associés à une compétence spécifique.

    Récupère la compétence spécifiée par son ID et les créneaux qui requièrent cette compétence,
    puis les passe au template 'polls/skill_slots.html'.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.
        skill_id (int): L'ID de la compétence.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'polls/skill_slots.html', la compétence et les créneaux associés.
    """
    skill = get_object_or_404(Skill, id=skill_id)
    slots = Slot.objects.filter(required_competence=skill)
    return render(request, 'polls/skill_slots.html', {'skill': skill, 'slots': slots})