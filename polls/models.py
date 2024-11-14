from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    skills = models.ManyToManyField('Skill', related_name='users_with_skill')
    search_slots = models.ManyToManyField('Slot', related_name='searching_users')
    help_slots = models.ManyToManyField('Slot', related_name='helping_users')

    def __str__(self):
        return f"{self.first_name} {self.name}"


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Slot(models.Model):
    date = models.DateTimeField()
    description = models.TextField()
    required_competence = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='required_for_slots')
    user_requesting_help = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requested_help_slots', null=True, blank=True)
    user_offering_help = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offered_help_slots', null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.description}"


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def display_skills(self):
        return Skill.objects.all()

    def display_slots(self):
        return Slot.objects.all()

    def clean(self):
        if self.user_requesting_help is None and self.user_offering_help is None:
            raise ValidationError(
                'Un créneau doit avoir soit un utilisateur demandant de l\'aide, soit un utilisateur offrant de l\'aide.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)