# windows not supported
# need to install uwsgi first, conda/pip
# https://hackersandslackers.com/deploy-flask-uwsgi-nginx/
# https://pypi.org/project/Flask-uWSGI-WebSocket/
# https://pypi.org/project/pyuwsgi/
uwsgi --http 127.0.0.1:8080  --module src/flask_test_app/uwsgi_main:app

# or run with ini file
# https://pythonise.com/series/learning-flask/python-flask-uwsgi-introduction
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
# https://towardsdatascience.com/how-to-do-rapid-prototyping-with-flask-uwsgi-nginx-and-docker-on-openshift-f0ef144033cb
# uwsgi uwsgi.ini
