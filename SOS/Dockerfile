FROM python:3.11.9
WORKDIR /SOS

COPY . /SOS/.

#Dependencies setting
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y nginx

ENV DJANGO_SETTINGS_MODULE=SOS.settings
ENV PYTHONUNBUFFERED 1

COPY nginx.conf /etc/nginx/sites-available/default
RUN rm -f /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled
RUN python manage.py collectstatic --noinput

CMD service nginx start && \ 
    python manage.py makemigrations question && \
    python manage.py migrate && \
    python manage.py load_questions && \ 
    gunicorn --bind 0.0.0.0:8000 SOS.wsgi:application





EXPOSE 80