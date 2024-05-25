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
        chapters = geomaticsQuestions.objects.values_list('chapter', flat=True).distinct()
        if len(chapters) <10:
            return Response({"error":"Not enough chapters available"}, status= status.HTTP_400_BAD_REQUEST)
        random_chapters = random.sample(list(chapters),10)

        weightage_1_records = []
        weightage_2_records = []

        
        for chapter in random_chapters:
            chapter_records_weightage_1 = geomaticsQuestions.objects.filter(chapter=chapter, weight=1)
            chapter_records_weightage_2 = geomaticsQuestions.objects.filter(chapter=chapter, weight=2)

            if chapter_records_weightage_1.exists():
                weightage_1_records.extend(random.sample(list(chapter_records_weightage_1),min(len(chapter_records_weightage_1),6)))

            if chapter_records_weightage_2.exists():
                weightage_2_records.extend(random.sample(list(chapter_records_weightage_2),min(len(chapter_records_weightage_2),2)))
        
        all_records = weightage_1_records + weightage_2_records

        serializer = questionSerializers(all_records, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
        filtered_questions = geomaticsQuestions.objects.filter(chapter=chapter_obj)
        
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
    