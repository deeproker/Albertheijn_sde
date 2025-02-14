import unittest
import sqlite3
import os
from app.database import init_db, get_db_connection

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup code
        if os.path.exists("data.db"):
            os.remove("data.db")
        init_db()

    @classmethod
    def tearDownClass(cls):
        # Teardown code
        if os.path.exists("data.db"):
            os.remove("data.db")

    def test_database_initialization(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM runners')
        count = cursor.fetchone()[0]
        self.assertEqual(count, 5)  # Expecting 5 runners from the CSV
        conn.close()

if __name__ == "__main__":
    unittest.main()