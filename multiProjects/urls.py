from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("payment/", include("payment.urls")),
    path("resumemaker/", include("resumemaker.urls")),
]
