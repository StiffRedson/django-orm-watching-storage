## Осваиваем _Django: ORM_

### Что это ?
Учебный проeкт. По легенде необходимо доработать винный сайт-магазин. При наличие готовой базы и шаблонов верстки разработать функционал по визуализации истории посещений, продолжительности посещений и выявлении подозрительно долгих визитов.

### Зачем ?
Это учебный проeкт от [_devman_](https://dvmn.org/modules/) для повышения навыков.   
Исходный код находится [_здесь_](https://github.com/dvmn-tasks/django-orm-watching-storage).


### Как запустить ?

 1. Склонировать проeкт
```
you@name: git clone https://github.com/StiffRedson/django-orm-watching-storage.git
```

 2. Установить и активировать окружение
 ```
 you@name: python3 -m venv venv
 you@name: source venv/bin/activate
 you@name: pip install -r requirements.txt
 ```

 3. Настройте _django-orm-watching-storage/project/settings.py_   
Проeкт учебный, но данные принято скрывать. Для теста я оставил актуальные данные ниже. Фаил _.env_ придется создать самостоятельно.     

__Пример ключей в .env__

> DEBUG=0   
> SECRET_KEY=REPLACE_ME    
> SQL_ENGINE=django.db.backends.postgresql_psycopg2    
> SQL_HOST=checkpoint.devman.org   
> SQL_PORT=5434    
> SQL_NAME=checkpoint   
> SQL_USER=guard  
> SQL_PASSWORD=osim5



 4. Запустить сервера
 ```
 you@name: python3 manage.py runserver 0.0.0.0:8000
 ```

По адресу [127.0.0.1:8000](http://127.0.0.1:8000) визуализированы данные: по действующим пропускам, история посещения и продолжительность.

## Контакты
---
| Contacts | Ivan Fedorov          |
|----------|-----------------------|
| Email    | StiffRedson@gmail.com |
| Telegram | @StivaRedson          |
