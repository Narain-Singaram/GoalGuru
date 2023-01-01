import builtins
import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import plotly.express as px

st.set_page_config(page_title='Qatar WC 2022', page_icon = '🏆')

st.title("🏆 Fifa World Cup 2022")

# Define a dictionary that maps country names to emojis
country_emoji_map = {
    "ARGENTINA": "🇦🇷",
    "AUSTRALIA": "🇦🇺",
    "BELGIUM": "🇧🇪",
    "BRAZIL": "🇧🇷",
    "CAMEROON": "🇨🇲",
    "CANADA": "🇨🇦",
    "COSTA RICA": "🇨🇷",
    "CROATIA": "🇭🇷",
    "DENMARK": "🇩🇰",
    "ECUADOR": "🇪🇨",
    "ENGLAND": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "FRANCE": "🇫🇷",
    "GERMANY": "🇩🇪",
    "GHANA": "🇬🇭",
    "IRAN": "🇮🇷",
    "JAPAN": "🇯🇵",
    "KOREA REPUBLIC": "🇰🇷",
    "MEXICO": "🇲🇽",
    "MOROCCO": "🇲🇦",
    "NETHERLANDS": "🇳🇱",
    "POLAND": "🇵🇱",
    "PORTUGAL": "🇵🇹",
    "QATAR": "🇶🇦",
    "SAUDI ARABIA": "🇸🇦",
    "SENEGAL": "🇸🇳",
    "SERBIA": "🇷🇸",
    "SPAIN": "🇪🇸",
    "SWITZERLAND": "🇨🇭",
    "TUNISIA": "🇹🇳",
    "UNITED STATES": "🇺🇸",
    "URUGUAY": "🇺🇾",
    "WALES": "🏴󠁧󠁢󠁷󠁬󠁳󠁿",
}

# Display the multiselect widget
first_second_team = st.multiselect("Select 2 teams from a match in the Fifa World Cup Qatar 2022 by the offical match name.", list(country_emoji_map.keys()), key="teams", max_selections=2)

st.caption("So it would be **:green[Argentina Vs. Saudi Arabia]** not **:red[Saudi Arabia vs Argentina]**")

df = pd.read_csv("Fifa_world_cup_matches.csv")

if first_second_team != []:

    results = df.loc[((df['team1'] == first_second_team[0]) & (df['team2'] == first_second_team[1]))]

    t_1_emoji = country_emoji_map[first_second_team[0]]
    t_2_emoji = country_emoji_map[first_second_team[1]]

    t_1 = first_second_team[0].title()
    t_2 = first_second_team[1].title()

    try:
        print("nothing")
    except IndexError:
        st.write("No rows were found in the results dataframe")

    tab1, tab2, tab3 = st.tabs(["Game Possession", "Attempts", "Owl"])

    with tab1:
        t1_possession = results.at[results.index[0], "possession team1"]
        t2_possession = results.at[results.index[0], "possession team2"]
        in_contest_possession = results.at[results.index[0], "possession in contest"]

        t1_possession = t1_possession.replace("%", "")
        t2_possession = t2_possession.replace("%", "")
        in_contest_possession = in_contest_possession.replace("%", "")

        options = {
            "title": {
                "text": f"Possession between {t_1_emoji} {t_1} and {t_2_emoji} {t_2}",
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

    with tab2:
        st.header(f"Attempts between {t_1_emoji} {t_1} & {t_2_emoji} {t_2}")
        total_attempts = [
            results.at[results.index[0], "total attempts team1"],
            results.at[results.index[0], "total attempts team2"],
        ]
        on_target_attempts = [
            results.at[results.index[0], "on target attempts team1"],
            results.at[results.index[0], "on target attempts team2"],
        ]
        off_target_attempts = [
            results.at[results.index[0], "off target attempts team1"],
            results.at[results.index[0], "off target attempts team2"],
        ]
        inside_penalty_area_attempts = [
            results.at[results.index[0], "attempts inside the penalty area team1"],
            results.at[results.index[0], "attempts inside the penalty area  team2"],
        ]
        outside_penalty_area_attempts = [
            results.at[results.index[0], "attempts outside the penalty area  team1"],
            results.at[results.index[0], "attempts outside the penalty area  team2"],
        ]

        st.subheader("Total Attempts")

        team1_total_attempts_col, team2_total_attempts_col = st.columns(2)

        team1_total_attempts_col.metric(label=f"Total Attempts - {t_1_emoji} {t_1}", value=f"{total_attempts[0]}", delta=f"{total_attempts[0] - total_attempts[1]}")
        team2_total_attempts_col.metric(label=f"Total Attempts - {t_2_emoji} {t_2}", value=f"{total_attempts[1]}", delta=f"{total_attempts[1] - total_attempts[0]}")

        team1_total_attempts_col.success(f'{on_target_attempts[0]} of these attempts were on target', icon=f"{t_1_emoji}")
        team2_total_attempts_col.success(f'{on_target_attempts[1]} of these attempts were on target', icon=f"{t_2_emoji}️")

        team1_total_attempts_col.error(f'{off_target_attempts[0]} of these attempts were off target', icon=f"{t_1_emoji}")
        team2_total_attempts_col.error(f'{off_target_attempts[1]} of these attempts were off target', icon=f"{t_2_emoji}")

        team1_total_attempts_col.info(f'{inside_penalty_area_attempts[0]} '
                                      f'of these attempts were inside of the penalty area', icon=f"{t_1_emoji}")
        team2_total_attempts_col.info(f'{inside_penalty_area_attempts[1]} '
                                      f'of these attempts were inside of the penalty area', icon=f"{t_2_emoji}")

        team1_total_attempts_col.info(f'{outside_penalty_area_attempts[0]} '
                                      f'of these attempts were outside of the penalty area', icon=f"{t_1_emoji}")
        team2_total_attempts_col.info(f'{outside_penalty_area_attempts[1]} '
                                      f'of these attempts were outside of the penalty area', icon=f"{t_2_emoji}")

        st.caption("Some attempts can be within multiple categories. "
                 "For example, a attempt could be inside the penalty area and could be off target.")
