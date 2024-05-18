from turtle import mode
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Questions(models.Model):
    chapter = models.IntegerField()
    image = models.ImageField(upload_to="quiz_images/")
    answer = models.CharField(max_length=255)

    def __int__(self):
        return self.id

class ExamLog(models.Model):
    user = models.ForeignKey (User,
                              on_delete=models.CASCADE,
                              related_name='userWhoSolved')
    chapter = models.IntegerField()
    exam_dateTime = models.DateTimeField(default=timezone.now)
    total_num_of_questions = models.IntegerField()
    num_of_correct_questions = models.IntegerField()
    exam_result = models.JSONField()

    def calculateResult(self, solved_questions):
        self.total_num_of_questions = len(solved_questions)
        self.num_of_correct_questions = sum([1 for sq in solved_questions if sq.wasRight])
        self.examResult = {
           "total_num_of_questions": self.total_num_of_questions,
           "num_of_correct_questions": self.num_of_correct_questions,
           "wrong_answers": [
               {'question_id': sq.solved_questions.id, "submitted_answer": sq.submittied_answer}
               for sq in solved_questions if not sq.was_right
           ]
        }
        self.save()

class SolvedQuestions(models.Model):
    user = models.ForeignKey (User,
                              on_delete=models.CASCADE,
                              related_name='userWhoSolved')
    solved_questions = models.ForeignKey(Questions,
                                       on_delete=models.CASCADE,
                                       related_name='solvedQuestions')
    exam_log = models.ForeignKey(ExamLog, on_delete=models.CASCADE, related_name='solvedQuestionsLog')
    was_right = models.BooleanField()
    submitted_answer = models.CharField(max_length=255)

    class Meta:
        unique_together = ('username', 'wrong_questions', 'exam_log')

    '''
    데이터 저장 및 결과 계산
사용자가 문제를 다 풀고 나면, SolvedQuestions에 데이터를 저장하고, ExamLog의 calculate_results 메서드를 호출하여 시험 결과를 계산하고 저장합니다. 이전의 결과를 변경하지 않도록, 새로운 시험 로그와 해결된 문제를 새롭게 생성해야 합니다.

python
Copy code
# Example usage:
# Create a new ExamLog instance for the new quiz attempt
exam_log = ExamLog(username=user, chapter=chapter)
exam_log.save()

# Solved questions for this particular exam attempt
solved_questions = [
    SolvedQuestions(username=user, solvedQuestions=question, wasRight=is_correct, submitted_answer=answer, exam_log=exam_log)
    for question, is_correct, answer in user_answers
]

# Bulk create solved questions
SolvedQuestions.objects.bulk_create(solved_questions)

# Calculate and save the results for the current exam log
exam_log.calculate_results(solved_questions)
    '''