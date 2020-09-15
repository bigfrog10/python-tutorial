# windows not supported
# need to install uwsgi first, conda/pip
# https://hackersandslackers.com/deploy-flask-uwsgi-nginx/
uwsgi --http 127.0.0.1:8080  --module src/flask_test_app/uwsgi_main:app

# or run with ini file
# https://pythonise.com/series/learning-flask/python-flask-uwsgi-introduction
# uwsgi uwsgi.ini
