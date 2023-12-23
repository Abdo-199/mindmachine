from sqlalchemy import create_engine, Column, DateTime, Float, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
import os
import config

# Define the database model
Base = declarative_base()


class DatabaseHandler:

    def __init__(self, data_directory, database_name):
        self.database_directory = os.path.join(data_directory, database_name)
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

    def get_number_of_asked_questions(self, given_timestamp): 
        session = self.Session()
        number_of_asked_questions = session.query(SearchHistory).filter(
            SearchHistory.timestamp <= datetime.utcnow(),
            SearchHistory.timestamp >= given_timestamp).count()
        session.close()
        return number_of_asked_questions

    def get_search_history(self, user_id):
        session = self.Session()
        history = session.query(SearchHistory).filter(SearchHistory.user_id == user_id).order_by(
            SearchHistory.timestamp.desc()).all()
        session.close()
        return history

    def log_search(self, user_id, query, session = None):
        if session is None:
            session = self.Session()
        try:
            # Check if max history count reached
            current_history_count = session.query(SearchHistory).filter(SearchHistory.user_id == user_id).count()
            if current_history_count >= config.max_search_history_per_user:
                # Delete the oldest entry
                oldest_entry = session.query(SearchHistory).filter(SearchHistory.user_id == user_id).order_by(
                    SearchHistory.timestamp.asc()).first()
                session.delete(oldest_entry)

            # Add new search history
            new_search_history = SearchHistory(user_id=user_id, search_query=query)
            session.add(new_search_history)
            session.commit()
        except Exception as e:
            print(f"Error in log_search: {e}")
            session.rollback()

    def test_user_settings(self):
        # Ensure the database and tables are initialized
        session = self.Session()
        # Create a test user if they don't exist
        user_id = 'test_user'
        # add_user(user_id, 'Test User', 'testuser@example.com', False)
        self.log_search('user_id', 'Human Genes 22', session)
        history = self.get_search_history('user_id')
        print(f"Search History for User:")
        for record in history:
            print(f"  {record.timestamp}: {record.search_query}")  # Delete a user

        # history = get_search_history('123')

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
    user_id = Column(String, ForeignKey('Users.user_id'))
    search_query = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)  # Timestamp for each search
    user = relationship("User")

if __name__ == "__main__":
    data_directory = ""
    database_name = "test.db"
    db_handler = DatabaseHandler(data_directory, database_name)
    db_handler.test_user_settings()