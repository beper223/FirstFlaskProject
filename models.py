# models.py (пример)
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    release_year = Column(Integer)
    category = Column(String)

    # Связь с актёрами (если есть)
    actors = relationship('Actor', secondary='film_actor', back_populates='films')

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    films = relationship('Film', secondary='film_actor', back_populates='actors')

# Промежуточная таблица (если many-to-many)
film_actor = Table(
    'film_actor', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)
