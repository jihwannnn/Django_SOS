from django.contrib import admin

# Register your models here.
from .models import Question, ExamLog, SolvedQuestion

admin.site.register(Question)
admin.site.register(ExamLog)
admin.site.register(SolvedQuestion)