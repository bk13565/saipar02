from django.contrib import admin
from .models import ProjectModel, EventModel, OpeningModel

# current/upcoming events, past events, openings

class EventModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'link')
    

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'link')

class OpeningModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'link',)

admin.site.register(EventModel, EventModelAdmin)
admin.site.register(ProjectModel, ProjectModelAdmin)
admin.site.register(OpeningModel, OpeningModelAdmin)