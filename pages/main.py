"""
Created on 7/17/2023

@author: yurah
"""

import streamlit as st


import pandas as pd
from db_fxn import create_table, add_tasks, view_all_tasks, \
  view_unique_tasks, get_task, edit_task_data, delete_task
import plotly.express as px

def main():
    st.set_page_config(page_title="My Tasks")
    st.title("My Tasks")
    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
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
          add_tasks(task, task_status, task_due_date)
          st.success("Successfully Added Task: {}".format(task))




    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_tasks()
        st.write(result)
        df = pd.DataFrame(result, columns=['Tasks', 'Status', 'Due Date'])
        with st.expander("View All Tasks"):
          st.dataframe(df)

        with st.expander("Task Status"):
          task_df = df['Status'].value_counts().to_frame()
          task_df = task_df.reset_index()
          st.dataframe(task_df)

          p1 = px.pie(task_df, names = 'index', values = 'Status')
          st.plotly_chart(p1)


    elif choice == "Update":
        st.subheader("Edit Items")
        with st.expander("Current Tasks"):
          result = view_all_tasks()
          # st.write(result)
          clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
          st.dataframe(clean_df)


          list_of_tasks = [i[0] for i in view_unique_tasks()]

          selected_task = st.selectbox("Task to Edit", list_of_tasks)

          selected_result = get_task(selected_task)
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
                             task_status, task_due_date)
              st.success("Successfully Updated {} to {}".format(task, new_task))

            with st.expander("View Updated Data"):
              result = view_all_tasks()
              # st.write(result)
              clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
              st.dataframe(clean_df)


    elif choice == "Delete":
        st.subheader("Delete Item")
        result = view_all_tasks()
        df = pd.DataFrame(result, columns = ['Task', 'Status', 'Due Date'])
        with st.expander("Current Data"):
          st.dataframe(df)

        list_of_tasks = [i[0] for i in view_unique_tasks()]

        selected_task = st.selectbox("Task to Delete", list_of_tasks)
        st.warning("Do you want to delete {}?".format(selected_task))
        if st.button("Delete Task"):
          delete_task(selected_task)
          st.warning("{} has been successfully deleted.", format(selected_task))

        new_result = view_all_tasks()
        df2 = pd.DataFrame(new_result, columns=['Task', 'Status', 'Due Date'])
        with st.expander("Updated Data"):
          st.dataframe(df2)

