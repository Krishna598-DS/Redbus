import streamlit as st
import pandas as pd
import pymysql

# Set page configuration
st.set_page_config(page_title="Redbus Availability", layout="wide")

# Page Header
st.markdown(
    """
    <style>
        h1 {
            color: #007bff;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        h3 {
            color: #555;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
    """, 
    unsafe_allow_html=True
)
st.markdown("<h1>Redbus - Bus Availability Checker</h1>", unsafe_allow_html=True)
st.markdown("<h3>Find buses, filter by rating, price, and availability!</h3>", unsafe_allow_html=True)

# Database connection and data fetching
try:
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

            # Filters in the sidebar
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
                    # Show details of the selected bus
                    if st.button(f"Show {bus_selected} Bus Details"):
                        bus_details = filtered_buses[filtered_buses["busname"] == bus_selected][
                            ["bustype", "departing_time", "duration", "star_rating", "price"]
                        ]
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
