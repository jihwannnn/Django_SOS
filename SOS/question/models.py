from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Questions(models.Model):
    chapter = models.IntegerField()
    image = models.ImageField(upload_to="quiz_images/")
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

class ExamLog(models.Model):
    username = models.ForeignKey (User,
                                  on_delete=models.CASCADE,
                                  related_name='userWhoSolved')
    chapter = models.IntegerField()
    examDateTime = models.DateTimeField()
    examResult = models.JSONField()

class SolvedQuestions(models.Model):
    username = models.ForeignKey (User,
                                  on_delete=models.CASCADE,
                                  related_name='userWhoHadSolved')
    solvedQuestions = models.ForeignKey(Questions,
                                       on_delete=models.CASCADE,
                                       related_name='solvedQuestions')
    wasRight = models.BooleanField()
    submitted_answer = models.CharField(max_length=255)