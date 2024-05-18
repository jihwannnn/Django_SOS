from django.urls import path
from . import views

app_name = 'question'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('quiz/', views.quiz, name='quiz'),
    path('retest/', views.retest, name='retest'),
    path('study/', views.study, name='study'),
    path('quiz/<int:chapter_num>/', views.quiz, name='quiz_chapter'),
]