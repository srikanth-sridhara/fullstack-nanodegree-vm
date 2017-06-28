from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItems

engine = create_engine('sqlite:///inventory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

### Categories db functions ###
def getCategories():
    return session.query(Categories).all()

def newCategory(categoryName):
    categoryToAdd = Categories(name=categoryName)
    session.add(categoryToAdd)
    session.commit()

def editRestaurant(restaurant_id, restaurantName=None, restaurantAddress=None, restaurantCategory=None):
    restaurantToEdit = getRestaurant(restaurant_id)
    if restaurantName != None:
        restaurantToEdit.name = restaurantName
    if restaurantAddress != None:
        restaurantToEdit.address = restaurantAddress
    if restaurantCategory != None:
        restaurantToEdit.category = restaurantCategory
    session.add(restaurantToEdit)
    session.commit()

def deleteRestaurant(restaurant_id):
    restaurantToDelete = getRestaurant(restaurant_id)
    session.delete(restaurantToDelete)
    session.commit()

def getRestaurant(restaurant_id):
    return session.query(Restaurant).filter_by(id=restaurant_id).one()


### Category Items db functions ###
def showMenu(restaurant_id):
    return session.query(CategoryItems).filter_by(restaurant_id=restaurant_id).all()

def newMenuItem(restaurant_id, name, course=None, description=None, price=None):
    newItem = CategoryItems(
        name=str(name),
        course=str(course),
        description=str(description),
        price=str(price),
        restaurant_id=restaurant_id)
    session.add(newItem)
    session.commit()

def editMenuItem(restaurant_id, menu_id, itemName=None, itemCourse=None, itemDescription=None, itemPrice=None):
    itemToEdit = getMenuItem(menu_id)
    if itemName != None:
        itemToEdit.name = itemName
    if itemCourse != None:
        itemToEdit.course = itemCourse
    if itemDescription != None:
        itemToEdit.description = itemDescription
    if itemPrice != None:
        itemToEdit.price = itemPrice
    # if restaurant_id != itemToEdit.restaurant_id:
    #     itemToEdit.restaurant_id = restaurant_id
    session.add(itemToEdit)
    session.commit()

def deleteMenuItem(menu_id):
    itemToDelete = getMenuItem(menu_id)
    session.delete(itemToDelete)
    session.commit()

def getMenuItem(menu_id):
    return session.query(CategoryItems).filter_by(id=menu_id).one()
