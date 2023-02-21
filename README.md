# Tree menu test
Django приложение реализовывающее древовидное меню через templatetag. Добавление новых меню и его элементов в бд просходит через админку Django. Нарисовать на любой нужной странице меню по его slug c помощью тега 
```
{% draw_menu 'name' %}
```
где 'main_menu' - slug нужного меню.
# Запуск проекта
```
https://github.com/FuR1DeV/test_uptrade
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
