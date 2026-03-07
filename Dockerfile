FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

RUN mkdir -p /app/media/posts_images
RUN mkdir -p /app/media/avatars

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "a_core.asgi:application"]
CMD python manage.py migrate && daphne -b 0.0.0.0 -p 8000 a_core.asgi:application