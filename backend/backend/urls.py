from django.contrib import admin
from django.urls import path, include

from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register', CreateUserView.as_view(), name="createuser"),
    path("api/token/generate", TokenObtainPairView.as_view(), name="get_tokens"),
    path("api/token/get-access-token",
         TokenRefreshView.as_view(), name="get_access_token"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/todo/", include("todo.urls")),
    path("api/", include("api.urls"))
]
