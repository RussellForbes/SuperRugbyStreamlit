import numpy as np
import pandas as pd
import glob
import streamlit as st
import plotly.graph_objs as go
from plotly.subplots import make_subplots

grouped_df = pd.read_csv('grouped_df.csv')
minutes_df = pd.read_csv('minutes_df.csv')
# --------------------------------------------------------------------------------------------------------------------
team_list = minutes_df['Team'].unique().tolist()


st.set_page_config(page_title="2023 Super Rugby")
st.subheader('2023 Super Rugby Player Stats')

team_selection = st.selectbox('Team:', team_list)

team_players = minutes_df[minutes_df['Team'] == team_selection]['Player Name'].unique().tolist()

player_1_selection = st.selectbox('Player:', team_players)
single_player_df = grouped_df[grouped_df['Player Name'] == player_1_selection]
single_player_df = single_player_df.copy()
single_player_df['Y Position'] = np.random.uniform(-0.05, 0.05)
single_player_df['Y Zero'] = 0

#st.dataframe(grouped_df[grouped_df['Player Name'] == player_1_selection][
#                 ['Player Name', 'Tries', 'Metres carried', 'Carries', 'Defenders beaten', 'Clean breaks', 'Passes',
#                  'Offloads', 'Turnovers conceded',
#                  'Try assists', 'Points', 'Tackles', 'Missed tackles', 'Turnovers won', 'Kicks in play']])

# y_position_list = np.linspace(0, 0, len(grouped_df['Player Name']))
y_position_list = np.random.uniform(-0.05, 0.05, len(grouped_df['Player Name']))

fig = make_subplots(rows=6, cols=1)

# TRACE 1
fig.add_trace(go.Scatter(y=y_position_list, x=grouped_df['Tries per 80'],
                         hovertext=grouped_df['Player Name'] + " " + round(grouped_df['Tries per 80'],
                                                                           2).astype(str),
                         hoverinfo='text',
                         mode='markers',
                         marker=dict(color='grey', size=20, opacity=0.25)),
              row=2, col=1)

fig.add_trace(go.Scatter(y=single_player_df['Y Position'], x=single_player_df['Tries per 80'],
                         hovertext=single_player_df['Player Name'], hoverinfo='text',
                         mode='markers+text',
                         text=round(single_player_df['Tries per 80'].iloc[0], 1).astype(
                             str) + " Tries per 80",
                         textposition='top center',
                         marker=dict(color='aqua', size=20,
                                     line=dict(width=2,
                                               color='black')
                                     ),
                         textfont=dict(color='white')), row=2, col=1)

# TRACE 2
fig.add_trace(go.Scatter(y=y_position_list, x=grouped_df['Clean breaks per 80'],
                         hovertext=grouped_df['Player Name'] + " " + round(grouped_df['Clean breaks per 80'],
                                                                           1).astype(str),
                         hoverinfo='text',
                         mode='markers', marker=dict(color='grey', size=20, opacity=0.25)), row=3, col=1)

fig.add_trace(go.Scatter(y=single_player_df['Y Position'], x=single_player_df['Clean breaks per 80'],
                         hovertext=single_player_df['Player Name'],
                         hoverinfo='text',
                         mode='markers+text',
                         text=round(single_player_df['Clean breaks per 80'].iloc[0], 1).astype(
                             str) + " Clean breaks per 80",
                         textposition='top center',
                         marker=dict(color='aqua', size=20,line=dict(width=2,
                                               color='black')),
                         textfont=dict(color='white')), row=3, col=1)

# TRACE 3
fig.add_trace(go.Scatter(y=y_position_list, x=grouped_df['Metres carried per 80'],
                         hovertext=grouped_df['Player Name'] + " " + round(grouped_df['Metres carried per 80'],
                                                                           1).astype(str),
                         hoverinfo='text',
                         mode='markers',
                         text=round(single_player_df['Metres carried per 80'].iloc[0], 1).astype(str),
                         marker=dict(color='grey', size=20, opacity=0.25)), row=4, col=1)

fig.add_trace(go.Scatter(y=single_player_df['Y Position'], x=single_player_df['Metres carried per 80'],
                         hovertext=single_player_df['Player Name'], hoverinfo='text',
                         mode='markers+text',
                         text=round(single_player_df['Metres carried per 80'].iloc[0], 1).astype(
                             str) + " Metres carried per 80",
                         textposition='top center',
                         marker=dict(color='aqua', size=20,line=dict(width=2,
                                               color='black')),
                         textfont=dict(color='white')), row=4, col=1)


# TRACE 4
fig.add_trace(go.Scatter(y=y_position_list, x=grouped_df['Defenders beaten per 80'],
                         hovertext=grouped_df['Player Name'] + " " + round(grouped_df['Defenders beaten per 80'],
                                                                           1).astype(str),
                         hoverinfo='text',
                         mode='markers',
                         text=round(single_player_df['Defenders beaten per 80'].iloc[0], 1).astype(str),
                         marker=dict(color='grey', size=20, opacity=0.25)), row=5, col=1)

fig.add_trace(go.Scatter(y=single_player_df['Y Position'], x=single_player_df['Defenders beaten per 80'],
                         hovertext=single_player_df['Player Name'], hoverinfo='text',
                         mode='markers+text',
                         text=round(single_player_df['Defenders beaten per 80'].iloc[0], 1).astype(
                             str) + " Defenders beaten per 80",
                         textposition='top center',
                         marker=dict(color='aqua', size=20,line=dict(width=2,
                                               color='black')),
                         textfont=dict(color='white')), row=5, col=1)

fig.update_layout(
    showlegend=False,
    xaxis=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    xaxis2=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    xaxis3=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    xaxis4=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    yaxis=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    yaxis2=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    yaxis3=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    yaxis4=dict(
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
    title='Player Stats',
    height=800)

st.plotly_chart(fig)

