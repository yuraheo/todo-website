"""
Created on 7/17/2023

@author: yurah
"""

import streamlit as st

def login():
    html_code = '''
       <iframe src="login.html" height="600" width="100%"></iframe>
       '''

    # JavaScript code for the iframe
    js_code = '''
       <iframe src="src/login.js" height="600" width="100%"></iframe>
       '''

    # Display the HTML and JavaScript iframes using st.markdown
    st.markdown(html_code, unsafe_allow_html=True)
    st.markdown(js_code, unsafe_allow_html=True)

