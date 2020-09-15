# windows not supported
# need to install gunicorn first: conda/pip
gunicorn -d --bind 0.0.0.0:5000 src/flask_test_app/gunicorn_main:app
