from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_periodic_email():
    subject = 'Регулярное уведомление'
    message = 'Привет! Вот ссылка на интересное видео: https://www.youtube.com/watch?v=rCindpkTgnk'
    from_email = settings.DEFAULT_FROM_EMAIL 
    recipient_list = ['maksim.malhinau@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return 'Email sent successfully'