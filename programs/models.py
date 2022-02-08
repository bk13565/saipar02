from django.db import models

# Create your models here.
class SocialPoliticalChangeModel(models.Model):
    project = models.CharField(max_length=100)
    subject = models.TextField()
    link = models.CharField(max_length=300)
    upload_link = models.FileField(upload_to="programs/social_political_change", blank=True)
    
    def __str__(self):
        return f" {self.project} "