from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    """
    Modèle représentant un utilisateur.

    Attributs:
        name (CharField): Nom de l'utilisateur.
        first_name (CharField): Prénom de l'utilisateur.
        email_address (EmailField): Adresse email unique de l'utilisateur.
        skills (ManyToManyField): Compétences de l'utilisateur.
        search_slots (ManyToManyField): Créneaux de recherche de l'utilisateur.
        help_slots (ManyToManyField): Créneaux d'aide de l'utilisateur.
    """
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    skills = models.ManyToManyField('Skill', related_name='users_with_skill')
    search_slots = models.ManyToManyField('Slot', related_name='searching_users')
    help_slots = models.ManyToManyField('Slot', related_name='helping_users')

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de l'utilisateur.
        """
        return f"{self.first_name} {self.name}"


class Skill(models.Model):
    """
    Modèle représentant une compétence.

    Attributs:
        name (CharField): Nom de la compétence.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de la compétence.
        """
        return self.name


class Slot(models.Model):
    """
    Modèle représentant un créneau horaire.

    Attributs:
        date (DateTimeField): Date et heure du créneau.
        description (TextField): Description du créneau.
        required_competence (ForeignKey): Compétence requise pour le créneau.
        user_requesting_help (ForeignKey): Utilisateur demandant de l'aide.
        user_offering_help (ForeignKey): Utilisateur offrant de l'aide.
    """
    date = models.DateTimeField()
    description = models.TextField()
    required_competence = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='required_for_slots')
    user_requesting_help = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requested_help_slots', null=True, blank=True)
    user_offering_help = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offered_help_slots', null=True, blank=True)

    def clean(self):
        """
        Valide que le créneau a soit un utilisateur demandant de l'aide, soit un utilisateur offrant de l'aide.
        Lève une ValidationError si ce n'est pas le cas.
        """
        if self.user_requesting_help is None and self.user_offering_help is None:
            raise ValidationError


    def save(self, *args, **kwargs):
        """
        Sauvegarde le créneau après validation.
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du créneau.
        """
        return f"{self.date} - {self.description}"


class Visitor(models.Model):
    """
    Modèle représentant un visiteur.

    Attributs:
        user (OneToOneField): Utilisateur associé au visiteur.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def display_skills(self):
        """
        Affiche toutes les compétences disponibles.

        Retourne:
            QuerySet: Ensemble des compétences.
        """
        return Skill.objects.all()

    def display_slots(self):
        """
        Affiche tous les créneaux disponibles.

        Retourne:
            QuerySet: Ensemble des créneaux.
        """
        return Slot.objects.all()