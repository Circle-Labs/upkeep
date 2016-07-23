## Dev

To Start

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

To Save
```
pip freeze > requirements.txt
```

## Prod

Requires
```
Must be in /var/apps with read/write permissions
redis on redis://localhost:6379/0
nginx server from nginx.conf
virtualenv installed
```

Commands
```
virtualenv venv
. ven/bin/activate
pip install -r requirments.txt
mkdir log
mkdir static
cp keys.py to reminders/
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
supervisord
supervisorctl
>status
```
reload nginx
