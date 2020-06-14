import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # log level
    LOG_LEVEL = logging.DEBUG
    USERNAME = 'test'
    PASSWORD = 'e10adc3949ba59abbe56e057f20f883e'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_PORT = 3306
    MYSQL_DB = 'flask'
    SECRET_KEY = 'mLZXDOv12YwdM9ZG'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    # Bootstrap flask config
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = True
    BOOTSTRAP_CDN_FORCE_SSL = True
    FLASKY_POSTS_PER_PAGE = 10
    # file upload path and file upload extensions
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@127.0.0.1:3306/flask"

    # Redis Config
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    DECODE_RESPONSES = os.environ.get('decode_responses', True)
    REDIS_PASSWORD = 'redis_pwd'


class TestingConfig(Config):
    """测试环境下的配置"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@127.0.0.1:3306/flask"


class ProductionConfig(Config):
    """生成环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@127.0.0.1:3306/flask"

    # Redis Config
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    DECODE_RESPONSES = os.environ.get('decode_responses', True)
    REDIS_PASSWORD = 'redis_pwd'


config = {
    'Development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
