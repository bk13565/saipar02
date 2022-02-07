from django.db import models

# Create your models here.
        
class OccasionalPaperModel(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    paper_link = models.FileField(upload_to="pubs/occassional_papers", blank=True)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f" {self.title} {self.paper_link} "
    
    def file_url(self):
        if self.paper and hasattr(self.paper, 'url'):
            return self.paper.url
    
class DiscussionPapersModel(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    paper_link = models.FileField(upload_to="pubs/discussion_papers", blank=True)
    
    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f" {self.title} {self.paper_link} "
    
    def file_url(self):
        if self.paper and hasattr(self.paper, 'url'):
            return self.paper.url

    
class ReportsModel(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    paper_link = models.FileField(upload_to="pubs/reports_and_policy_briefs", blank=True)
    
    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f" {self.title} {self.paper_link} "
    
    def file_url(self):
        if self.paper and hasattr(self.paper, 'url'):
            return self.paper.url
    
    
class ZSSJModel(models.Model):
    pub_date = models.DateField()
    vol = models.IntegerField()
    num = models.IntegerField()
    link = models.FileField(upload_to="pubs/zssj", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f" {self.vol} {self.num} "
    
BOOK_TYPE = (
    (0,"eBook"),
    (1,"eArticle"),
    (2,"print")
    )

class SAIPARBookshelfModel(models.Model):
    book_type = models.IntegerField(choices=BOOK_TYPE, blank=True)
    downloadable = models.BooleanField(default=False)
    link = models.FileField(upload_to="pubs/SAIPAR_bookshelf", blank=True)
    price = models.IntegerField(blank=True)
    title = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" {self.title} "
    
    # not neccessary
    def file_url(self):
        if self.paper and hasattr(self.paper, 'url'):
            return self.paper.url
    
    
    