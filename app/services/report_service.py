from app.database import get_db_connection
from datetime import date, datetime

def get_weekly_cost():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT
            team,
            strftime('%Y-%W', datetime(ts_start, 'unixepoch')) AS week,
            ROUND(SUM(CEIL(duration / 60.0) * rate_per_minute), 4) AS total_cost
        FROM workflows
        JOIN runners ON workflows.runner_id = runners.id
        GROUP BY team, week
        ORDER BY team, week
    ''')
    rows = cursor.fetchall()
    conn.close()
    return [
        {"team": row[0], "week": row[1], "total_cost": row[2]}
        for row in rows
    ]

def get_running_cost(start_date: date, end_date: date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        WITH RECURSIVE dates(d) AS (
            SELECT ?
            UNION ALL
            SELECT date(d, '+1 day') FROM dates WHERE d < ?
        )
        SELECT
            d.d,
            (
                SELECT ROUND(SUM(CEIL(w.duration / 60.0) * r.rate_per_minute), 4)
                FROM workflows w
                JOIN runners r ON w.runner_id = r.id
                WHERE DATE(datetime(w.ts_start, 'unixepoch')) <= d.d
            ) AS running_total
        FROM dates d
    ''', (start_date.isoformat(), end_date.isoformat()))
    rows = cursor.fetchall()
    conn.close()
    return [{"date": row[0], "running_total": row[1] or 0.0} for row in rows]