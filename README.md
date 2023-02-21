# Tree menu test
Django приложение реализовывающее древовидное меню через templatetag. Добавление новых меню и его элементов в бд просходит через админку Django. Нарисовать на любой нужной странице меню по его slug c помощью тега 
```
{% draw_menu 'name' %}
```
где 'main_menu' - slug нужного меню.
# Запуск проекта
```
git clone git@github.com:clownvkkaschenko/django-tree-menu.git
python -m venv venv
source venv/Scripts/activate
```
Перейдите в папку с приложением /app/ установите зависимости и запустите проект
```
pip install -r requirements.txt
```
Выполните миграции
```
python manage.py makemigrations
python manage.py migrate
```
После этого проект будет готов к работе по команде
```
python manage.py runserver
```