import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data

col1 = st.text_input(label="Place", key="City")
city = col1

col2 = st.slider(label="Forecast Days", min_value=1, max_value=5, key="Days", help="Select the number of days to view")
days = col2

col3 = st.selectbox(label="Select Data to View", options=('Temperatures', 'Sky'), key="Data",
                    placeholder="Choose an option", disabled=False, label_visibility="visible")
option = col3
col4 = st.subheader(f"{option}  Forecast in  {city}  for the Next {days} Days ")

if city:
    try:
        if option == 'Temperatures':
            data = [i['main']['temp'] / 10 for i in get_data(city, days)]
            date = [i['dt_txt'] for i in get_data(city, days)]

            figure = px.line(x=date, y=data, labels={"x": "Date", "y": "Temperature (C)"})

            col5 = st.plotly_chart(figure)

        if option == 'Sky':
            datas = [i['weather'][0]['main'] for i in get_data(city, days)]
            dates = [i['dt_txt'] for i in get_data(city, days)]
            dicts = []
            for data in datas:
                if data == "Clear":
                    dicts.append('images/clear.png')
                if data == "Clouds":
                    dicts.append('images/cloud.png')
                if data == "Rain":
                    dicts.append('images/rain.png')
                if data == "Snow":
                    dicts.append('images/snow.png')

            rest = dict(map(lambda i,j : (i,j) , dates,dicts))
            rest = list(rest.items())
            print(rest)
            col6, col7, col8, col9, col10 = st.columns(5)
            with col6:
                   res8_list= rest[:8]
                   rest8_dict = dict(res8_list)
                   for k in rest8_dict:
                    st.image(rest8_dict[k])
                    st.write(k)

            with col7:
                res16_list = rest[8:16]
                rest16_dict = dict(res16_list)
                for k in rest16_dict:
                    st.image(rest16_dict[k])
                    st.write(k)

            with col8:
                res24_list = rest[16:24]
                rest24_dict = dict(res24_list)
                for k in rest24_dict:
                    st.image(rest24_dict[k])
                    st.write(k)
            with col9:
                res32_list = rest[24:32]
                rest32_dict = dict(res32_list)
                for k in rest32_dict:
                    st.image(rest32_dict[k])
                    st.write(k)
            with col10:
                res40_list = rest[32:40]
                rest40_dict = dict(res40_list)
                for k in rest40_dict:
                    st.image(rest40_dict[k])
                    st.write(k)
    except KeyError:
        st.write("City does not exist in the database")
#
#             with col10:
#                 for k in dicts[32:40]:
#                     st.image(k)
#                 # st.write(k)
#     except KeyError:
#         st.write( "City does not exist in the database")
#
# # image = Image.open('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80')
#
col11 = st.image(   "https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",
)
