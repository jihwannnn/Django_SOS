from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
    chapter = models.IntegerField()
    image = models.ImageField(upload_to="quiz_images/")
    answer = models.CharField(max_length=255)

    def __int__(self):
        return self.id

class SolvedQuestion(models.Model):
    username = models.ForeignKey (User,
                                  on_delete=models.CASCADE,
                                  related_name='userWhoHadSolved')
    solvedQuestion = models.ForeignKey(Question,
                                       on_delete=models.CASCADE,
                                       related_name='solvedQuestion')
    wasRight = models.BooleanField()
    submitted_answer = models.CharField(max_length=255)
    class Meta:
        unique_together = ('username', 'solvedQuestion')

class ExamLog(models.Model):
    username = models.ForeignKey (User,
                                  on_delete=models.CASCADE,
                                  related_name='userWhoSolved')
    chapter = models.IntegerField()
    examDateTime = models.DateTimeField()
    examResult = models.JSONField()