from cgi import test
from django.urls import path
from . import views


app_name = 'question'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('retest/<int:chapter_num>/', views.retest, name='retest'),
    path('quiz/<int:chapter_num>/', views.quiz, name='quiz'),
    path('study/<int:chapter_num>/', views.study, name='study'),
    path('mistake_log/', views.mistake_log, name='mistake_log'), #add by g
    path('result/', views.result, name='result'),

    # for testing
    path('test/', views.test, name='test')
]