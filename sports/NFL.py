import csv
import streamlit as st


st.title("🏈 NFL")
st.header("On Any Given Sunday... ", divider= 'orange')

a_team = st.text_input("Enter the Away Team", placeholder="Ex. Miami Dolphins, Kansas City Chiefs")

# Verify if away team has been inputted properly
with open('sports/teams.csv', "r") as file:
    reader = csv.reader(file)
    teams = [item[0] for item in reader]

if a_team:
    if a_team not in teams:
        st.error("Invalid Team Name")

# Verify if home team has been inputted properly
h_team = st.text_input("Enter the Home Team", placeholder="Ex. Miami Dolphins, Kansas City Chiefs")

with open('sports/teams.csv', "r") as file:
    reader = csv.reader(file)
    teams = [item[0] for item in reader]

if h_team:
    if h_team not in teams:
        st.error("Invalid Team Name")

a_qb = st.text_input("Enter the Away Starting QB", placeholder="Ex. Tua Tagovailoa, Patrick Mahomes")

# Verify if away QB has been inputted properly
with open('sports/qbs.csv', "r") as file:
    reader = csv.reader(file)
    qbs = [item[0] for item in reader]

if a_qb:
    if a_qb not in qbs:
        st.error("Invalid QB Name")

h_qb = st.text_input("Enter the Home Starting QB", placeholder="Ex. Tua Tagovailoa, Patrick Mahomes")

# Verify if home QB has been inputted properly
with open('sports/qbs.csv', "r") as file:
    reader = csv.reader(file)
    qbs = [item[0] for item in reader]

if h_qb:
    if h_qb not in qbs:
        st.error("Invalid QB Name")

# Button CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: green;
        color: white;
    }
    .stButton>button:active {
        background-color: white;
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a layout with three columns and place the button in the center column
col1, col2, col3 = st.columns([1, 0.5, 1])

with col2:
    calculate_button = st.button("Calculate Lines")



def awayPointsProjection(away_team, home_team, away_qb):
    # away team points per game (E3)
    with open('sports/ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == away_team:
                away_ppg = item[2]
    # away team points per game in the last 3 games (F3)
    with open('sports/ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == away_team:
                away_ppg_l3 = item[3]
    # home team allowed points (K3)
    with open('sports/opp_ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == home_team:
                home_allowed_points = item[2]
    # home team allowed points in the last 3 games (L3)
    with open('sports/opp_ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == home_team:
                home_allowed_points_l3 = item[3]   
    # away QBR (M3)
    with open('sports/qbr.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[0] == away_qb:
                away_qbr = item[2]
    
    projection = (float(away_ppg) + float(away_ppg_l3) + float(home_allowed_points) + float(home_allowed_points_l3) + float(away_qbr)) / 5
    
    return projection


def homePointsProjection(home_team, away_team, home_qb):
    # home team points per game (G3)
    with open('sports/ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == home_team:
                home_ppg = item[2]
    # home team points per game in the last 3 games (H3)
    with open('sports/ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == home_team:
                home_ppg_l3 = item[3]
    # away team allowed points (I3)
    with open('sports/opp_ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == away_team:
                away_allowed_points = item[2]
    # away team allowed points in the last 3 games (J3)
    with open('sports/opp_ppg.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] == away_team:
                away_allowed_points_l3 = item[3]   
    # home QBR (N3)
    with open('sports/qbr.csv', "r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[0] == home_qb:
                home_qbr = item[2]
    
    projection = (float(home_ppg) + float(home_ppg_l3) + float(away_allowed_points) + float(away_allowed_points_l3) + float(home_qbr)) / 5
    
    return projection


def totalPointsProjection():
    away = awayPointsProjection(a_team, h_team, a_qb)
    home = homePointsProjection(h_team, a_team, h_qb)

    return away + home


def pointsSpreadProjection():
    away = awayPointsProjection(a_team, h_team, a_qb)
    home = homePointsProjection(h_team, a_team, h_qb)

    return away - home



# Handle button click
if calculate_button:
    st.write('Calculating lines...')
    st.write(awayPointsProjection(a_team, h_team, a_qb))
    st.write(homePointsProjection(h_team, a_team, h_qb))
    st.write(totalPointsProjection())
    st.write(pointsSpreadProjection())



