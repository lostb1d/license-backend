from django.urls import path
from .views import signup_view, CustomLoginView, profile_view, index_view

urlpatterns = [
    path('home/', index_view, name='index-view'),
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
]
