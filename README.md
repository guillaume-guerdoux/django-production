# django-production
This repository is a basic repository to use django in production with nginx, uwsgi, docker and git

https://gist.github.com/noelboss/3fe13927025b89757f8fb12e9066f2fa
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
https://www.codementor.io/samueljames/nginx-setting-up-a-simple-proxy-server-using-docker-and-python-django-f7hy4e6jv
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
https://medium.com/@tiago.arasilva/django-build-an-app-with-docker-and-nginx-fd491a05ba2a

First :  DEPLOYMENT WITH GIT ON REMOTE SERVER
https://gist.github.com/noelboss/3fe13927025b89757f8fb12e9066f2fa
https://medium.com/@francoisromain/vps-deploy-with-git-fea605f1303b

First try only with the gist tuto
if that doesnt work, try to use rights chmod, rights to be able to write in files

SECOND : For the uwsgi nginx developement
Begining is like that : 
sudo apt-get update
export LC_ALL=C
sudo apt-get upgrade
sudo apt-get install python3-dev
sudo apt-get install python3-pip
sudo apt-get install virtualenv
virtualenv "my_site_venv" -p python3
activate venv

From venv, get your git repo

pip3 install uwsgi
pip3 install django
pip3 install -r requirements.txt

Then follow entirely the tuto : https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

Once you have installend the django uwsgi nginx, you need to deal with celery and redis

THIRD : CELERY AND REDIS

1. Celery Daemonization ! 
First you need to create a new user celery

sudo groupadd celery
sudo useradd -g celery celery

Then created this file as: /etc/default/celeryd

Put the content of http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#generic-init-scripts in it

then copy and past this file https://raw.githubusercontent.com/celery/celery/3.1/extra/generic-init.d/celeryd in  /etc/init.d/celeryd

Then make this file executable : chmod +x /etc/init.d/celeryd
Grand permissions to user celery : 
chown -R celery:celery /var/log/celery/
chown -R celery:celery /var/run/celery/

Finally you can run sudo /etc/init.d/celeryd start

If this doest not work : here are the links 
http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#generic-init-scripts
https://pythad.github.io/articles/2016-12/how-to-run-celery-as-a-daemon-in-production
https://stackoverflow.com/questions/28825760/celery-not-running-permission-denied


2. Redis server daemonization
https://stackoverflow.com/questions/6910378/how-can-i-stop-redis-server
sudo /etc/init.d/redis-server start


Finally, when you push a modification on a celery task, you only need to do 
sudo /etc/init.d/celeryd restart



For DJANGO DEV AND PROD 
Create a file named localsettings.py imported by settings.py where there is the dev or prod parameters
Field to put in localsettings : 
  "secret_key"
  "debug"
  "allowed_hosts"
  "sent_address"
  "server_email"
  "email_host"
  "email_port"
  "email_password"
  "email_host_user"

To create secret key : 
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()


