import streamlit as st
import pandas as pd
import datetime
import requests
'''
# TaxiFareModel front
'''

st.markdown("""# Predict your fare amount""")

'''
### Please fill out the following fields:
'''
date_selector = st.date_input("Pick up date")
time_selector = st.time_input("Pick up time")
date_and_time_selector = datetime.datetime.combine(date_selector, time_selector)

pickup_lon = st.number_input("Pickup longitude", value=74.0060, min_value=-180., max_value=180.,step = 0.0001)
pickup_lat = st.number_input("Pickup latitude", value=40.7128, min_value=-90., max_value=90.,step = 0.0001)
dropoff_lon = st.number_input("Dropoff longitude", value=74.1, min_value=-180., max_value=180.,step = 0.0001)
dropoff_lat = st.number_input("Dropoff latitude", value=40.2, min_value=-90., max_value=90.,step = 0.0001)
option = st.selectbox('Nb of passengers?',(1,2,3,4,5,6,7,8))

st.write('Date and time', str(date_and_time_selector))
st.write('Pickup longitude', pickup_lon)
st.write('Pickup latitude', pickup_lat)
st.write('Dropoff longitude', dropoff_lon)
st.write('Dropoff latitude', dropoff_lat)
st.write('Nb of passengers?', option)

params = {
    'pickup_datetime': str(date_and_time_selector),
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': option,
}

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':
#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

#2. Let's build a dictionary containing the parameters for our API...

#3. Let's call our API using the `requests` package...
if st.button(label="Get fare"):
    response = requests.get(url, params=params).json()
    st.write(response["fare"])

#4. Let's retrieve the prediction from the **JSON** returned by the API...
