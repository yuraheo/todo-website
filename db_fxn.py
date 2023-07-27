import sqlite3
conn = sqlite3.connect("data.db",  check_same_thread = False)
c = conn.cursor()


# Database
# Table
# Field/Columns
# DataType


def create_user_table():
    c.execute('''CREATE TABLE IF NOT EXISTS usertable(userId TEXT, passWord TEXT)''')



def create_task_table():
    c.execute('''CREATE TABLE IF NOT EXISTS tasktable(userId TEXT, task TEXT, task_status TEXT, task_due_date DATE)''')


def add_tasks(userId, task, task_status, task_due_date):
    c.execute('''INSERT INTO tasktable(userId, task, task_status,
              task_due_date) VALUES(?,?,?,?)''',(userId, task, task_status, task_due_date))
    conn.commit()



def view_all_tasks(userId):
    c.execute('''SELECT task, task_status, task_due_date FROM tasktable WHERE userId = "{}"'''.format(userId))
    data = c.fetchall()
    return data


def view_unique_tasks():
    c.execute('''SELECT DISTINCT task FROM tasktable''')
    data = c.fetchall()
    return data

def get_task(task, userId):
    c.execute('''SELECT * FROM tasktable WHERE task=? and userId=?''',
        (task, userId))
    data = c.fetchall()
    return data


def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date, userId):
    c.execute(
        '''UPDATE tasktable SET task=?, task_status=?, task_due_date=? WHERE task=? and task_status=? and task_due_date=? and userId=?''',
        (new_task, new_task_status, new_task_date, task, task_status,
         task_due_date, userId))
    conn.commit()
    data = c.fetchall()
    return data


def delete_task(task, userId):
    c.execute('''DELETE FROM tasktable WHERE task=? and userId=?''',
        (task, userId))
    conn.commit()

def add_user(userId, passWord):
    c.execute('''INSERT INTO usertable (userId, passWord) VALUES (?, ?)''', (userId, passWord))
    conn.commit()

def get_user_password(userId):
    c.execute('''SELECT passWord FROM usertable WHERE userId = ?''', (userId,))
    data = c.fetchone()
    if not data:
        return None
    return data[0]


    
def check_user_exists(userId):
    c.execute('''SELECT * FROM usertable WHERE userId=?''', (userId,))
    data = c.fetchall()
    return len(data) > 0

    










