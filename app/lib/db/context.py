from contextlib import contextmanager
import mysql.connector

from conf.db_conf import DB_CONFIG


@contextmanager
def will_commit(connection):
    try:
        yield
        connection.commit()
    except mysql.connector.Error as e:
        print(f'Something with db went wrong: {e}')
        connection.rollback()


@contextmanager
def db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        yield connection
    finally:
        connection.close()
