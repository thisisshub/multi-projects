# importing models and libraries
from .models import Posts
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
 
# class based views for posts
class Postslist(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs_homepage.html'
    paginate_by = 4
 
# class based view for each post
class Postdetail(generic.DetailView):
    model = Posts
    template_name = "blogs_individual.html"