# project/auth/__init__.py
from flask import Blueprint

# Создаём Blueprint с именем 'auth' и префиксом URL '/auth'
auth_bp = Blueprint(
    'search',
    __name__,
    url_prefix='/',
    template_folder='templates'        # Опционально: своя статика
)

# Импортируем роуты после создания Blueprint (чтобы избежать circular imports)
from . import routes