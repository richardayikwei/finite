import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection(database = "DATABASE_URL"):
    conn = psycopg2.connect(os.getenv(database))
    return conn

def increment_count_manager(func, connect_info = get_connection()):
    def proxy(*args,**kwargs):
        query = f'UPDATE password_counter SET clicks = clicks + 1 WHERE id = %s;'
        with connect_info.cursor() as cur:
            cur.execute(query, (1,))
        connect_info.commit()  

        return func(*args, **kwargs)
    return proxy

def get_count_manager(connect_info = get_connection()):
    query = f'SELECT clicks FROM password_counter WHERE id = %s;'
    with connect_info.cursor() as cur:
        cur.execute(query, (1,))
        return cur.fetchone()[0]
