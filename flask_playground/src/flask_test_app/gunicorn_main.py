import logging

from flask_test_app.web_main import app

# https://trstringer.com/logging-flask-gunicorn-the-manageable-way/
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    app.run()  # no parameter here, use gunicorn to set these

