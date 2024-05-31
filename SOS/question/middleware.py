# question/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        exempt_urls = [reverse('root'), reverse('question:index'), reverse('question:signup'), reverse('question:logout'), '/admin/']
        
        # 현재 경로가 예외 URL에 포함되어 있지 않고 사용자가 인증되지 않은 경우
        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('question:index')