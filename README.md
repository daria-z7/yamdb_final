##  Проект "API_YaMDb"

![example workflow](https://github.com/daria-z7/yamdb_final/actions/workflows/yamdb_worflow.yml/badge.svg)
[![Actions Status](https://github.com/daria-z7/yamdb_final/workflows/Django-app%20workflow/badge.svg)](https://github.com/daria-z7/yamdb_final/actions)

### Описание проекта:

Проект YaMDb даёт возможность собирать отзывы пользователей на произведения, разделенные на категории и отнесенные к одному или нескольким жанрам.

### Технологии:

При реализации проекта были использованы следующие основные технологии, фреймворки и библиотеки:
- Python 3.7
- Django 2.2.16
- Django Rest FrameWork 3.12.4
- Django-filter 21.1

### Как запустить проект:
Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone 'ссылка на репозиторий'
```

```
cd api_yamdb
```

Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```
```
python3 -m pip install --upgrade pip
```

Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполните миграции:

```
python3 manage.py migrate
```

Запустите проект:

```
python3 manage.py runserver
```

### Документация, примеры запросов и ответов:

Обратившись к эндпоинту /redoc/, вы можете ознакомиться с документацией сервиса, посмотреть доступные варианты запросов к серверу и его ответов.

### Авторы проекта:

Проект был реализован в рамках группового проекта студентами 29-ой когорты курса "Phyton-разработчик" Яндекс Практикума. Авторы проекта:
- Зайцева Дарья
- Филлипов Владислав
- Некляев Алексей
