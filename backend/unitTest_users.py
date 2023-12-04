import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_orm import Base, User, SearchHistory, log_search

class TestUserCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
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

    def test_log_search(self):
        self.add_user('101', 'Test User', 'test@example.com', False)

        # Verify user is added
        user = self.session.query(User).filter_by(user_id='101').first()
        self.assertIsNotNone(user)

        # Log a search query using the same session
        log_search('101', 'test query', self.session)

        # Retrieve and verify the logged search
        logged_search = self.session.query(SearchHistory).filter_by(user_id='101').first()
        self.assertIsNotNone(logged_search)


if __name__ == '__main__':
    unittest.main()
