import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import plotly.express as px

st.title("Fifa World Cup 2022")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days")
first_second_team = st.multiselect("Select a team from the world cup", ('ARGENTINA', 'AUSTRALIA', 'BELGIUM', 'BRAZIL',
                                              'CAMEROON', 'CANADA', 'COSTA RICA', 'CROATIA',
                                              'DENMARK', 'ECUADOR', 'ENGLAND', 'FRANCE',
                                              'GERMANY', 'GHANA', 'IRAN', 'JAPAN',
                                              'KOREA REPUBLIC', 'MEXICO', 'MOROCCO', 'NETHERLANDS',
                                              'POLAND', 'PORTUGAL', 'QATAR', 'SAUDI ARABIA',
                                              'SENEGAL', 'SERBIA', 'SPAIN', 'SWITZERLAND',
                                              'TUNISIA', 'UNITED STATES', 'URUGUAY', 'WALES'), key="teams", max_selections=2)

df = pd.read_csv("Fifa_world_cup_matches.csv")

if first_second_team != []:

    results = df.loc[((df['team1'] == first_second_team[0]) & (df['team2'] == first_second_team[1]))
                | ((df['team1'] == first_second_team[1]) & (df['team2'] == first_second_team[0]))]

    try:
        print("nothing")
    except IndexError:
        st.write("No rows were found in the results dataframe")

    tab1, tab2, tab3 = st.tabs(["Game Possession", "Dog", "Owl"])

    with tab1:
        team1_possession_value = results.at[results.index[0], "possession team1"]
        team2_possession_value = results.at[results.index[0], "possession team2"]
        st.write(team1_possession_value,team2_possession_value )

        options = {
            "title": {
                "text": "Referer of a Website",
                "subtext": "Fake Data",
                "left": "center"
            },
            "tooltip": {
                "trigger": "item"
            },
            "legend": {
                "orient": "vertical",
                "left": "left"
            },
            "series": [
                {
                    "name": "Access From",
                    "type": "pie",
                    "radius": "50%",
                    "data": [
                        {f"value": "46", "name": "Search Engine" },
                        {f"value": "50", "name": "Direct" },
                        {f"value": "4", "name": "In Contest"}
                    ],
                    "emphasis": {
                        "itemStyle": {
                            "shadowBlur": "10",
                            "shadowOffsetX": "0",
                            "shadowColor": "rgba(0, 0, 0, 0.5)"
                        }
                    }
                }
            ]
        }
        st_echarts(options=options)

