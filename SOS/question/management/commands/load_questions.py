import os
from django.core.management.base import BaseCommand
from django.core.files import File
from question.models import Questions
from django.conf import settings

class Command(BaseCommand):
    help = 'Load questions into the database'

    def handle(self, *args, **kwargs):
        # this json is for loading questions
        questions = [
            {"chapter": 8,
             "image": os.path.join(settings.MEDIA_ROOT, "quiz_images", "itm_logo.png"),
             "answer":"wow"}
            # 추가 문제 데이터
        ]
        for q in questions:
            # check if the question is already loaded in DB
            if not Questions.objects.filter(chapter=q["chapter"], answer=q["answer"]).exists():
                with open(q["image"], 'rb') as img_file:
                    question = Questions(
                        chapter = q["chapter"],
                        answer = q["answer"]
                    )
                    question.image.save(os.path.basename(q["image"]), File(img_file), save=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded question: {q["answer"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skipping duplicated question: {q["answer"]}'))
        self.stdout.write(self.style.SUCCESS('Finished loading questions'))
