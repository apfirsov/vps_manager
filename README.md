## Добро пожаловать в проект VPS manager
Это Rest API приложение на фреймоворке DRF, реализованное в рамках тестового задания.

Дополнительно реализованы:

- управление пользователями, аутентификация, авторизация с использованием
[Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html) и
[JWT](https://django-rest-framework-simplejwt.readthedocs.io/).
- Расширение для динамической документации API
[drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)

#### Задание

Используя DRF (Django Rest Framework) разработать REST-сервис для управления виртуальными серверами (VPS).

##### Объект VPS

- uid - идентификатор
- cpu - количество ядер
- ram - объем RAM
- hdd - объем HDD
- status - статус сервера (started, blocked, stopped)

##### API поддерживает операции

- создать VPS
- получить VPS по uid
- получить список VPS с возможностью фильтрации по параметрам
- перевести VPS в другой статус
#### Технологии
- [Django 2.2.16](https://docs.djangoproject.com/en/4.0/releases/2.2.16/)
- [DRF 3.12.4](https://www.django-rest-framework.org/community/release-notes/)

Подробнее в [requirements.txt](https://github.com/apfirsov/vps_manager/blob/main/requirements.txt)

#### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:apfirsov/vps_manager.git
```

```
cd vps_manager
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в головной каталог:

```
cd vps_manager
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

#### Документация к API с примерами запросов/ответов:

Подробная документация доступна по url:
```
http://<your_host>/redoc/
http://<your_host>/swagger/
```

Пример получения списка VPS:
```
GET /api/vps/?cpu=4&status=started
```
```
{
  "count": 1,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "uid": "07cc67f4-45d6-494b-adac-09b5cbc7e2b5",
      "cpu": 4,
      "ram": 16,
      "hdd": 100,
      "status": "started"
    }
  ]
}
```
Пример изменения статуса VPS:
```
POST /api/vps/{uid}/change_status/
```

content type application/json:
```
{
  "status": "stopped"
}
```
Response:
```
{
  "uid": "07cc67f4-45d6-494b-adac-09b5cbc7e2b5",
  "cpu": 4,
  "ram": 16,
  "hdd": 100,
  "status": "stopped"
}
```

****
####  Об авторе
Мой профиль на [GitHub](https://github.com/apfirsov)