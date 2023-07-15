# from flask import Flask, render_template
# import streamlit as st
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#   return render_template('home.html')


# @app.route('/main')
# def main():
#   st.title("My Tasks")
#   menu = ["Create", "Read", "Update", "Delete", "About"]
#   choice = st.sidebar.selectbox("Menu", menu)

#   if choice == "Create":
#     st.subheader("Add Item")

#   elif choice == "Read":
#     st.subheader("View Items")

#   elif choice == "Update":
#     st.subheader("Edit/Update Items")

#   elif choice == "Delete":
#     st.subheader("Delete Item")


# return render_template('main.html')

# import db

# db.init_app(app)

# import auth

# app.register_blueprint(auth.bp)

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', debug=True)
#   main()

