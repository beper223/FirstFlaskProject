
# 🎬 Flask Movie Search App

Веб-приложение на Flask для поиска фильмов по названию, актёру, жанру и году. Запросы логируются в таблицу `search_logs`, где учитывается частота поиска.

## 🚀 Функциональность

- 🔍 Поиск фильмов с фильтрами: название, актёр, категория, год
- 📈 Логирование поисков с подсчётом количества обращений
- 📊 Отображение популярных запросов
- 💾 Работа с базой данных MySQL через контекстный менеджер
- 🎨 Интерфейс на Bootstrap 5

## 🗃 Структура проекта

```
project/
│
├── app.py                  # Основной Flask-приложение
├── db.py                   # Контекстный менеджер MySQL
├── templates/
│   └── index.html          # HTML-шаблон
├── static/                 # (необязательно) стили, изображения и т.д.
├── requirements.txt        # Зависимости
└── README.md               # Документация
```

## 🛠 Установка

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## ⚙️ Настройка базы данных

Создайте базу данных MySQL и выполните SQL-скрипты из `schema.sql`, содержащие таблицы:

- `actor`, `category`, `film`
- `film_actor`, `film_category`
- `search_logs`

## 📝 Пример `.env` или конфигурации (в `db.py`)

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'filmdb'
}
```

## ▶️ Запуск

```bash
python app.py
```

Приложение будет доступно по адресу:  
📍 http://localhost:5000

## 📋 Пример запроса

```
http://localhost:5000/?film=Matrix&actor=Keanu&year=1999
```

## ✅ Зависимости

- Flask
- mysql-connector-python
- Bootstrap (через CDN)

## 📌 Примечания

- Значения поля `search_type` в `search_logs`: `keyword`, `genre`, `year`, `actor`
- При повторном запросе счётчик `search_count` увеличивается

## 📸 Интерфейс

![preview](preview.png)

## 📄 License

MIT License
