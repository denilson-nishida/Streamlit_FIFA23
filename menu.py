import streamlit as st
#from streamlit_extras.app_logo import add_logo


def unauthenticated_menu():

    st.html("""
    <style>
      [alt=Logo] {
        
        width: 210px;
        height:100px;
      }
    </style>
    """)

    st.logo("./src/fifa.png")
    #st.sidebar.page_link("./home.py", label="Home", icon="🏠")
    #st.sidebar.page_link("pages/players.py", label="Players", icon="🏃‍♂️")
    #st.sidebar.page_link("pages/teams.py", label="Teams", icon="⚽")
  

# Classes proprias
def menu():
    unauthenticated_menu()
