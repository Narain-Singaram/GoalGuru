import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import plotly.express as px

st.title("Fifa World Cup 2022")
first_second_team = st.multiselect("Select 2 teams from a match in the Fifa World Cup Qatar 2022", ('ARGENTINA', 'AUSTRALIA', 'BELGIUM', 'BRAZIL',
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
        in_contest_possession_value = results.at[results.index[0], "possession in contest"]
        st.write(team1_possession_value,team2_possession_value )

        options = {
            "title": {
                "text": f"Game Possession Between {first_second_team[0]} and {first_second_team[1]}",
                "left": "center"
            },
            "tooltip": {
                "trigger": "item"
            },
            "legend": {
                "orient": "vertical",
                "bottom": "bottom"
            },
            "series": [
                {
                    "name": "Access From",
                    "type": "pie",
                    "radius": "50%",
                    "data": [
                        {f"value": "46", "name": f"{first_second_team[0]}" },
                        {f"value": "50", "name": f"{first_second_team[1]}" },
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

