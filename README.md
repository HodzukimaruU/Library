# Library Management App 📚

Это Django-приложение для управления книгами и пользовательскими аккаунтами. Оно позволяет пользователям регистрироваться, подтверждать электронную почту, добавлять и управлять книгами, а также просматривать каталог книг по жанрам.

## Технологии

- **Django**
- **Django REST Framework**
- **SQLite**
- **Celery и Redis**

## Основные функции

### Аутентификация и регистрация

- **Регистрация**: Пользователи могут зарегистрироваться, указав имя, фамилию, email и пароль.
- **Подтверждение email**: После регистрации пользователь получает на email ссылку для подтверждения учетной записи.
- **Авторизация**: Вход в систему с помощью имени пользователя и пароля.
- **Сброс пароля**: Возможность сбросить пароль через email.

    Для проверки функционала в базе уже есть добавленные пользователи, чьи данные можно ввести и авторизироваться:

```yaml
#Первый пользователь
Username: Uppa
Password: 33550k17

#Второй пользователь
Username: mora
Password: 44440k17
```


### Управление профилем

- Пользователи могут просматривать свой профиль.
- Доступ к личным книгам через профиль.

### Управление каталогом книг

- **Добавление, редактирование и удаление книги**: Авторизированные пользователи могут добавлять свои книги с указанием жанра, описания и обложки. А так же редактировать и удалять книги, которые сами создали(книги созданные другими пользователями редактировать и удлаять не могут , а только просматривать)
- **Отоброжение всех книг**: Каталог всех книг с пагинацией на главной странице.
- **Просмотр книги**: Просмотр деталей книги
- Просмотр книг по жанру: Каталог книг, принадлежащих конкретному жанру.

### Celery

- Реализована переодическая задача, которая отправляет ссылку на ютуб-видео раз в 10 минут (Так же в базе добавлен интервал раз в 1 минуту).
- Использование celery beat для переодических задач и celery results для отображения результатов задач в базе.
- Конфигурация celery через .env файл

  Для проверки переодической задачи в файле tasks.py в переменной recipient_list укажите почту на которую переодическая задача будет отправлять письмо:

```yaml
@shared_task
def send_periodic_email():
    subject = 'Регулярное уведомление'
    message = 'Привет! Вот ссылка на интересное видео: https://www.youtube.com/watch?v=rCindpkTgnk'
    from_email = settings.DEFAULT_FROM_EMAIL 
    recipient_list = ['укажите_почту']

    send_mail(subject, message, from_email, recipient_list)

    return 'Email sent successfully'{
    "start_date": "2020-01-01",
    "end_date": "2023-12-31",
    "min_pages": 100,
    "max_pages": 500
}

```

### API

POST запрос на получение списка книг с ранжированием по количеству страниц в отдельном поле в указанный период.
Для проверки запроса можно использовать postman и через отправить на урл http://127.0.0.1:8000/api/ вот такой body:

```yaml
{
    "start_date": "2020-01-01",
    "end_date": "2023-12-31",
    "min_pages": 100,
    "max_pages": 500
}

```

Так же реализация такого запрос в виде sql :

```shell
SELECT * 
FROM core_book
WHERE publication_date >= '2020-01-01'
  AND publication_date <= '2023-12-31'
  AND pages >= 100
  AND pages <= 500
ORDER BY pages;
```

## Запуск и настройка

### Требования

- Docker
- Docker Compose

### Настрока .env

1. Создайте .env файл на одном уровне с docker compose.yaml

```yaml

SECRET_KEY = 'your_django_key'
DEBUG_MODE = True
SERVER_HOST = 'http://127.0.0.1:8000'

###### SMTP ######
EMAIL_HOST = 'your_smtp_server'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'your_smtp_login'
EMAIL_HOST_PASSWORD = 'your_smtp_password'
# EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FROM = 'sender's_email'
DEFAULT_FROM_EMAIL = 'sender's_email'

###### CELERY ######
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TIMEZONE = 'Europe/Minsk'
CELERY_CACHE_BACKEND = 'default'
CACHE_BACKEND = 'redis://redis:6379/1'
```

Зайдите в директорию с docker-compose.yaml и запустите в консоли :

```shell
docker-compose up -d
```
