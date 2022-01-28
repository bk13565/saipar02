from django.contrib import admin

# Register your models here.
from .models import OcasionalPaperModel, DiscussionPapersModel, ReportsModel, ZSSJModel, SAIPARBookshelfModel

class OccassionalPapersModelAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'paper_link', 'created_on', 'updated_on')
    
class DiscussionPapersModelAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'paper_link', 'created_on', 'updated_on')
    
class ReportsModelAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'paper_link', 'created_on', 'updated_on')
    
class ZSSJModelAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'vol', 'num', 'link', 'created_on')
    
class SAIPARBookshelfModelAdmin(admin.ModelAdmin):
    list_display = ('book_type', 'downloadable', 'title', 'link', 'price', 'created_on')
    
admin.site.register(OcasionalPaperModel, OccassionalPapersModelAdmin)
admin.site.register(DiscussionPapersModel, DiscussionPapersModelAdmin)
admin.site.register(ReportsModel, ReportsModelAdmin)
admin.site.register(ZSSJModel, ZSSJModelAdmin)
admin.site.register(SAIPARBookshelfModel, SAIPARBookshelfModelAdmin)