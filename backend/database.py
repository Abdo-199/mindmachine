import sqlite3

def log_search(student_number, query):
    conn = sqlite3.connect('user_search_history_admin.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SearchHistory (student_number, search_query) VALUES (?, ?)",
                   (student_number, query))
    conn.commit()
    conn.close()

#log_search(102, 'Mia Khalifa')
