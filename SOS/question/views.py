from django.db import IntegrityError
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Func, FloatField
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
import logging

from .models import Question, SolvedQuestion, ExamLog

class Random(Func):
    function = 'RANDOM'
    output_field = FloatField()

def root_view(request):
    # 사용자가 인증된 경우 메인 페이지로 리다이렉트
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

@login_required
def main(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'question/main.html', context)

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
            return render(request, 'question/signup.html', {'error': 'The user is already registered'})
    else:
        return render(request, 'question/signup.html')

logger = logging.getLogger(__name__)

@login_required
@csrf_exempt
@login_required
def quiz(request, chapter_num):
    logger.debug("Entered quiz view with chapter_num: %s", chapter_num)
    current_user = request.user
    questions = Question.objects.filter(chapter=chapter_num)
    total_questions = questions.count()
    total_1 = total_questions - 1
    current_index = int(request.GET.get('q', 0))
    current_index = max(0, min(current_index, total_questions - 1))
    current_question = questions[current_index] if total_questions > 0 else None

    logger.debug("Total questions: %d, Current index: %d", total_questions, current_index)

    if request.method == 'POST':
        try:
            logger.debug("Processing POST request")
            data = json.loads(request.body)
            submitted_answers = data.get('answers')
            logger.debug("Submitted answers: %s", submitted_answers)

            if not current_user.is_authenticated:
                logger.warning("User not authenticated")
                return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=401)

            total_correctness = 0
            for i, question in enumerate(questions):
                correctness = False
                if question.answer.lower() == submitted_answers[i].lower():
                    correctness = True
                    total_correctness += 1
                solved_question, created = SolvedQuestion.objects.get_or_create(
                    user=current_user,
                    solved_questions=question,
                    defaults={'was_right': correctness, 'submitted_answer': submitted_answers[i]}
                )
                if not created:
                    # If the solved question already exists, update it
                    solved_question.was_right = correctness
                    solved_question.submitted_answer = submitted_answers[i]
                    solved_question.save()
                logger.debug("Saved solved question: %s", solved_question)
            exam_log = ExamLog(
                user=current_user,
                chapter=chapter_num,
                exam_dateTime=timezone.now(),
                total_solved_questions=total_questions,
                total_correct_questions=total_correctness
            )
            exam_log.save()
            logger.debug("Saved exam log: %s", exam_log)

            request.session['correct_answers'] = total_correctness
            request.session['incorrect_answers'] = total_questions - total_correctness
            request.session['total_questions'] = total_questions
            request.session['chapter_num'] = chapter_num

            return JsonResponse({'success': True})
        except IntegrityError as e:
            logger.error("IntegrityError in quiz view: %s", str(e))
            return JsonResponse({'success': False, 'message': 'Integrity error occurred: ' + str(e)}, status=500)
        except Exception as e:
            logger.error("Error in quiz view: %s", str(e), exc_info=True)
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
        'total_1': total_1
    }
    logger.debug("Rendering quiz template with context: %s", context)
    return render(request, 'question/quiz.html', context)

@login_required
@csrf_exempt
@login_required
def retest(request, chapter_num):
    logger.debug("Entered quiz view with chapter_num: %s", chapter_num)
    current_user=request.user
    questions = SolvedQuestion.objects.filter(user = current_user, solved_questions__chapter=chapter_num, was_right=False)
    total_questions = questions.count()
    total_1 = total_questions - 1
    current_index = int(request.GET.get('q', 0))
    current_index = max(0, min(current_index, total_questions - 1))
    current_question = questions[current_index] if total_questions > 0 else None

    logger.debug("Total questions: %d, Current index: %d", total_questions, current_index)

    if request.method == 'POST':
        try:
            logger.debug("Processing POST request")
            data = json.loads(request.body)
            submitted_answers = data.get('answers')
            logger.debug("Submitted answers: %s", submitted_answers)

            if not current_user.is_authenticated:
                logger.warning("User not authenticated")
                return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=401)

            total_correctness = 0
            for i, question in enumerate(questions):
                correctness = False
                if question.solved_questions.answer.lower() == submitted_answers[i].lower():
                    correctness = True
                    total_correctness += 1
                solved_question, created = SolvedQuestion.objects.get_or_create(
                    user=current_user,
                    solved_questions=question.solved_questions,
                    defaults={'was_right': correctness, 'submitted_answer': submitted_answers[i]}
                )
                if not created:
                    # If the solved question already exists, update it
                    solved_question.was_right = correctness
                    solved_question.submitted_answer = submitted_answers[i]
                    solved_question.save()
                logger.debug("Saved solved question: %s", solved_question)
            exam_log = ExamLog(
                user=current_user,
                chapter=chapter_num,
                exam_dateTime=timezone.now(),
                total_solved_questions=total_questions,
                total_correct_questions=total_correctness
            )
            exam_log.save()
            logger.debug("Saved exam log: %s", exam_log)

            request.session['correct_answers'] = total_correctness
            request.session['incorrect_answers'] = total_questions - total_correctness
            request.session['total_questions'] = total_questions
            request.session['chapter_num'] = chapter_num

            return JsonResponse({'success': True})
        except IntegrityError as e:
            logger.error("IntegrityError in quiz view: %s", str(e))
            return JsonResponse({'success': False, 'message': 'Integrity error occurred: ' + str(e)}, status=500)
        except Exception as e:
            logger.error("Error in quiz view: %s", str(e), exc_info=True)
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
        'total_1': total_1
    }
    logger.debug("Rendering quiz template with context: %s", context)
    return render(request, 'question/retest.html', context)

@login_required
def study(request, chapter_num):
    questions = Question.objects.filter(chapter=chapter_num)
    total_questions = questions.count()
    total_1 = total_questions - 1
    current_index = int(request.GET.get('q', 0))
    current_index = max(0, min(current_index, total_questions - 1))
    current_question = questions[current_index] if total_questions > 0 else None

    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
        'total_1': total_1,
    }
    return render(request, 'question/study.html', context)

@login_required
def mistake_log(request):
    mistake_logs = ExamLog.objects.filter(user=request.user.id).order_by('-exam_dateTime') # '-exam_dateTime' means that it is sorted by newest first.
    return render(request, 'question/mistake_log.html', {"exam_logs": mistake_logs})  #add by G

def test(request):
    question = Question.objects.get(chapter = 8)
    return render(request, 'question/test.html', {
        'question' : question
    })

@login_required
def result(request):
    correct_answers = request.session.get('correct_answers', 0)
    incorrect_answers = request.session.get('incorrect_answers', 0)
    total_questions = request.session.get('total_questions', 0)
    chapter_num = request.session.get('chapter_num', 0)

    context = {
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
        'total_questions': total_questions,
        'chapter_num': chapter_num,
    }

    return render(request, 'question/result.html', context)


# Create your views here.
