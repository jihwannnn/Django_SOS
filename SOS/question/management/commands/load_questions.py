import os
from django.core.management.base import BaseCommand
from django.core.files import File
from question.models import Questions
from django.conf import settings

class Command(BaseCommand):
    help = 'Load questions into the database'

    def handle(self, *args, **kwargs):
        questions = [
            {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "itm_logo.png"),
             "answer": "wow"}
            # 추가 문제 데이터
        ]
        for q in questions:
            if not Questions.objects.filter(chapter=q["chapter"], answer=q["answer"]).exists():
                image_path = q["image"]
                if os.path.exists(image_path):
                    question = Questions(
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