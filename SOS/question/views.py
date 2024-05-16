from django.shortcuts import render
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

    
# Create your views here.
