import psycopg
import config


def get_connection():
    return psycopg.connect(
        host=config.DB_HOST,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )


def get_employees():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, username, fullname, department
        FROM employees
        ORDER BY id
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def count_employees():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM employees")

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total
