from django.urls import path, include
from .views import Postdetail, Postslist

urlpatterns = [
    # home page
    path('', Postslist.as_view(), name='posts'),
    # route for posts
    path('<slug:slug>/', Postdetail.as_view(), name='post_detail'),
]