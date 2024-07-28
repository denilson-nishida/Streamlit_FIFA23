import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='FIFA 23 | Players',
    layout='wide',
    page_icon="⚽"  
)

import menu
menu.menu()

df_data = st.session_state['data']

clubs = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Club', clubs)

df_players = df_data[df_data['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Player', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

st.markdown(f'**Club:** {player_stats["Club"]}')
st.markdown(f'**Position:** {player_stats["Position"]}')

col1, col2, col3, _, _ = st.columns(5)
col1.markdown(f'**Age:** {player_stats["Age"]}')
col2.markdown(f'**Height:** {player_stats["Height(cm.)"] / 100} m')
col3.markdown(f'**Weight:** {player_stats["Weight(lbs.)"] * 0.453:.1f} kg')
st.divider()

st.subheader(f'**Overall:** {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))

col1, col2, col3, _ = st.columns(4)
col1.metric(label='Market Value', value=f'£ {player_stats["Value(£)"]:,.0f}')
col2.metric(label='Wage', value=f'£ {player_stats["Wage(£)"]:,.0f}')
col3.metric(label='Release Clause', value=f'£ {player_stats["Release Clause(£)"]:,.0f}')
