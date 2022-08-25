# YAMBD API
База отзывов пользователей о фильмах, книгах и музыке.


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```python
git clone https://github.com/sergeiivanitsa/api_yamdb.git
```
```python
cd api_yamdb
```
Cоздать директорию для email:
```python
mkdir api_yamdb/sent_emails
```

Cоздать и активировать виртуальное окружение:
```python
python3 -m venv venv
```
```python
source venv/bin/activate
```
```python
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```python
pip install -r requirements.txt
```
Выполнить миграции:
```python
python3 manage.py migrate
```
Запустить проект:
```python
python3 manage.py runserver
```

## Стек
* Django 2.2.16
* djangorestframework 3.12.4
* djangorestframework-simplejwt 5.2.0
