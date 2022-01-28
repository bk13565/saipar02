from django.shortcuts import render
from django.views import generic
from .models import EventModel, ProjectModel, OpeningModel
import datetime

# Create your views here.
class EventListView(generic.ListView):
    template_name = "resources/event_project_list.html"
    # model = EventModel
    context_object_name = "events"

    def get_queryset(self):
        queryset = EventModel.objects.filter(date__gte=datetime.datetime.now().date())        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        queryset = EventModel.objects.filter(date__lt= datetime.datetime.now().date())
        # project_queryset = ProjectModel.objects.filter(date__gte=datetime.datetime.now().date())
        #added the project queryset in here because it's the same template
        project_queryset = ProjectModel.objects.all()
        openings_queryset = OpeningModel.objects.all()

        context.update({
                "past_events": queryset,
                "current_projects" : project_queryset,
                "current_openings" : openings_queryset,
            })
        return context  
    
    
class HomepageView(generic.TemplateView):
    template_name = "homepage.html"
    
class AboutUsView(generic.TemplateView):
    template_name = "aboutus.html"
    
class ZLIIView(generic.TemplateView):
    template_name = "zlii.html"