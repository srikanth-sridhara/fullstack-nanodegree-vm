""" This is the setup needed for the inventory database """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Categories(Base):
    """ Categories Table """
    __tablename__ = 'categories'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        """ This function is used to serialize the table objects """
        return {
            'name': self.name,
            'id': self.id,
        }

class CategoryItems(Base):
    """ Category Items Table """
    __tablename__ = 'category_items'
    title = Column(String(80), nullable=False)
    description = Column(String(250))
    photo = Column(String(250))

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)

    @property
    def serialize(self):
        """ This function is used to serialize the table objects """
        return {
            'title': self.title,
            'description': self.description,
            'id': self.id,
            'category_id': self.category_id,
        }


db = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(db)
