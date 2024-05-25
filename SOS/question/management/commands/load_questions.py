import os
from django.core.management.base import BaseCommand
from django.core.files import File
from question.models import Question
from django.conf import settings

class Command(BaseCommand):
    help = 'Load questions into the database'

    def handle(self, *args, **kwargs):
        questions = [
            {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "itm_logo.png"),
             "answer": "a"},
            # 추가 문제 데이터
            {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "1.png"),
             "answer": "b"},
            {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "2.png"),
             "answer": "c"},

            {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "3.png"),
             "answer": "a"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "4.png"),
             "answer": "b"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "5.png"),
             "answer": "c"},

             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "6.png"),
             "answer": "a"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "7.png"),
             "answer": "b"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "8.png"),
             "answer": "c"},
        ]
        for q in questions:
            if not Question.objects.filter(chapter=q["chapter"], answer=q["answer"]).exists():
                image_path = q["image"]
                if os.path.exists(image_path):
                    question = Question(
                        chapter=q["chapter"],
                        answer=q["answer"]
                    )
                    # 기존 파일을 참조
                    question.image.name = os.path.relpath(image_path, settings.MEDIA_ROOT)
                    question.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully loaded question: {q["answer"]}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Image file not found: {image_path}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skipping duplicated question: {q["answer"]}'))
        self.stdout.write(self.style.SUCCESS('Finished loading questions'))