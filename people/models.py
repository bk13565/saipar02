from django.db import models
# from PIL import Image
from PIL import Image

# Create your models here.
# class Hero(models.Model):
# 	name = models.CharField(max_length=60)
# 	alias = models.CharField(max_length=60)

# 	def __str__(self):
# 		return self.name

RESEARCH_STATUS = (
    (0, "None"),
    (1, "Research Staff"),
    (2, "Research Affiliate"),
    (3, "SAIPAR Fellow"),
    (4, "Robert Kent Fellow"),
    (5, "Intern"),
)

COMMITTEE = (
    (1, "Executive"),
    (2, "Audit"),
)
	
class Staff(models.Model):
    name = models.CharField(max_length=60)
    affiliation = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to='images/people', blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    institution = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    director = models.BooleanField(default=False, null=True)
    committee = models.IntegerField(choices=COMMITTEE, blank=True, null=True)
    International_Advisory_Board = models.BooleanField(default=False, null=True) #international advisory board member
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return f" {self.name} "
    
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class ResearchStaff(Staff):
    research_status = models.IntegerField(choices=RESEARCH_STATUS, default=0)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return f" {self.name} {self.research_status} "
    
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url




