# Django project: SOS, OS quiz website

### ***Front***

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
