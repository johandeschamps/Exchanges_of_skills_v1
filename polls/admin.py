# polls/admin.py
from django.contrib import admin
from .models import User, Skill, Slot

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'name', 'email_address')
    search_fields = ('first_name', 'name', 'email_address')
    filter_horizontal = ('skills',)  # Affiche les compétences dans un widget horizontal
    exclude = ('search_slots', 'help_slots')  # Exclut les champs de créneaux

admin.site.register(User, UserAdmin)
admin.site.register(Skill)
admin.site.register(Slot)