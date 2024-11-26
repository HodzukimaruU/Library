FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app/library_app
COPY requirements.txt /app/library_app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
COPY .env /app/library_app/
#RUN python ./library_app/manage.py collectstatic --noinput
RUN python manage.py collectstatic --noinput
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]