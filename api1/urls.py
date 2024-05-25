from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('geomatics/', include("api1.geo-urls")),
    path('civil/', include("api1.civil-urls")),
    path('accounts/', include("api1.account-urls")),
]
