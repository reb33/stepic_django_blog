#!/bin/bash
source /Users/kbarylnikov/education/stepik/mysite/env/bin/activate
exec gunicorn -c "/Users/kbarylnikov/education/stepik/mysite/mysite/gunicorn_config.py" mysite.wsgi