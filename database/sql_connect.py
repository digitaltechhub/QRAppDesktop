from mysql.connector import errorcode
import mysql.connector as myc
from .cred import config as conff

cursor = None
config = conff


def connect(conf):
    global cursor
    try:
        conn = myc.connect(**config)
    except myc.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Username/pwd")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("DB does not exist")
        else:
            print(err)
    else:
        cursor = conn.cursor()

    return cursor


cursor = connect(config)
print(type(cursor))
