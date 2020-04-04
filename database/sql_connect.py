# TODO: Link pycharm to mysql database
from mysql.connector import errorcode
import mysql.connector as myc
from cred import config as conff

cursor = None
config = conff


def connect(conf=config):
    global cursor, conn
    try:
        conn = myc.connect(**conf)
    except myc.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Username/pwd")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("DB does not exist")
        else:
            print(err)
    else:
        cursor = conn.cursor()

    return cursor, conn


def close_conn(conn, cursor):
    if conn.is_connected():
        cursor.close()
        conn.close()


def register_user(username, email, phone_number, password):
    global connec, cursor
    try:
        insert_query = 'INSERT INTO Users (username, email, phone_number, user_password) VALUES (%s, %s, %s, %s)'
        quadruple = (username, email, phone_number, password)

        cursor, connec = connect()

        cursor.execute(insert_query, quadruple)
        connec.commit()
    except myc.Error as e:
        print(e)
    finally:
        close_conn(connec, cursor)

