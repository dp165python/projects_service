import os

from core.constants import APP_ENV_DEV, APP_ENV_PROD, APP_ENV_TEST


class Config:
    DB_USER = os.environ.get('DB_USER', 'arthur')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'arthur234')
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEBUG = False
    HOST = '127.0.0.1'
    DB_NAME = os.environ.get('DB_NAME', 'projects')
    DB_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestConfig(Config):
    DB_NAME = os.environ.get('DB_NAME', 'projects_test')


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_TEST:
        return TestConfig
    if env == APP_ENV_PROD:
        return ProductionConfig

    return DevelopmentConfig
