import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'strong key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/votask.db'
    WTF_CSRF_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class Develop(Config):
    DEBUG = True


class Deploy(Config):

    def init_app(app):
        Config.init_app(app)


config = {
    'develop': Develop,
    'deploy': Deploy,
}
