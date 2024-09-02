class Config():
    pass

class developmentConfig(Config):
    debug=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

class productionConfig(Config):
    debug=False
    SQLALCHEMY_DATABASE_URI = "postgresql://flask:123@localhost:5432/flask_posts"


config_options={
        'production':productionConfig,
        'development':developmentConfig,
    }