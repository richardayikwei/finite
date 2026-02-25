import psycopg2
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

def get_connection():
    """
    Open connection to database 
    """
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

def increment_count_manager(connect_info = get_connection() , database_name="password_counter"):
    """
    connect to database and to specific table
    Parameters
    ----------
    connect_info :
         (Default value = get_connection()) connection function to database
    database_name :
         (Default value = "password_counter") name of database table

    Returns
    -------
    function that was decorated
    """
    def decorator(func):
        """

        Parameters
        ----------
        func :
            

        Returns
        -------

        """
        @wraps(func)
        def proxy(*args,**kwargs):
            """

            Parameters
            ----------
            *args :
                
            **kwargs :
                

            Returns
            -------

            """
            query = f'UPDATE {database_name} SET clicks = clicks + 1 WHERE id = %s;'
            with connect_info.cursor() as cur:
                cur.execute(query, (1,))
                connect_info.commit()  

            return func(*args, **kwargs)
        return proxy
    return decorator

def get_count_manager(connect_info = get_connection(), database_name="password_counter"):
    """
    connect to database and specific table and retrieve count of passwords generated
    Parameters
    ----------
    connect_info :
         (Default value = get_connection()) connection function to database
    database_name :
         (Default value = "password_counter") name of database table

    Returns
    -------
    Count of passwords generated from database
    """
    query = f'SELECT clicks FROM {database_name} WHERE id = %s;'
    with connect_info.cursor() as cur:
        cur.execute(query, (1,))
        return cur.fetchone()[0]