from flask import Blueprint, render_template, request
from db.db_manager import DatabaseManager
# from . import auth_bp  # Импорт Blueprint из текущего модуля

# Создаём Blueprint с именем 'search' и префиксом URL '/search'
# from flask import Blueprint
auth_bp = Blueprint('search', __name__)


@auth_bp.route('/', methods=['GET'])
def index():
    film = request.args.get('film', '').strip()
    actor = request.args.get('actor', '').strip()
    category = request.args.get('category', '').strip()
    year = request.args.get('year', '').strip()

    with DatabaseManager() as db:
        if film:
            db.save_search_query(film,"keyword")
        if actor:
            db.save_search_query(actor,"actor")
        if category:
            db.save_search_query(category,"genre")
        if year:
            db.save_search_query(year,"year")
        results = db.get_movies(film,actor,category,year)
        popular_queries = db.get_popular_queries()

    return render_template('testindex.html', results=results, popular_queries=popular_queries)


# @auth_bp.route('/about')
# def about():  # put application's code here
#     return render_template('about.html')