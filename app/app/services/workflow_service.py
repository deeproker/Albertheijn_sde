from app.database import get_db_connection
import sqlite3

def insert_workflows(workflows):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for wf in workflows:
            cursor.execute('''
                INSERT INTO workflows
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                wf.id, wf.project, wf.team, wf.ts_start,
                wf.duration, wf.runner_id, wf.name, wf.success
            ))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise ValueError(f"Database error: {str(e)}")
    finally:
        conn.close()