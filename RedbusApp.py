import streamlit as st
import pandas as pd
import pymysql

# Set page configuration
st.set_page_config(page_title="Redbus Availability Checker", layout="wide")

# Custom CSS for background, fonts, and overall styling
st.markdown(
    """
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Arial', sans-serif;
            color: #212529;
        }
        .main {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007bff;
            font-size: 3rem;
            text-align: center;
            font-family: 'Georgia', serif;
        }
        h3 {
            color: #6c757d;
            text-align: center;
            font-size: 1.5rem;
        }
        .stButton button {
            background-color: #007bff !important;
            color: white !important;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 1rem;
        }
        .sidebar .stRadio > label {
            font-size: 1rem;
            font-weight: bold;
            color: #495057;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.markdown("<h1>Redbus - Bus Availability Checker</h1>", unsafe_allow_html=True)
st.markdown("<h3>Find your ideal bus with ease and comfort!</h3>", unsafe_allow_html=True)

# App Content
with st.container():
    try:
        # Connect to the database
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="123456789",  # Update with your database password
            database="Redbus"      # Update with your database name
        )
        mycursor = mydb.cursor()

        # Fetch data from the database
        mycursor.execute("SELECT * FROM bus_routes")
        data = mycursor.fetchall()
        columns = [desc[0] for desc in mycursor.description]
        table = pd.DataFrame(data, columns=columns)

        # State selection
        statelist = table["state"].unique().tolist()
        statelist = ["Choose your state"] + statelist
        selected_state = st.selectbox("Select Your State", statelist)

        if selected_state != "Choose your state":
            # Route selection
            routes = table[table["state"] == selected_state]["route_name"].unique().tolist()
            route_selected = st.selectbox("Select Your Route", ["Choose your desired route"] + routes)

            if route_selected != "Choose your desired route":
                st.sidebar.markdown("<h3 style='color: maroon;'>Filter Options</h3>", unsafe_allow_html=True)

                # Sidebar filters
                rating = st.sidebar.radio(
                    "Star Rating",
                    options=[5, 4, 3, 2, 1],
                    format_func=lambda x: "⭐" * x,
                    horizontal=True
                )
                max_price = st.sidebar.slider("Max Ticket Price (INR)", 100, 10000, step=100, value=5000)
                seats = st.sidebar.number_input("Seats Required", min_value=1, max_value=57, value=1)

                # Filter buses based on user input
                filtered_buses = table[
                    (table["route_name"] == route_selected) &
                    (table["star_rating"] >= rating) &
                    (table["price"] <= max_price) &
                    (table["seats_available"] >= seats)
                ]

                if not filtered_buses.empty:
                    # Show available buses
                    bus_names = filtered_buses["busname"].unique().tolist()
                    bus_selected = st.radio("Available Buses", bus_names)

                    if bus_selected:
                        if st.button(f"Show {bus_selected} Bus Details"):
                            # Select relevant details
                            bus_details = filtered_buses[filtered_buses["busname"] == bus_selected][
                                ["bustype", "departing_time", "reaching_time", "duration", "star_rating", "price", "seats_available"]
                            ]

                            # Reset index to start from 1
                            bus_details.reset_index(drop=True, inplace=True)
                            bus_details.index += 1

                            # Format times to display only hours and minutes
                            bus_details["departing_time"] = pd.to_datetime(bus_details["departing_time"]).dt.strftime('%H:%M')
                            bus_details["reaching_time"] = pd.to_datetime(bus_details["reaching_time"]).dt.strftime('%H:%M')

                            # Remove trailing decimals
                            bus_details["star_rating"] = bus_details["star_rating"].map('{:.0f}'.format)
                            bus_details["price"] = bus_details["price"].map('{:.0f}'.format)
                            bus_details["seats_available"] = bus_details["seats_available"].map('{:.0f}'.format)

                            # Rename columns for display
                            bus_details.rename(columns={
                                "bustype": "Bus Type",
                                "departing_time": "Departing Time",
                                "reaching_time": "Arrival Time",
                                "duration": "Duration",
                                "star_rating": "Star Rating",
                                "price": "Price",
                                "seats_available": "Seats Available"
                            }, inplace=True)

                            st.markdown("<h3>Bus Details:</h3>", unsafe_allow_html=True)
                            st.table(bus_details)
                else:
                    st.warning("No buses found for the selected filters. Please try adjusting the filters.")
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
    finally:
        if 'mycursor' in locals():
            mycursor.close()
        if 'mydb' in locals():
            mydb.close()

# Footer
st.markdown(
    """
    <hr>
    <div style='text-align: center; color: gray;'>
        <small>Powered by Redbus Data Scraping | © 2024</small>
    </div>
    """,
    unsafe_allow_html=True
)
