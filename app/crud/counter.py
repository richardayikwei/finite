from functools import wraps
from app.db import conn
from psycopg2 import sql

def increment_count_manager(connect_info = conn , database_name="password_counter"):
    """
    connect to database and to specific table
    Parameters
    ----------
    connect_info :
         (Default value = conn) connection to database
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
            query = sql.SQL('UPDATE {} SET clicks = clicks + 1 WHERE id = %s').format(
                sql.Identifier(database_name)
            )
            with connect_info.cursor() as cur:
                cur.execute(query, (1,))
                connect_info.commit()  

            return func(*args, **kwargs)
        return proxy
    return decorator

def get_count_manager(connect_info = conn, database_name="password_counter"):
    """
    connect to database and specific table and retrieve count of passwords generated
    Parameters
    ----------
    connect_info :
         (Default value = conn) connection to database
    database_name :
         (Default value = "password_counter") name of database table

    Returns
    -------
    Count of passwords generated from database
    """
    query = sql.SQL('SELECT clicks FROM {} WHERE id = %s').format(
        sql.Identifier(database_name)
    )
    with connect_info.cursor() as cur:
        cur.execute(query, (1,))
        return cur.fetchone()[0]