# project/__init__.py
from flask import Flask
from .search import auth_bp
#from .blog import blog_bp


def create_app():
    app = Flask(__name__)

    # Регистрируем Blueprints
    app.register_blueprint(auth_bp)
    #app.register_blueprint(blog_bp)

    # Настройка конфигурации, БД и других расширений
    # app.config['SECRET_KEY'] = 'your-secret-key'

    return app