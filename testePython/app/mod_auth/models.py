# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
# from app import db

# Define a base model for other database tables to inherit
class Base():

    __abstract__  = True


# Define a User model
class User(Base):
    
    __tablename__ = 'auth_user'

    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)            