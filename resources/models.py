from django.db import models

# Create your models here.

class EventModel(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    link = models.URLField(max_length=300, blank=True)
    upload_link = models.FileField(upload_to="events&resources/events", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-date', '-time')
    
    def __str__(self):
        return f"{self.title} {self.date}"
    
    
class ProjectModel(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    link = models.URLField(max_length=300)
    upload_link = models.FileField(upload_to="events&resources/projects", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('date', 'title')
    
    def __str__(self):
        return f" {self.title} {self.subject}"
    
    
class OpeningModel(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=300)
    upload_link = models.FileField(upload_to="events&resources/openings", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" {self.title} "
    
    