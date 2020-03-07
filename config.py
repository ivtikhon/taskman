import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'taskman.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = '127.0.0.1:5000'


class TestingConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.getcwd(), 'taskman.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
}