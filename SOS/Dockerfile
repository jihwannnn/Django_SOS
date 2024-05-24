FROM python:3.11.9
WORKDIR /SOS
COPY requirements.txt /SOS/requirements.txt
COPY manage.py /SOS/manage.py
COPY . /SOS/.
RUN pip install --no-cache-dir -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=SOS.settings
ENV PYTHONUNBUFFERED 1
RUN python manage.py makemigrations question
RUN python manage.py migrate
RUN python manage.py load_questions
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "SOS.wsgi:application"]
EXPOSE 8000