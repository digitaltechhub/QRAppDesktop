# TODO: Link pycharm to mysql database
# TODO: Add date automatically to table on registration
from mysql.connector import errorcode
import mysql.connector as myc
from database.cred import config as conff

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
    global cursor, connec
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


def check_user(username):
    """

    :type username: object
    :param username: from login/input, user trying to login
    """
    q = None
    global cursor, connec
    try:
        select_query = "SELECT email, phone_number, user_password FROM Users WHERE username = %s"

        cursor, connec = connect()

        cursor.execute(select_query, (username,))
        q = cursor.fetchall()

    except myc.Error as e:
        print(e)
    finally:
        close_conn(connec, cursor)

    return q


def login_user(username, password):
    # TODO: setup method to return error messages
    # TODO: create last login updated after every successful user login
    result = check_user(username)

    if result:
        pwd = result[0][2]
        if pwd == password:
            return True
        else:
            return False
    else:
        return False
