import streamlit as st

home_page = st.Page("homepage.py", title = "Home", icon= "🏠", default= True)

nfl_page = st.Page("sports/NFL.py", title="NFL", icon="🏈")
nba_page = st.Page("sports/NBA.py", title="NBA", icon="🏀")
nhl_page = st.Page("sports/NHL.py", title="NHL", icon="🏒")
mlb_page = st.Page("sports/MLB.py", title="MLB", icon="⚾")

nfl_calc_page = st.Page("calculations/NFL_calc.py", title="NFL Calculations", icon="🏈")
nba_calc_page = st.Page("calculations/NBA_calc.py", title="NBA Calculations", icon="🏀")
nhl_calc_page = st.Page("calculations/NHL_calc.py", title="NHL Calculations", icon="🏒")
mlb_calc_page = st.Page("calculations/MLB_calc.py", title="MLB Calculations", icon="⚾")

pg = st.navigation({"": [home_page], "Sports": [nfl_page, nba_page, nhl_page, mlb_page], 
                    "How We Calculate Lines": [nfl_calc_page, nba_calc_page, nhl_calc_page, mlb_calc_page]})


st.set_page_config(
    page_title = "LineMatch",
    page_icon = ":scales:",
    menu_items={
        'About' : '''**Developers:*** 
        [Rishabh Dwarakanath](https://github.com/rdwarakanath2022)'''
    },
    layout= "wide"
)

pg.run()
