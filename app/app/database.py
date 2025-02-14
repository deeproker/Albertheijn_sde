import sqlite3
from pathlib import Path
import csv

def get_db_connection():
    return sqlite3.connect('data.db')

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS runners (
            id INTEGER PRIMARY KEY,
            size TEXT,
            rate_per_minute REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workflows (
            id TEXT PRIMARY KEY,
            project INTEGER,
            team TEXT,
            ts_start INTEGER,
            duration INTEGER,
            runner_id INTEGER,
            name TEXT,
            success INTEGER,
            FOREIGN KEY(runner_id) REFERENCES runners(id)
        )
    ''')

    # Load base data if runners table is empty
    cursor.execute('SELECT COUNT(*) FROM runners')
    if cursor.fetchone()[0] == 0:
        csv_path = Path(__file__).parent / 'base_data_runner_rate.csv'
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rate = float(row['rate_per_minute'].replace(',', '.'))
                cursor.execute('''
                    INSERT INTO runners (id, size, rate_per_minute)
                    VALUES (?, ?, ?)
                ''', (int(row['id']), row['size'], rate))
        conn.commit()
    conn.close()