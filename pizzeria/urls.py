from django.contrib import admin
from django.urls import path, include
from api import urls as appurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include(appurls)),

]