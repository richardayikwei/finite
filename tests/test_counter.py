from app.counter import increment_count_manager, get_count_manager, get_connection
import pytest
import os
import psycopg2


class TestDabaseChanges:
    @pytest.fixture(scope="class")
    def conn(self):
        connection = get_connection()
        yield connection
        connection.close()

    def reset_counter(self, conn):
        cur = conn.cursor()
        cur.execute("UPDATE test_password_counter SET clicks = 0 WHERE id = 1;")
        conn.commit()
        cur.close()

    def dolittle(self):
        pass

    def test_get_count_manager(self, conn):
        self.reset_counter(conn)
        assert get_count_manager(connect_info=conn, database_name="test_password_counter") == 0

    def test_increment_count_manager(self, conn):
        self.reset_counter(conn)
        increment_count_manager(self.dolittle,connect_info=conn, database_name = "test_password_counter")
        # assert get_count_manager(connect_info=conn, database_name="test_password_counter") == 1