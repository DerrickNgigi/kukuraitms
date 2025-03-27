import streamlit as st
import pandas as pd


# Title of the app
st.title("KURA CHECKPOINT SYSTEM")

# Sidebar
st.sidebar.header("Menu")
if st.sidebar.button("Apps"):
    st.sidebar.write("Navigate to Apps")
if st.sidebar.button("Settings"):
    st.sidebar.write("Navigate to Settings")

# Main content
st.markdown("---")

# Top Section: Title
st.subheader("KURA CHECKPOINT SYSTEM")

# Middle Section
col1, col2 = st.columns([4, 2])

with col1:
    # Video Stream Section
    # video_file = open("motion20.mp4", "rb")
    # video_bytes = video_file.read()
    st.video("https://youtu.be/WVSYqut7pLs", autoplay=True, loop=True)

with col2:
    # Lane Vehicle Count Sections
    st.subheader("Lane 1 Vehicle Count")
    lane1_data = {
        "Vehicle Type": ["Car", "Bus", "Lorry", "Motorbike", "Truck"],
        "Count": [2, 2, 2, 2, 2]
    }
    df_lane1 = pd.DataFrame(lane1_data)
    st.table(df_lane1)

    st.subheader("Lane 2 Vehicle Count")
    lane2_data = {
        "Vehicle Type": ["Car", "Bus", "Lorry", "Motorbike", "Truck"],
        "Count": [2, 2, 2, 2, 2]
    }
    df_lane2 = pd.DataFrame(lane2_data)
    st.table(df_lane2)

# Bottom Section
st.markdown("---")
col3, col4, col5 = st.columns([2, 2, 3])

with col3:
    st.subheader("Lane 1")
    # Image of car capture in Lane 1
    st.image("20221110165408702-0(KCV897Z)(0)(0)(0002102)(3)(05)(00)(Company).JPG", caption="Image of car capture in lane 1")

with col4:
    st.subheader("Lane 2")
    # Image of car capture in Lane 2
    st.image("20221110165403883-0(KBY343T)(0)(0)(0002102)(3)(08)(00)(Company).JPG", caption="Image of car capture in lane 2")

with col5:
    # Graph of Vehicle Count Over Time
    st.subheader("Vehicle Count Over Time")
    # Graph of Vehicle Count Over Time

    # Simulate data for the graph
    vehicle_types = ["Car", "Bus", "Lorry", "Motorbike", "Truck"]
    time_periods = ["Morning", "Afternoon", "Evening", "Night"]
    data = {
        "Time Period": time_periods,
        "Car": [5, 10, 8, 3],
        "Bus": [2, 4, 3, 1],
        "Lorry": [1, 3, 2, 1],
        "Motorbike": [8, 12, 10, 5],
        "Truck": [3, 6, 4, 2]
    }

    # Convert the data into a format suitable for st.line_chart()
    df_graph = pd.DataFrame(data).set_index("Time Period")

    # Display the line chart
st.line_chart(df_graph)

# Footer
st.markdown("---")
st.write("Made in collaboration with KURA & KU")