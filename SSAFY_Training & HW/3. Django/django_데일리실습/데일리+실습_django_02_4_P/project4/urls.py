from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("chatting/", include("chatting.urls")),
    path("information/", include("information.urls")),
    path("admin/", admin.site.urls),
]
