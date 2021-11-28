# api_final
Финальная версия проекта API для Yatube: данное API позволяет просматривать списки существующих постов авторов, создавать, редактировать, изменять, удалять существующие посты, просматривать, оставлять редактировать, создавать комментарии к существующим постам, просматривать список групп, а также подписываться на авторов и просматривать списки подписок. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/malyshevadv/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:

Запрос токена доступа:
'''
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json

{
    "username": "string",
    "password": "string"
}
'''


Публикация поста:
'''
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "Мой первый пост"
}
'''

Публикация поста с указанием группы:
'''
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "My perfect post",
    "group": 1
}
'''

Получение списка постов:
'''
GET http://127.0.0.1:8000/api/v1/posts/
'''

Получение списка постов с ограничением количества на страницу и смещением: 
'''
GET http://127.0.0.1:8000/api/v1/posts/?limit=1&offset=1
'''

Изменение поста:
'''
PUT http://127.0.0.1:8000/api/v1/posts/2/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "My perfect post changed",
    "group": 1
}
'''

Обновление поста:
'''
PATCH http://127.0.0.1:8000/api/v1/posts/1/
Content-Type: application/json
Authorization: Bearer <token>

{
    "group": 2
}
'''

Удаление поста:
'''
DELETE http://127.0.0.1:8000/api/v1/posts/4/
Content-Type: application/json
Authorization: Bearer <token>
'''

Добавление комментария к посту:
'''
POST http://127.0.0.1:8000/api/v1/posts/2/comments/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "Another rude comment"
}
'''

Получение списка комментариев:
'''
GET http://127.0.0.1:8000/api/v1/posts/2/comments/
Content-Type: application/json
Authorization: Bearer <token>
'''

Обновление комментария:
'''
PATCH http://127.0.0.1:8000/api/v1/posts/2/comments/1/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "Changed another rude comment"
}
'''

Замена комментария:
'''
PUT http://127.0.0.1:8000/api/v1/posts/2/comments/3/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "Replaced another rude comment"
}
'''

Удаление комментария:
'''
DELETE http://127.0.0.1:8000/api/v1/posts/3/comments/2/
Content-Type: application/json
Authorization: Bearer <token>
'''

Получение списка групп:
'''
GET http://127.0.0.1:8000/api/v1/groups/
Content-Type: application/json
'''

Получение детальной инфомрации о группе:
'''
GET http://127.0.0.1:8000/api/v1/groups/2/
Content-Type: application/json
'''

Подписка на автора:
'''
POST http://127.0.0.1:8000/api/v1/follow/
Content-Type: application/json
Authorization: Bearer <token>

{
    "following": "User2"
}
'''

Получение списка подписок:
'''
GET http://127.0.0.1:8000/api/v1/follow/
Content-Type: application/json
Authorization: Bearer <token>
'''

Поиск определенного автора среди подписок:
'''
GET http://127.0.0.1:8000/api/v1/follow/?search=User
Content-Type: application/json
Authorization: Bearer <token>
'''
