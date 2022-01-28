from django.shortcuts import render
from django.views import generic
from .models import SocialPoliticalChangeModel

# Create your views here.

class EducationProgramView(generic.TemplateView):
    template_name = "programs/education_programs.html"
    
class LawProgramView(generic.TemplateView):
    template_name = "programs/law_programs.html"
    
class LawEditorialBoardView(generic.TemplateView):
    template_name = "programs/editorial_board.html"
    
class EconomicProgramView(generic.TemplateView):
    template_name = "programs/economic_programs.html"
    
class SocialPoliticalChangeView(generic.ListView):
    template_name = "programs/social_political_change.html"
    context_object_name = "projects"
    
    def get_queryset(self):
        queryset = SocialPoliticalChangeModel.objects.all()
        return queryset