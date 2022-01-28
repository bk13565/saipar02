from .views import EconomicProgramView, EducationProgramView, LawProgramView, \
                    LawEditorialBoardView, EducationProgramView, SocialPoliticalChangeView
from django.urls import path, include


app_name = "programs"

urlpatterns = [
    path("education/", EducationProgramView.as_view(), name="education"),
    path("law/", LawProgramView.as_view(), name="law"),
    path("law/editorial-board/", LawEditorialBoardView.as_view(), name="law-editorial"),
    path("economics/", EconomicProgramView.as_view(), name="economics"),
    path("social-political-change/", SocialPoliticalChangeView.as_view(), name="social-politial"),
]
