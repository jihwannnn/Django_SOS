import os
import random
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('question:index')
        else:
            return render(request, 'question/index.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'question/index.html')


def main(request):
    return render(request, 'question/main.html')

def logout_view(request):
    logout(request)
    return redirect('question:login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            return render(request, 'myapp/signup.html', {'error': 'Passwords do not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('question:index')
        except Exception as e:
            return render(request, 'question/signup.html', {'error': str(e)})
    else:
        return render(request, 'question/signup.html')
    
    
# Create your views here.
