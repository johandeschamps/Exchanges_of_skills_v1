# polls/admin.py

from django.contrib import admin
from .models import User, Skill, Slot

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Slot)