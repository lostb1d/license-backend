from django.contrib import admin
from django.urls import path
from civil.views import *

urlpatterns = [
    path('random-questions/', RandomQuestionsAPIView.as_view(), name='random-questions'),
    path('<str:chapter_code>', RandomQuestionsByChapterCodeView.as_view(), name='chapter-wise-question'),     
    
]
