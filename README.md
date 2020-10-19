## Осваиваем _Django: ORM_

### Что это ?
Учебный проeкт. По легенде необходимо доработать пульт охраны банка. При наличие готовой базы и шаблонов верстки разработать функционал по визуализации истории посещений, продолжительности посещений и выявлении подозрительно долгих визитов.

### Зачем ?
Это учебный проeкт от [_devman_](https://dvmn.org/modules/) для повышения навыков.   
Исходный код находится [_здесь_](https://github.com/dvmn-tasks/django-orm-watching-storage).


### Как запустить ?

 1. Склонировать проeкт
```
you@name: git clone https://github.com/StiffRedson/django-orm-watching-storage.git
```

 2. Установить окружение
 ```
 you@name: python3 -m venv venv
 you@name: source venv/bin/activate
 you@name: pip install -r requirements.txt
 ```

 3. Настройте _django-orm-watching-storage/project/settings.py_   
Проeкт учебный, но данные принято скрывать. Для теста я оставил актуальные данные по дефолту, но приоритет у указанных в _.env_.  При необходимости _.env_ придется создать самостоятельно.     

__Пример ключей в .env__
> SECRET_KEY=    
> SQL_HOST=    
> SQL_PORT=5432    
> SQL_NAME=    
> SQL_USER=    
> SQL_PASSWORD=    


 4. Запустить сервер
 ```
 you@name: python3 main.py
 ```

По адресу [127.0.0.1:8000](127.0.0.1:8000) визуализированы данные: по действующим пропускам, история посещения и продолжительность.

## Автор
---
| Contacts | Ivan Fedorov          |
|----------|-----------------------|
| Email    | StiffRedson@gmail.com |
| Telegram | @StivaRedson          |
