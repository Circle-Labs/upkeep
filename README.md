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
cp keys.py to reminders/
supervisord
supervisorctl
>status
```
reload nginx
