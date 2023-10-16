import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

col1 = st.text_input(label="Place", key="City")
city = col1

col2 = st.slider(label="Forecast Days", min_value=1, max_value=5, key="Days", help="Select the number of days to view")
days = col2

col3 = st.selectbox(label="Select Data to View", options=('Temperatures', 'Sky'), key="Data",
                    placeholder="Choose an option", disabled=False, label_visibility="visible")
option = col3
col4 = st.subheader(f"{option}  Forecast in  {city}  for the Next {days} Days ")


def get_date(days):
    dates = ["2023-10-16", "2023-10-17", "2023-10-18"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]

    return dates, temperatures


d, t = get_date(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})

col5 = st.plotly_chart(figure)


# image = Image.open('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80')

col5 = st.image(
    "https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",

)
