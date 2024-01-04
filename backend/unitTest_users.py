import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from database_orm import Base, User, UserSettings, log_search, get_search_history, get_user_settings, update_user_settings, MAX_SEARCH_HISTORY_PER_USER
from databaseHandler import Base, User, SearchHistory, DatabaseHandler
from datetime import datetime, timedelta

class TestUserCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///testing.db')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.db_handler = DatabaseHandler('','testing.db')  # Pass the correct database URL

    def setUp(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def add_user(self, user_id, name, email, is_admin):
        new_user = User(user_id=user_id, name=name, email=email, is_admin=is_admin)
        self.session.add(new_user)
        self.session.commit()

    def test_add_user(self):
        self.add_user('130', 'John Doe', 'johndoe@example.com', False)
        user = self.session.query(User).filter_by(user_id='130').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'John Doe')

    def test_get_user(self):
        self.add_user('130', 'Jane Doe', 'janedoe@example.com', False)
        user = self.session.query(User).filter_by(user_id='130').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'Jane Doe')

    def test_update_user(self):
        self.add_user('129', 'Jim Beam', 'jimbeam@example.com', False)
        user = self.session.query(User).filter_by(user_id='129').first()
        user.name = 'James Beam'
        self.session.commit()

        updated_user = self.session.query(User).filter_by(user_id='129').first()
        self.assertEqual(updated_user.name, 'James Beam')

    def test_delete_user(self):
        self.add_user('126', 'Jack Daniels', 'jackdaniels@example.com', False)
        user = self.session.query(User).filter_by(user_id='126').first()
        self.session.delete(user)
        self.session.commit()

        deleted_user = self.session.query(User).filter_by(user_id='126').first()
        self.assertIsNone(deleted_user)

    def test_get_all_users(self):
        self.add_user('132', 'Johnny Walker', 'johnnywalker@example.com', False)
        self.add_user('133', 'Jim Murray', 'jimmurray@example.com', False)
        users = self.session.query(User).all()
        self.assertTrue(len(users) >= 2)

    def test_log_search(self):
        self.add_user('101', 'Test User', 'test@example.com', False)

        # Verify user is added
        user = self.session.query(User).filter_by(user_id='101').first()
        self.assertIsNotNone(user)

        # Log a search query using the DatabaseHandler instance
        self.db_handler.log_search('101', 'test query', self.session)

        # Retrieve and verify the logged search
        logged_search = self.session.query(SearchHistory).filter_by(user_id='101').first()
        self.assertIsNotNone(logged_search)

    def add_user_with_login(self, user_id, name, email, is_admin, days_ago):
        """
        Helper method to add a user with a specified last login time.
        """
        session = self.Session()  # Use a new session for this operation
        last_login_time = datetime.now() - timedelta(days=days_ago)
        new_user = User(user_id=user_id, name=name, email=email, is_admin=is_admin, last_login=last_login_time)
        session.add(new_user)
        session.commit()
        session.close()

    def test_update_last_login(self):
        self.add_user('201', 'Active User', 'active@example.com', False)

        session = self.Session()  # Create a new session for this operation
        self.db_handler.update_last_login('201')  # Ensure this method commits the change
        session.close()

        # Verify the change
        session = self.Session()
        updated_user = session.query(User).filter_by(user_id='201').first()
        session.close()
        self.assertIsNotNone(updated_user.last_login)

    def test_get_active_users(self):
        self.add_user_with_login('301', 'Active User1', 'active1@example.com', False, 10)  # 10 days ago
        self.add_user_with_login('302', 'Inactive User', 'inactive@example.com', False, 40)  # 40 days ago

        # Validation of setup data
        user_301 = self.session.query(User).filter_by(user_id='301').first()
        user_302 = self.session.query(User).filter_by(user_id='302').first()
        print(f"User 301 last login: {user_301.last_login}, User 302 last login: {user_302.last_login}")

        active_users = self.db_handler.get_active_users()
        self.assertTrue(any(user.user_id == '301' for user in active_users))
        self.assertFalse(any(user.user_id == '302' for user in active_users))

    def test_get_inactive_users(self):
        self.add_user_with_login('401', 'Active User', 'active@example.com', False, 10)  # 10 days ago
        self.add_user_with_login('402', 'Inactive User', 'inactive@example.com', False, 40)  # 40 days ago

        inactive_users = self.db_handler.get_inactive_users()
        self.assertTrue(any(user.user_id == '402' for user in inactive_users))
        self.assertFalse(any(user.user_id == '401' for user in inactive_users))

if __name__ == '__main__':
    unittest.main()
