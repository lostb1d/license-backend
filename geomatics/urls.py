from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('random-questions/', RandomQuestionsAPIView.as_view(), name='random-questions'),

    path('questions/', questionList.as_view(), name='get-questions'),
    path('questions/<int:pk>', questionListRetrieveUpdateDestroy.as_view(), name='questions-crud'),

    path('correctOpt/', correctOptionList.as_view() , name='get-correct-option'),
    path('correctOpt/<int:pk>', correctOptionRetrieveUpdateDestroy.as_view() , name='correct-option-rud'),

    path('chapter/<str:chapter_code>', RandomQuestionsByChapterCodeView.as_view(), name='surveying'), 


    # path('surveying/', fosQuestionList.as_view() , name='get-fos-question'),
    # path('surveying/<int:pk>', fosQuestionRetrieveUpdateDestroy.as_view() , name='fos-rud'),

    #url for template
    path('geo/', index, name='index'),
    path('add-question/', addQuestion, name='add-question'),
    path('question/', viewQuestions, name='view-question'),

    path('question/<int:pk>/update/', updateQuestion, name='update-question'),
    path('question/<int:pk>/delete/', deleteQuestion, name='delete-question'),

]
