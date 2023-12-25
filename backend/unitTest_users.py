import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from database_orm import Base, User, UserSettings, log_search, get_search_history, get_user_settings, update_user_settings, MAX_SEARCH_HISTORY_PER_USER
from databaseHandler import Base, User, SearchHistory, UserSettings, DatabaseHandler, MAX_SEARCH_HISTORY_PER_USER

class TestUserCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.db_handler = DatabaseHandler('', ':memory:')  # Pass the correct database URL

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
        self.add_user('123', 'John Doe', 'johndoe@example.com', False)
        user = self.session.query(User).filter_by(user_id='123').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'John Doe')

    def test_get_user(self):
        self.add_user('124', 'Jane Doe', 'janedoe@example.com', False)
        user = self.session.query(User).filter_by(user_id='124').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'Jane Doe')

    def test_update_user(self):
        self.add_user('125', 'Jim Beam', 'jimbeam@example.com', False)
        user = self.session.query(User).filter_by(user_id='125').first()
        user.name = 'James Beam'
        self.session.commit()

        updated_user = self.session.query(User).filter_by(user_id='125').first()
        self.assertEqual(updated_user.name, 'James Beam')

    def test_delete_user(self):
        self.add_user('126', 'Jack Daniels', 'jackdaniels@example.com', False)
        user = self.session.query(User).filter_by(user_id='126').first()
        self.session.delete(user)
        self.session.commit()

        deleted_user = self.session.query(User).filter_by(user_id='126').first()
        self.assertIsNone(deleted_user)

    def test_get_all_users(self):
        self.add_user('127', 'Johnny Walker', 'johnnywalker@example.com', False)
        self.add_user('128', 'Jim Murray', 'jimmurray@example.com', False)
        users = self.session.query(User).all()
        self.assertTrue(len(users) >= 2)

    def test_log_search_and_get_history(self):
        user_id = 'unique_user_id_for_this_test'
        self.add_user(user_id, 'Search User', 'searchuser@example.com', False)
    def test_log_search_and_get_history(self):
        user_id = 'unique_user_id_for_this_test'
        self.add_user(user_id, 'Search User', 'searchuser@example.com', False)

        # Log multiple search queries
        for i in range(MAX_SEARCH_HISTORY_PER_USER + 2):  # Two more than the limit
            self.db_handler.log_search(user_id, f'Search Query {i + 1}', self.session)

        # Retrieve the search history
        history = self.db_handler.get_search_history(user_id)

        # Check if the search history size is correct (should be MAX_SEARCH_HISTORY_PER_USER)
        self.assertEqual(len(history), MAX_SEARCH_HISTORY_PER_USER)

        # Check the oldest entry in the history (which should be at the end of the list)
        # This entry should be 'Search Query 3' if the first two entries were deleted
        expected_oldest_query = 'Search Query 3'
        self.assertEqual(history[-1].search_query, expected_oldest_query)

    def test_update_and_get_user_settings(self):
        # Create a test user
        user_id = 'setting_test_user'
        self.add_user(user_id, 'Settings Test User', 'settings@test.com', False)

        # Test updating user settings
        logout_timer_test = 7200  # Example value
        max_disk_space_test = 2048  # Example value
        self.db_handler.update_user_settings(user_id, logout_timer_test, max_disk_space_test)

        # Retrieve and test the updated settings
        settings = self.db_handler.get_user_settings(user_id)
        self.assertIsNotNone(settings)
        self.assertEqual(settings.logout_timer, logout_timer_test)
        self.assertEqual(settings.max_disk_space, max_disk_space_test)


if __name__ == '__main__':
    unittest.main()
