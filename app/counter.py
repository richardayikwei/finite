import psycopg2
import os


conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

def increment_count_manager(func):
    def proxy(*args,**kwargs):
        query = f'UPDATE password_counter SET clicks = clicks + 1 WHERE id = %s;'
        cur.execute(query, (1,))
        conn.commit()  

        return func(*args, **kwargs)
    return proxy

def get_count_manager():
    query = f'SELECT clicks FROM password_counter WHERE id = %s;'
    cur.execute(query, (1,))
    return cur.fetchone()[0]

@increment_count_manager
def hack(a,b,c):
    # print(a + b + c)
    pass

# hack(1, 2, 3)
hack(4, 5, 6)
