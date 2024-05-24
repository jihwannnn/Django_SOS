from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
    chapter = models.IntegerField()
    image = models.ImageField(upload_to="quiz_images/")
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

class SolvedQuestion(models.Model):
    user = models.ForeignKey (User,
                              on_delete=models.CASCADE,
                              related_name='user_who_solved')
    solved_questions = models.ForeignKey(Question,
                                       on_delete=models.CASCADE,
                                       related_name='solved_by_users')
    was_right = models.BooleanField()
    submitted_answer = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user', 'solved_questions')

class ExamLog(models.Model):
    user = models.ForeignKey (User,
                              on_delete=models.CASCADE,
                              related_name='user_who_had_solved')
    chapter = models.IntegerField()
    exam_dateTime = models.DateTimeField(auto_now_add=True)
    total_solved_questions = models.IntegerField()
    total_correct_questions = models.IntegerField()