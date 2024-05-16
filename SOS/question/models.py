from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model

# Create your models here.

class Questions(models.Model):
    chapter = models.IntegerField()
    image = models.ImageField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

class examLog(models.Model):
    username = models.ForeignKey (User,
                                  on_delete=models.CASCADE,
                                  related_name='username')
    chapter = models.IntegerField()
    examDateTime = models.DateTimeField()
    examResult = models.JSONField()

class SolvedQuestions(models.Model):
    username = models.ForeignKey (User,
                                  on_delete=models.CASCADE,
                                  related_name='username')
    solvedQuestions = models.ForeignKey(Questions,
                                       on_delete=models.CASCADE,
                                       related_name='solved questions')
    wasRight = models.BooleanField()
    submitted_answer = models.CharField()