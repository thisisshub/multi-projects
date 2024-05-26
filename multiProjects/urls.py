from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views 


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("jwt_app/", include("jwt_app.urls")),
    path("payment/", include("payment.urls")),
    path("resumemaker/", include("resumemaker.urls")),
    path("api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
