from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from accounts.models import Course
from django.conf import settings
from django.contrib.auth.models import User
# if i want to add user model in other model 

# from django.conf import settings
# from django.db import models

# class ExampleModel(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # other fields

# Create your models here.


class chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    chapterCode = models.CharField(max_length=30)
    chapterName = models.CharField(max_length=200)

    def __str__(self):
        return self.chapterName
    
class correctOption(models.Model):
    correctOpt = models.CharField(max_length=1)

    def __str__(self):
        return self.correctOpt

class weightage(models.Model):
    mark = models.IntegerField()

    def __str__(self):
        return str(self.mark)
        
class geomaticsQuestions(models.Model):
    chapter = models.ForeignKey(chapter, on_delete=models.CASCADE)
    question = QuillField()
    option1 = QuillField()
    option2 = QuillField()
    option3 = QuillField()
    option4 = QuillField()
    correctOpt = models.ForeignKey(correctOption, on_delete=models.CASCADE)
    explanation = QuillField()
    weight = models.ForeignKey(weightage, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    def __str__(self):
        return self.question.html
