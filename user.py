"""
Created on 7/17/2023

@author: yuraheo
"""

import mysql.connector
from configparser import ConfigParser
import bcrypt
CNX= mysql.connector.connect (conn)




def login(userName: str, password: str) -> str:
    if (userName is None or password is None):
        return False

    args = [userName, password]
    result_args = executeSQLQuery("CheckUser",args)
    # returns => ('admin', 'admin', 1)
    if result_args is not None:
        hashed_password = result_args[1]
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            return result_args[0]
    return None




def executeSQLQuery(query, args):
    global CNX
    if (CNX is None):
        config = ConfigParser()
        config. read("config.ini")
        _host = config.get('MySQL', 'host')
        _port = config.get('MySQL', 'port')
        _database = config.get('MySQL', 'database')
        _user = config.get('MySQL', 'user')
        _password = config.get('MySQL', 'password')
        CNX = mysql.connector.connect(host=_host, database=_database,
                                      user=_user, passwd=_password, port=_port)

        with CNX.cursor() as cur:
            return cur.callproc(query, args)


def signup(userName: str, password: str) -> bool:
    if userName is None or password is None:
        return False

    if check_user_exists(userName):
        return False

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    save_user(userName, hashed_password)

    return True


    


def check_user_exists(userName: str) -> bool:
    args = [userName]
    result_args = executeSQLQuery("CheckUserExists", args)

    if result_args is not None:
        return result_args[0] >0
    return False


def save_user(userName: str, hashed_password: str) -> str:
    args = [userName, hashed_password]
    result_args = executeSQLQuery("SaveUser", args)
    if result_args is not None:
        return result_args[0]


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

