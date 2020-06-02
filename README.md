**Usage:**

    1. Run command - python manage.py migrate
    1. Run server - python manage.py runserver
    2. Run bot - python bot.py

P.S<br>
All users have password "strong_password".
If in config file number_of_users = 3 bot create 3 users with username "user_0", "user_1" and "user_2".

**API:**
    
    POST - /api/v1/signup
    Request:
        {
            "username": "testuser", 
            "password": "strong_password"
        }
    Response:
        {
            "username": "testuser", 
            "last_activity": null, 
            "last_activity": null
        }
    
    POST - /api/v1/login
    Request:
        {
            "username": "testuser", 
            "password": "strong_password"
        }
    Response:
        {
            "token": "XXX"
        }
    
    Add header {Authorization: JWT XXX}
    GET - /api/v1/users
    Response:
        {
            "count": 10,
            "next": null,
            "previous": null,
            "results": [
                {
                  "username": "testuser",
                  "last_login": "2020-06-02T13:12:47",
                  "last_activity": "2020-06-02T13:12:48"
                },
                ...
            ]
        }

    GET - /api/v1/users/<user_id>
    Response:
        {
            "username": "testuser",
            "last_login": "2020-06-02T13:12:47",
            "last_activity": "2020-06-02T13:12:48"
        }
    
    POST - /api/v1/posts/
    Request:
        {
            "subject": "Test",
            "body": "Some text here"
        }
    Response:
        {
            "id": 1,
            "author": "testuser",
            "subject": "Test",
            "body": "Some text here",
            "pub_date": "2020-05-31T17:41:37",
            "total_likes": 0,
            "is_fan": false
        }
    
    GET - /api/v1/posts
    Response:
        {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "author": "testuser",
                    "subject": "Test",
                    "body": "Some text here",
                    "pub_date": "2020-05-31T17:41:37",
                    "total_likes": 0,
                    "is_fan": false
                }
            ]
        }
    
    GET - /api/v1/posts/<post_id>
    Response:
        {
            "id": 1,
            "author": "testuser",
            "subject": "Test",
            "body": "Some text here",
            "pub_date": "2020-05-31T17:41:37",
            "total_likes": 0,
            "is_fan": false
        }
    
    POST - /api/v1/posts/<post_id>/like/

    POST - /api/v1/posts/<post_id>/unlike/
    
    GET - /api/v1/posts/<post_id>/fans
    Response:
        [
            {
                "username": "testuser",
                "last_login": "2020-06-02T13:12:47",
                "last_activity": "2020-06-02T13:12:48"
            },
            ...
        ]
    
    GET - /api/v1/analytics?date_from=2020-05-30&date_to=2020-06-02
    Response:
        [
            {
            "date": "2020-06-02",
            "total_likes": 19
            }
        ]