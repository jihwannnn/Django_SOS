# Django project: SOS, OS quiz website
# 서버 돌리기 전에 makemigrations, migrate, load_questions 꼭 해야됩니다.. createsuperuser하면 admin접속 할 수 있어여

### ***Front***
- 프론트에서 수시로 추가해주세여
static 관련해서 setting.py도 건들고
모든 스타일과 js, html 건듬

5/19 23:02 Changed name incorret_ans to mistake_log
Therefore, changed existing html, css, js files name
Main : (html) add id in 3rd button and (js) add function for url move to mistake_log
Views and urls : add urls and views to handle for mistake_log
Retest : copy quiz's html also the link for css and js


### ***Back***

models.py ->
- Question
- SolvedQuestion
- ExamLog

views.py ->
- index
- main
- logout_view
- signup
- quiz
- retest
- study
- mistake_log
- finishQuiz
