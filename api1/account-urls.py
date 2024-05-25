from django.contrib import admin
from django.urls import path
from accounts.views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', UserDetailView.as_view(), name='user-detail'),
    path('current_user/', CurrentUserView.as_view(), name='current-user'),
]
