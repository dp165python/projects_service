import os

from core.constants import APP_ENV_DEV, APP_ENV_PROD


class Config:
    DB_USER = os.environ.get('DB_USER', 'eugene')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '1401')
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEBUG = False
    HOST = '127.0.0.1'
    TOKEN = os.environ.get('TOKEN', None)
    DB_NAME = os.environ.get('DB_NAME', 'projects')
    DB_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    DB_NAME = os.environ.get('DB_NAME', 'test_api')


class ProductionConfig(Config):
    pass


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProductionConfig

    return DevelopmentConfig
