from django.contrib import admin

# Register your models here.
from .models import Questions, ExamLog, SolvedQuestions

admin.site.register(Questions)
admin.site.register(ExamLog)
admin.site.register(SolvedQuestions)