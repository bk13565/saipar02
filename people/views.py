from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import StaffSerializer, ResearchSerializer
from .models import COMMITTEE, Staff, ResearchStaff
from django.views import generic


# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('name')
    serializer_class = StaffSerializer

class ResearchViewSet(viewsets.ModelViewSet):
    queryset = ResearchStaff.objects.all().order_by('name')
    serializer_class = ResearchSerializer
    
# contexts: staff, directors - audit/executive, IAB, research
class PeopleView(generic.ListView):
    template_name = "people/people.html"
    context_object_name = "staff"
    
    def get_queryset(self):
        queryset = Staff.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(PeopleView, self).get_context_data(**kwargs)
        #research staff members
        research = ResearchStaff.objects.all()
        research_staff = research.filter(research_status=1)
        research_affiliates = research.filter(research_status=2)
        saipar_fellows = research.filter(research_status=3)
        kent_fellows = research.filter(research_status=4)
        interns = research.filter(research_status=5)
        #IAB
        iab_staff = Staff.objects.filter(International_Advisory_Board=True).order_by('name')
        #directors
        directors = Staff.objects.filter(director=True)
        #committee members
        executive_committee = Staff.objects.filter(committee=1)
        audit_committee = Staff.objects.filter(committee=2)
        #staff
        staff = Staff.objects.filter(affiliation="SAIPAR")
        
        context.update({
            "iab_staff": iab_staff,
            "directors" : directors,
            "executive_committee" : executive_committee,
            "audit_committee" : audit_committee,
            "staff" : staff,
        })
        
        return context
        
# contexts: staff, directors - audit/executive, IAB, research
class ResearchPeopleView(generic.ListView):
    template_name = "people/research_people.html"
    context_object_name = "research"
    
    def get_queryset(self):
        queryset = ResearchStaff.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ResearchPeopleView, self).get_context_data(**kwargs)
        #research staff members
        research = ResearchStaff.objects.all()
        research_staff = research.filter(research_status=1)
        research_affiliates = research.filter(research_status=2)
        saipar_fellows = research.filter(research_status=3)
        kent_fellows = research.filter(research_status=4)
        interns = research.filter(research_status=5)
                
        context.update({
            "research_staff" : research_staff,
            "research_affiliates" : research_affiliates,
            "saipar_fellows" : saipar_fellows,
            "kent_fellows" : kent_fellows,
            "interns" : interns,
        })
        
        return context
        