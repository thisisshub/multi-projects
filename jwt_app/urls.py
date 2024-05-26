from . import views 
from django.urls import path 
  
urlpatterns = [ 
    path('hello/', views.HelloView.as_view(), name ='hello'), 
] 