from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class courses(models.Model):
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.course

class chapter(models.Model):
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
        
class questions(models.Model):
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

    def __str__(self):
        return self.question.html
