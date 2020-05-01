import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY") or "Do_not_reuse_(wtfKey)_Add_environ_if_going_live"
    MAIL_SERVER=os.environ.get('MAIL_SERVER','smtp.gmail.com')
    MAIL_PORT=int(os.environ.get("MAIL_PORT","587"))
    MAIL_USE_TLS=os.environ.get("MAIL_USE_TLS",'true').lower() in ['true','on','1']
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME",'obeythetestinggoat2@gmail.com')
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
    FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'
    FLASKY_MAIL_SENDER='FLASKY Admin <flasky@example.com>'
    FLASKY_ADMIN=os.environ.get('FLASKY_ADMIN',"obeythetestinggoat2@gmail.com")#recepient
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    FLASKY_POSTS_PER_PAGE=5
    FLASKY_COMMENTS_PER_PAGE=3
    SQLALCHEMY_RECORD_QUERIES=True
    FLASKY_SLOW_DB_QUERY_TIME=0.5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get("DEV_DATABASE_URL") or 'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')
    #if left is undefined, right will be evaluated

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get("DEV_DATABASE_URL") or 'sqlite://'
    WTF_CSRF_ENABLED=False
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DEV_DATABASE_URL") or 'sqlite:///'+os.path.join(basedir,'data.sqlite')
    @classmethod
    def init_app(cls,app):
        Config.init_app(app)
        #email errors to admin
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure=None
        if getattr(cls,"MAIL_USERNAME",None) is not None:
            credentials=(cls.MAIL_USERNAME,cls.MAIL_PASSWORD)
            if getattr(cls,"MAIL_USE_TLS",None):
                secure=()
        mail_handler=SMTPHandler(
            mailhost=(cls.MAIL_SERVER,cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX+" Application Error",
            credentials=credentials,
            secure=secure
            )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
    }