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
        t1_possession = results.at[results.index[0], "possession team1"]
        t2_possession = results.at[results.index[0], "possession team2"]
        in_contest_possession = results.at[results.index[0], "possession in contest"]

        t1_possession = t1_possession.replace("%", "")
        t2_possession = t2_possession.replace("%", "")
        in_contest_possession = in_contest_possession.replace("%", "")

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
                        {"value": f"{t1_possession}", "name": f"{first_second_team[0]}"},
                        {"value": f"{t2_possession}", "name": f"{first_second_team[1]}"},
                        {"value": f"{in_contest_possession}", "name": "In Contest"}
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

