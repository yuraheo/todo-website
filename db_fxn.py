import sqlite3
conn = sqlite3.connect("data.db",  check_same_thread = False)
c = conn.cursor()


# Database
# Table
# Field/Columns
# DataType




def create_user_table():
    c.execute('''CREATE TABLE IF NOT EXISTS userstable(userId TEXT, task TEXT, task_status TEXT, task_due_date DATE)''')


def add_tasks(userId, task, task_status, task_due_date):
    c.execute('''INSERT INTO userstable(userId, task, task_status,
              task_due_date) VALUES(?,?,?,?)''',(userId, task, task_status, task_due_date))
    conn.commit()



def view_all_tasks(userId):
    c.execute('''SELECT task, task_status, task_due_date FROM userstable WHERE userId = "{}"'''.format(userId))
    data = c.fetchall()
    return data


def view_unique_tasks():
    c.execute('''SELECT DISTINCT task FROM userstable''')
    data = c.fetchall()
    return data

def get_task(task, userId):
    c.execute('''SELECT * FROM userstable WHERE task=? and userId=?''',
        (task, userId))
    data = c.fetchall()
    return data

# def get_user(userId):
#     c.execute('''SELECT * FROM userstable WHERE userId= "{}"'''.format(userId))
#     data = c.fetchall()
#     return data


def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date, userId):
    c.execute(
        '''UPDATE userstable SET task=?, task_status=?, task_due_date=? WHERE task=? and task_status=? and task_due_date=? and userId=?''',
        (new_task, new_task_status, new_task_date, task, task_status,
         task_due_date, userId))
    conn.commit()
    data = c.fetchall()
    return data


def delete_task(task, userId):
    c.execute('''DELETE FROM userstable WHERE task=? and userId=?''',
        (task, userId))
    conn.commit()








