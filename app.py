
import streamlit as st
import pandas as pd
from db_fxn import create_user_table, add_tasks, view_all_tasks, \
  view_unique_tasks, get_task, edit_task_data, delete_task
import plotly.express as px

from user import login, signup

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
signupSection = st.container()
logOutSection = st.container()


def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    st.session_state['userId'] = None



def show_logout_page():
    loginSection.empty()
    with logOutSection:
        st.button("Log Out", key = "logout", on_click = LoggedOut_Clicked)


def signed_up_Clicked(userName, password):
  if signup(userName, password):
      st.session_state['loggedIn'] = True
      st.session_state['userId'] = userName



def LoggedIn_Clicked(userName, password):
    if login(userName, password):
        st.session_state['loggedIn'] = True
        st.session_state['userId'] =userName

    else:
        st.session_state["loggedIn"] = False
        st.error("Invalid username or password")


def show_login_page():
  st.title("What ToDo.")
  st.header(": to make the best out of today")
  menu = ["Login", "Sign Up"]
  choice = st.sidebar.selectbox("Menu", menu)
  if choice == "Login":
    with loginSection:
      if not st.session_state['loggedIn']:
          userName = st.text_input(label = "", value ="", placeholder =
          "Enter your user name")
          password = st.text_input(label="", value="", placeholder=
          "Enter your password", type = "password")
          st.button("Login", key = "login", on_click = lambda:
          LoggedIn_Clicked(userName, password))

  if choice == "Sign Up":
    with signupSection:
      if st.session_state['loggedIn'] == False:
          userName = st.text_input(label = "", value ="", placeholder =
          "Enter your new user name")
          password = st.text_input(label="", value="", placeholder=
          "Enter your new password", type = "password")
          st.button("Signup", key = "signup", on_click = lambda:
          signed_up_Clicked(userName, password))





def main():

    st.title("My Tasks")
    menu = ["Create", "Read", "Update", "Delete", "About"]
    userId = st.session_state['userId']
    choice = st.sidebar.selectbox("Menu", menu)

    create_user_table()
    if choice == "Create":
        st.subheader("Add Item")

        # Layout
        col1,col2 = st.columns(2)

        with col1:
          task = st.text_area("Task To Do")

        with col2:
          task_status = st.selectbox("Status", ["To Do", "Doing", "Done"])
          task_due_date = st.date_input("Due Date")


        if st.button("Add Task"):
          add_tasks(userId, task, task_status, task_due_date)
          st.success("Successfully Added Task: {}".format(task))
          st.balloons()




    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_tasks(userId)
        st.write(result)
        with st.expander("View All"):
			      clean_df = pd.DataFrame(result,columns=["Task", "Status", "Due Date"])
			      st.dataframe(clean_df)

        with st.expander("Task Status"):
          task_df = clean_df['Status'].value_counts().to_frame()
          task_df = task_df.reset_index()
          st.dataframe(task_df)

          p1 = px.pie(task_df, names = task_df.index, values = 'Status')
          st.plotly_chart(p1,use_container_width=True)


    elif choice == "Update":
        st.subheader("Edit Items")
        with st.expander("Current Tasks"):
          result = view_all_tasks(userId)
          # st.write(result)
          clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
          st.dataframe(clean_df)


          list_of_tasks = [i[0] for i in view_unique_tasks()]

          selected_task = st.selectbox("Task to Edit", list_of_tasks)

          selected_result = get_task(selected_task, userId)
          st.write(selected_result)

          if selected_result:
            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]


            # Layout
            col1, col2 = st.columns(2)

            with col1:
              new_task = st.text_area("Task To Do", task)

            with col2:
              new_task_status = st.selectbox(task_status, ["To Do", "Doing",
                                                           "Done"])
              new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task"):
              edit_task_data(new_task, new_task_status, new_task_due_date, task,
                             task_status, task_due_date, userId)
              st.success("Successfully Updated {} to {}".format(task, new_task))

        with st.expander("View Updated Data"):
          result = view_all_tasks(userId)
          # st.write(result)
          clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
          st.dataframe(clean_df)


    elif choice == "Delete":
        st.subheader("Delete Item")
        result = view_all_tasks(userId)
        df = pd.DataFrame(result, columns = ['Task', 'Status', 'Due Date'])
        with st.expander("Current Data"):
          st.dataframe(df)

        list_of_tasks = [i[0] for i in view_unique_tasks()]

        selected_task = st.selectbox("Task to Delete", list_of_tasks)
        st.warning("Do you want to delete {}?".format(selected_task))
        if st.button("Delete Task"):
          delete_task(selected_task, userId)
          st.write(f"{selected_task} has been successfully deleted.")

        new_result = view_all_tasks(userId)
        df2 = pd.DataFrame(new_result, columns=['Task', 'Status', 'Due Date'])
        with st.expander("Updated Data"):
          st.dataframe(df2)

    else:
      st.subheader("About What ToDo")
      st.info("Built with Streamlit")
      st.info("Created by: Yura Heo")



    


with headerSection:
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 


    else:
        if st.session_state['loggedIn']:
            show_logout_page()
            main()
        else:
            show_login_page()





