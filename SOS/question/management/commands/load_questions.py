from django.core.management.base import BaseCommand
from question.models import Question

class Command(BaseCommand):
    help = 'Load questions into the database'

    def handle(self, *args, **kwargs):
        questions = [
            {"question_text": "What is the capital of France?", "correct_answer": "Paris"},
            {"question_text": "What is 2 + 2?", "correct_answer": "4"},
            # 추가 문제 데이터
        ]
        for q in questions:
            Question.objects.create(**q)
        self.stdout.write(self.style.SUCCESS('Successfully loaded questions'))
