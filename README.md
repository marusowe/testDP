### Тестовое задание ###

Требуется реализовать web-приложение - аналог bit.ly и подобных систем.
То есть для длинных урлов создает их короткие аналоги <domain>/<subpart>.

Приложение содержит одну страницу на которой:
Форма, в которой можно ввести URL, который должен быть сокращен
Табличка со всеми сокращенными URL (с пагинацией) данного пользователя

Обязательные требования:
* Приложение НЕ содержит авторизации
* Приложение отслеживает пользователей по сессии (использовать сессии Django), т.е. у каждого пользователя свой набор редиректов (правил)
* Данные хранятся в MySQL
* При заходе на сжатый URL приложение редиректит (серверный редирект) на соответствующий URL (который был сжат)
* Пользователь по желанию может указать свой <subpart>. Если такой <subpart> уже используется, нужно сообщить об этом юзеру
* Реализация на Django
* Кэширование редиректов в редисе. Требуется сохранить в редис маппинг сокращенного урла с полным адресом, а не объект правила редиректа полностью. НЕ ИСПОЛЬЗОВАТЬ кэширование представлений, QuerySet’ов, и иные высокоуровневые способы, которые подразумевают лишь установку пары атрибутов в настройке приложения
* Очистка старых правил по расписанию:
удаление записей из MySQL; 
 очистку редиректов из Redis можно реализовать либо вместе с очисткой MySQL, либо по TTL

### Документация ###

* https://docs.google.com/document/d/1jxFdEmsLpeJA2SeXQMQkUzK0Cc2L-s9pUilMS25GTMo/edit?usp=sharing

### Необходимое окружение ###

* Python 3.8
* MySQL
* Redis

### Тесты ###
   `python manage.py test`

### Развертывание ###

1. Скачать с репозитория
2. Установить виратульное окружение Python  
   `python3.8 -m venv venv`
3. Активировать виртуальное окружение  
    `source venv/bin/activate`
4. Установить зависимости  
    `pip install -r requirements.txt`
5. Выполнить файл инциализациия MySQL  
    `mysql -u root -p < mysql/init.sql`
6. Выполнить миграции  
    `python manage.py migrate`
7. Создать суперпользователя для доступа к панели администратора  
    `python manage.py createsuperuser`
8. Запустить приложение  
    `python manage.py runserver`
9. Запустить celery beat для удаления записей по расписанию  
    `celery -A config beat `
10. Запустить celery для выполнения celery beat  
    `celery -A config worker -l INFO`