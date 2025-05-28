# from flask import Flask
#
# app = Flask(__name__)
#
# # Импорт views (роуты регистрируются через декоратор @app.route)
# from views import *
#
# if __name__ == '__main__':
#     app.run(debug=True)

# project/app.py
from project import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
