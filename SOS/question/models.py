from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# A model that stores the questions.
# Each question has chapter number, image of the question, and its correct answer.
class Question(models.Model):
    chapter = models.IntegerField()
    image = models.ImageField(upload_to="quiz_images/")
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer

# A model that stroes the questions that users solved.
# Each record contains the user who solved, the question that was solved, 
# boolean indicating whether the user's answer was correct, and the user's answer.
class SolvedQuestion(models.Model):
    user = models.ForeignKey (User,
                              on_delete=models.CASCADE,
                              related_name='user_who_solved')
    solved_questions = models.ForeignKey(Question,
                                       on_delete=models.CASCADE,
                                       related_name='solved_by_users')
    was_right = models.BooleanField()
    submitted_answer = models.CharField(max_length=255)

    # Ensure that each user can solve a particular quesiton only once(if the user solve again, update.)
    class Meta:
        unique_together = ('user', 'solved_questions')

# A model that stores the record of exams in Quiz page and Retest page.
# Each record contains the user who solved, the chapter it belongs to,
# total number of questions that are provided, number of questions which the user got correctly.
class ExamLog(models.Model):
    user = models.ForeignKey (User,
                              on_delete=models.CASCADE,
                              related_name='user_who_had_solved')
    chapter = models.IntegerField()
    exam_dateTime = models.DateTimeField(auto_now_add=True)
    total_solved_questions = models.IntegerField(default=1)
    total_correct_questions = models.IntegerField(default=0)