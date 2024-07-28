import streamlit as st
#from streamlit_extras.app_logo import add_logo


def unauthenticated_menu():

  st.logo("./src/fifa3.png")
  st.sidebar.page_link("1_home.py", label="Home", icon="🏠")
  st.sidebar.page_link("pages/2_players.py", label="Players", icon="🏃‍♂️")
  st.sidebar.page_link("pages/3_teams.py", label="Teams", icon="⚽")
  

# Classes proprias
def menu():
    unauthenticated_menu()

