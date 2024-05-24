from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics
from rest_framework import permissions
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Random
from rest_framework.views import APIView
from .forms import *
import random

#random question api
class RandomQuestionsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        chapters = questions.objects.values_list('chapter', flat=True).distinct()
        if len(chapters) <10:
            return Response({"error":"Not enough chapters available"}, status= status.HTTP_400_BAD_REQUEST)
        random_chapters = random.sample(list(chapters),10)

        weightage_1_records = []
        weightage_2_records = []

        
        for chapter in random_chapters:
            chapter_records_weightage_1 = questions.objects.filter(chapter=chapter, weight=1)
            chapter_records_weightage_2 = questions.objects.filter(chapter=chapter, weight=2)

            if chapter_records_weightage_1.exists():
                weightage_1_records.extend(random.sample(list(chapter_records_weightage_1),min(len(chapter_records_weightage_1),6)))

            if chapter_records_weightage_2.exists():
                weightage_2_records.extend(random.sample(list(chapter_records_weightage_2),min(len(chapter_records_weightage_2),2)))
        
        # if len(weightage_1_records)>6:
        #     weightage_1_records = random.sample(weightage_1_records,6)

        
        # if len(weightage_1_records)>2:
        #     weightage_2_records = random.sample(weightage_2_records,2)

        all_records = weightage_1_records + weightage_2_records

        serializer = questionSerializers(all_records, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
        


#question list
class questionList(generics.ListCreateAPIView):
    queryset = questions.objects.all()
    serializer_class = questionSerializers

class questionListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = questions.objects.all()
    serializer_class = questionSerializers


#correct option
class correctOptionList(generics.ListCreateAPIView):
    queryset = correctOption.objects.all()
    serializer_class = correctOptionSerializers

class correctOptionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = correctOption.objects.all()
    serializer_class = correctOptionSerializers

#fundamental of surveying
class RandomQuestionsByChapterCodeView(generics.ListAPIView):
    serializer_class = questionSerializers

    def get_queryset(self):
        chapter_code = self.kwargs['chapter_code']
        try:
            # Get the chapter based on chapterCode
            chapter_obj = chapter.objects.get(chapterCode=chapter_code)
        except chapter.DoesNotExist:
            return []
        
        # Filter questions by the chapter
        filtered_questions = questions.objects.filter(chapter=chapter_obj)
        
        # If there are fewer than 20 questions, return them all
        if len(filtered_questions) <= 10:
            return filtered_questions
        
        # Otherwise, return a random sample of 20 questions
        return random.sample(list(filtered_questions), 10)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"error": "No questions found for the provided chapter code."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#for django template 

#adding questions
def index(request):
    return render(request, 'index.html')

def addQuestion(request):
    if request.method == 'POST':
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-question')
    else:
        form = questionForm()
    return render(request,'add-question.html',{'form':form})

def viewQuestions(request):
    question = questions.objects.all()

    return render(request, 'view-question.html',{'question':question})

def updateQuestion(request, pk):
    question = get_object_or_404(questions, pk=pk)
    if request.method == 'POST':
        form = questionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('view-question')
    else:
        form = questionForm(instance=question)
    return render(request, 'update-question.html',{'form': form})

def deleteQuestion(request, pk):
    question = get_object_or_404(questions, pk=pk)
    if request.method=='POST':
        question.delete()
        return redirect('view-question')
    return render(request, 'question-confirm-delete.html',{'question': question} )
