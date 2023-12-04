import sqlite3
import unittest

def log_search(student_number, query):
    conn = sqlite3.connect('user_search_history_admin.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SearchHistory (student_number, search_query) VALUES (?, ?)",
                   (student_number, query))
    conn.commit()
    conn.close()

def add_user(student_number, name, email, is_admin):
    """Add a new user to the Users table."""
    conn = sqlite3.connect('user_search_history_admin.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Users (student_number, name, email, is_admin)
        VALUES (?, ?, ?, ?)
    """, (student_number, name, email, is_admin))
    conn.commit()
    conn.close()

def get_user(student_number):
    """Retrieve a user's details by student number."""
    conn = sqlite3.connect('user_search_history_admin.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Users WHERE student_number = ?
    """, (student_number,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
    """Retrieve all users' details."""
    conn = sqlite3.connect('user_search_history_admin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(student_number, name=None, email=None, is_admin=None):
    """Update a user's details."""
    conn = sqlite3.connect('user_search_history_admin.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Users
        SET name = COALESCE(?, name),
            email = COALESCE(?, email),
            is_admin = COALESCE(?, is_admin)
        WHERE student_number = ?
    """, (name, email, is_admin, student_number))
    conn.commit()
    conn.close()

def delete_user(student_number):
    """Delete a user from the database."""
    conn = sqlite3.connect('user_search_history_admin.db')
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Users WHERE student_number = ?
    """, (student_number,))
    conn.commit()
    conn.close()

class TestDatabaseCRUD(unittest.TestCase):
    def setUp(self):
        # Set up a test user
        self.test_student_number = 999
        self.test_name = "Test User"
        self.test_email = "test@example.com"
        self.test_is_admin = False
        add_user(self.test_student_number, self.test_name, self.test_email, self.test_is_admin)

    def test_add_user(self):
        user = get_user(self.test_student_number)
        self.assertIsNotNone(user)
        self.assertEqual(user[0], self.test_student_number)  # Corrected index for student_number
        self.assertEqual(user[1], self.test_name)             # Corrected index for name

    def test_update_user(self):
        new_name = "Updated Test User"
        update_user(self.test_student_number, name=new_name)
        user = get_user(self.test_student_number)
        self.assertEqual(user[1], new_name)  # Corrected index for name

    def test_delete_user(self):
        delete_user(self.test_student_number)
        user = get_user(self.test_student_number)
        self.assertIsNone(user)

    def tearDown(self):
        # Clean up the test user
        delete_user(self.test_student_number)

if __name__ == '__main__':
    unittest.main()



#log_search(101, 'Testing')

# add_user(105, "Test", "test_user@gmail.com", 0)


# update_user(104, is_admin=0)
# delete_user(105)
# my_user = get_user(105)
# print(my_user)

# my_list = get_all_users()
#
# print(my_list)