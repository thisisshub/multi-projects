from django.urls import path
from .views import resumeinput, resumeoutput

urlpatterns = [
    path("", resumeinput, name="resumemaker_resumeinput"),
    path("generate/", resumeoutput, name="resumemaker_resumeoutput")
]