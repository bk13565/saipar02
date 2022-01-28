from django.contrib import admin
from django.db.models.query import QuerySet
from .models import NewsletterSubscriber, Newsletter

def send_saipar_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)
        
send_saipar_newsletter.short_description = "Send Newsletter To Subscribers"

class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on', 'confirmed')
    
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'subject', )
    actions = [send_saipar_newsletter]

admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
