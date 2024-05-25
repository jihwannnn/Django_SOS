import enum
from re import sub
from time import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import json
from django.core.exceptions import ValidationError

from .models import Question, SolvedQuestion, ExamLog

def root_view(request):
    # 사용자가 인증된 경우 메인 페이지로 리다이렉트
    if request.user.is_authenticated:
        return redirect('question:main')
    else:
        return redirect('question:index')


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
    current_user=request.user.id
    questions = Question.objects.filter(chapter=chapter_num)

    # deliver index number of one question as a url pattern
    total_questions = questions.count()
    
    # start from 0
    current_index = int(request.GET.get('q', 0))

    # ensuring index range
    current_index = max(0, min(current_index, total_questions - 1))

    current_question = questions[current_index] if total_questions > 0 else None

    if request.method == 'POST':
        # Get the submitted answers JSON and parse it
        submitted_answers_json = request.POST.get('submitted_answers')
        submitted_answers = json.loads(submitted_answers_json)['answers']
        total_correctness = 0
        for i, question in enumerate(questions):
            correctness = False
            if question.answer in submitted_answers[i]:
                correctness = True
                total_correctness += 1
            solved_question = SolvedQuestion(
                user = current_user,
                solved_questions = question,
                was_right = correctness,
                submitted_answer = submitted_answers[i]
            )
            solved_question.save()

        # Save the exam log
        exam_log = ExamLog(
            user = current_user,
            chapter = chapter_num,
            exam_dateTime = timezone.now(),
            total_solved_questions = total_questions,
            total_correct_questions = total_correctness
        )
        exam_log.save()

    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
    }
    return render(request, 'question/quiz.html', context)


def retest(request, chapter_num):
    current_user=request.user.id
    questions = SolvedQuestion.objects.filter(chapter=chapter_num, was_right=False)

    # deliver index number of one question as a url pattern
    total_questions = questions.count()
    
    # start from 0
    current_index = int(request.GET.get('q', 0))

    # ensuring index range
    current_index = max(0, min(current_index, total_questions - 1))

    current_question = questions[current_index] if total_questions > 0 else None

    if request.method == 'POST':
        # Get the submitted answers JSON and parse it
        submitted_answers_json = request.POST.get('submitted_answers')
        submitted_answers = json.loads(submitted_answers_json)['answers']
        total_correctness = 0
        for i, question in enumerate(questions):
            correctness = False
            if question.answer in submitted_answers[i]:
                correctness = True
                total_correctness += 1
            solved_question = SolvedQuestion(
                user = current_user,
                solved_questions = question,
                was_right = correctness,
                submitted_answer = submitted_answers[i]
            )
            solved_question.save()

        # Save the exam log
        exam_log = ExamLog(
            user = current_user,
            chapter = chapter_num,
            exam_dateTime = timezone.now(),
            total_solved_questions = total_questions,
            total_correct_questions = total_correctness
        )
        exam_log.save()

    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
    }
    return render(request, 'question/retest.html', context)

def study(request, chapter_num):
    questions = Question.objects.filter(chapter=chapter_num)

    # deliver index number of one question as a url pattern
    total_questions = questions.count()

    # start from 0
    current_index = int(request.GET.get('q', 0))

    # ensuring index range
    current_index = max(0, min(current_index, total_questions - 1))

    current_question = questions[current_index] if total_questions > 0 else None

    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
    }
    return render(request, 'question/study.html', context)

def mistake_log(request):
    return render(request, 'question/mistake_log.html')  #add by G

def test(request):
    question = Question.objects.get(chapter = 8)
    return render(request, 'question/test.html', {
        'question' : question
    })

def finishQuiz(request, examResult):
    if request.method == 'POST':
        user = request.POST.get('user')
        chapter = request.POST.get('chapter')
        exam_dateTime = request.POST.get('exam_dateTime')
        exam_result = request.POST.get('exam_result')
        exam_log = ExamLog(
            user=user,
            chapter=chapter,
            exam_dateTime=exam_dateTime,
            exam_result=exam_result
        )
        exam_log.save()


# Create your views here.
