# webscrapper rest api
### work in progress

----------------------

To test run it as a Django app:
```
pythom manage.py runserver
```
and connect to API:
```
curl http://127.0.0.1:8000/stats/
```
It's an early version. It's working by passing my counter.py methods to restapp/view.py.
It's my first python program, it's slow and against the rules :).

**ToDo:**

1. Create Models for articles and authors instead using model in counter.py
2. Extend webscrapping algorithm to fit in new models
3. Move webscrapping algorithm to background worker (Django Q?)
4. Serializers for new models
5. Modify views to use new models and serializers and output proper JSON
6. Change local database to postgress
6. Reconfigure Dockerfile, docker-compose.yml and requirements.txt to use in docker-compose