import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from .models import Questions, SolvedQuestions, ExamLog



def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('question:main')
        else:
            return render(request, 'question/index.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'question/index.html')


def main(request):
    return render(request, 'question/main.html')

def logout_view(request):
    logout(request)
    return redirect('question:index')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # 입력 검증
        if not username or not password or not password_confirm:
            return render(request, 'question/signup.html', {'error': 'All fields are required'})

        if password != password_confirm:
            return render(request, 'question/signup.html', {'error': 'Passwords do not match'})

        # 사용자 생성 시 예외 처리
        try:
            user = User.objects.create_user(username=username, password=password)
            user.full_clean()  # 추가적인 검증
            user.save()
            login(request, user)
            return redirect('question:index')
        except ValidationError as e:
            return render(request, 'question/signup.html', {'error': e.messages})
        except Exception as e:
            return render(request, 'question/signup.html', {'error': 'An unexpected error occurred'})
    else:
        return render(request, 'question/signup.html')
    
def quiz(request, chapter_num):
    questions = Questions.objects.filter(chapter = chapter_num)

    return render(request, 'question/quiz.html')

def retest(request):
    return render(request, 'question/retest.html')

def study(request):
    return render(request, 'question/study.html')
    
def test(request):
    question = Questions.objects.get(chapter = 8)
    return render(request, 'question/test.html', {
        'question' : question
    })

# Create your views here.
