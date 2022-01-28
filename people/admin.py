from django.contrib import admin

# Register your models here.
from .models import Staff, ResearchStaff

# admin.site.register(Hero)
admin.site.register(Staff)
admin.site.register(ResearchStaff)