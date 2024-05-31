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
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_1.png"),
             "answer": "4"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_2.png"),
             "answer": "swap page into frame"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_3.png"),
             "answer": "demand paging"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_4.png"),
             "answer": "if bit is i"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_5.png"),
             "answer": "page is on backing store"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_6.png"),
             "answer": "no page fault"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_7.png"),
             "answer": "parent and child share same pages"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_8.png"),
             "answer": "separation between logical and physical memory"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_9.png"),
             "answer": "bring desired page into free frame"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_10.png"),
             "answer": "how many frames to give each process"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_11.png"),
             "answer": "Faults decrease as frames increase"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_12.png"),
             "answer": "Faults don't always decrease as frames increase"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_13.png"),
             "answer": "replace page that has not been used"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_14.png"),
             "answer": "not recently used but modified"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_15.png"),
             "answer": "iminimum number of frames"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_16.png"),
             "answer": "process selects a replacement frame"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_17.png"),
             "answer": "speed of access to memory varies"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_18.png"),
             "answer": "The amount of memory accessible from the TLB"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_19.png"),
             "answer": "pages must sometimes be locked into memory"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "10_20.png"),
             "answer": "shared library shared pages shared library"}
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