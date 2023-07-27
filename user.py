"""
Created on 7/17/2023

@author: yuraheo
"""

from db_fxn import get_user_password, add_user, check_user_exists

from configparser import ConfigParser
import bcrypt








def login(userName: str, password: str) -> bool:
    if (userName is None or password is None):
        return False

    if password != get_user_password(userName):
        return False
    
    if password == get_user_password(userName):
        return True


def signup(userName: str, password: str) -> bool:
    if userName is None or password is None:
        error_message = "Both userName and password must be provided."
        return False, error_message


    if check_user_exists(userName):
        error_message = "User already exists. Please choose a different userName."
        return False, error_message

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    add_user(userName, hashed_password)
    return True





def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()


# def save_user(userName: str, hashed_password: str) -> str:
#     args = [userName, hashed_password]
#     result_args = executeSQLQuery("SaveUser", args)
#     if result_args is not None:
#         return result_args[0]




# def executeSQLQuery(query, args):
#     global CNX
#     if (CNX is None):
#         config = ConfigParser()
#         config. read("config.ini")
#         _host = config.get('MySQL', 'host')
#         _port = config.get('MySQL', 'port')
#         _database = config.get('MySQL', 'database')
#         _user = config.get('MySQL', 'user')
#         _password = config.get('MySQL', 'password')
#         CNX = mysql.connector.connect(host=_host, database=_database,
#                                       user=_user, passwd=_password, port=_port)

#         with CNX.cursor() as cur:
#             cur.callproc(query, args)
#         # Fetch the result of the stored procedure
#             result = None
#             for result_args in cur.stored_results():
#                 result = result_args.fetchone()[0]
#             return result
