from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    # Libs urls
    path("__reload__/", include("django_browser_reload.urls")),
]
