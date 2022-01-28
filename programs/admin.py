from django.contrib import admin
from .models import SocialPoliticalChangeModel
# Register your models here.

class SocialPoliticalChangeModelAdmin(admin.ModelAdmin):
    list_display = ("project", "subject" ,"link")


admin.site.register(SocialPoliticalChangeModel, SocialPoliticalChangeModelAdmin)
