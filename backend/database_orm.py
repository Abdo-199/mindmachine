from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

# Define the database model
Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    user_id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    is_admin = Column(Boolean)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, name={self.name}, email={self.email}, is_admin={self.is_admin})>"

class SearchHistory(Base):
    __tablename__ = 'SearchHistory'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    search_query = Column(String)
    user = relationship("User")

# Function to initialize the database
def initialize_database():
    engine = create_engine('sqlite:///user_search_history_admin.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

# Initialize the database and create a session factory
Session = initialize_database()

# CRUD operations using SQLAlchemy ORM

def add_user(user_id, name, email, is_admin):
    session = Session()
    new_user = User(user_id=user_id, name=name, email=email, is_admin=is_admin)
    session.add(new_user)
    session.commit()
    session.close()

def get_user(user_id):
    session = Session()
    user = session.query(User).filter(User.user_id == user_id).first()
    session.close()
    return user

def get_all_users():
    session = Session()
    users = session.query(User).all()
    session.close()
    return users

def update_user(user_id, name=None, email=None, is_admin=None):
    session = Session()
    user = session.query(User).filter(User.user_id == user_id).first()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        if is_admin is not None:
            user.is_admin = is_admin
        session.commit()
    session.close()

def delete_user(user_id):
    session = Session()
    user = session.query(User).filter(User.user_id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()

def log_search(user_id, query, session=None):
    if session is None:
        session = Session()
    try:
        new_search_history = SearchHistory(user_id=user_id, search_query=query)
        session.add(new_search_history)
        session.commit()
    except Exception as e:
        print(f"Error in log_search: {e}")
    finally:
        if session is None:
            session.close()



# Example usage
if __name__ == "__main__":
    # Add a new user
    add_user('123', 'John Doe', 'johndoe@example.com', False)

    # Retrieve a user
    user = get_user('123')
    print(user)

    # Update a user
    update_user('123', name='Jane Doe')
    log_search('123', 'Human Genes')
    # Delete a user
    # delete_user('123')
