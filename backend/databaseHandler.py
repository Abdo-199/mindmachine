from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database model
Base = declarative_base()

class DatabaseHandler:

    def __init__(self, data_directory, database_name):
        self.database_directory = data_directory + '/' +database_name
        self.create_conncetion()    

    def create_conncetion(self):
        # Configure the database connection
        self.engine = create_engine(f'sqlite:///{self.database_directory}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    # CRUD operations using SQLAlchemy ORM

    def check_for_Admin(self, user):
        if user.is_admin:
            return True
        else:
            return False

    def check_for_user(self, user_id):
        user = self.get_user(user_id)
        if user is None:
            return False
        else:
            return True

    def add_user(self, user_id, name, email, is_admin):

        does_user_exist = self.check_for_user(user_id)
        if does_user_exist:
            return False

        session = self.Session()
        new_user = User(user_id=user_id, name=name, email=email, is_admin=is_admin)
        session.add(new_user)
        session.commit()
        session.close()

    def get_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter(User.user_id == user_id).first()
        session.close()
        return user

    def get_all_users(self):
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return users

    def update_user(self, user_id, name=None, email=None, is_admin=None):
        session = self.Session()
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

    def delete_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def log_search(self, user_id, query, session=None):
        if session is None:
            session = self.Session()
        try:
            new_search_history = SearchHistory(user_id=user_id, search_query=query)
            session.add(new_search_history)
            session.commit()
        except Exception as e:
            print(f"Error in log_search: {e}")
        finally:
            if session is None:
                session.close()



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
    