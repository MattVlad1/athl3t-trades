
import streamlit as st
import pandas as pd

# Load data
players = pd.read_csv("data/players.csv")
funds = pd.read_csv("data/team_funds.csv")
users = pd.read_csv("data/users.csv")
holdings = pd.read_csv("data/holdings.csv")

# Simulate current user
current_user_id = "user_001"
user_wallet = users.loc[users["User ID"] == current_user_id, "Wallet Balance"].values[0]

st.set_page_config(page_title="ATHL3T Trades", layout="wide")
st.title("ATHL3T Trades - NFL Market")

st.sidebar.header(f"Wallet Balance: ${user_wallet}")
st.sidebar.write("User: MattV")

# Market View
st.header("Player Market")
for _, row in players.iterrows():
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    with col1:
        st.markdown(f"**{row['Player Name']}** ({row['Team']}) - {row['Position']}")
    with col2:
        st.write(f"${row['Current Price']}")
    with col3:
        if st.button(f"Buy {row['Player Name']}", key=row['Player Name']):
            st.success(f"Bought 1 share of {row['Player Name']} (mock)")
    with col4:
        if st.button(f"Sell {row['Player Name']}", key=row['Player Name'] + "_sell"):
            st.warning(f"Sold 1 share of {row['Player Name']} (mock)")

# Team Funds
st.header("Team Funds")
for _, row in funds.iterrows():
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(f"**{row['Fund Name']}** - Includes: {row['Players Included']}")
    with col2:
        st.write(f"${row['Fund Price']}")
    with col3:
        if st.button(f"Buy {row['Fund Name']}", key=row['Fund Name']):
            st.success(f"Bought 1 share of {row['Fund Name']} (mock)")
