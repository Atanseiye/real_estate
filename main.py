import streamlit as st
from process import wrangle, prediction
import pandas as pd


st.title("Real Estate Value Prediction App")

# Example options for the dropdown
type_option = ['Mini Flat', 'Bungalow', 'Terrace', 'Detached house', 'Semi-detached house']
type_of_house = st.selectbox('Select an option:', type_option)

# Boys Quarters
boys_option = ['Present', 'Absent']
boys_quarters = st.selectbox('Is Boy\'s quarters Available there?', boys_option)

# Density
density_option = ['High density', 'Medium density', 'Low density']
density = st.selectbox('What is the desity of the location', density_option)

condition_option = ['Very good', 'Good', 'Fair', 'Poor']
condition = st.selectbox('What is the condition of the place', condition_option)

# Ceiling
ceiling_optioin = ['Asbestos', 'Others', 'POP', 'PVC']
ceiling = st.selectbox('What type of ceiling is used', ceiling_optioin)

# Floor type
floor_option = ['Tiles', 'Others', 'Wooden', 'Marble', 'Cement screed']
floor = st.selectbox('What type of Floor is used', floor_option)

# Roof
roof_option = ['Corrugated Iron Sheet', 'Long Span Aluminium Roofing sheet', 'Aluminium Step Tiles Roofing Sheet', 'Others']
roof = st.selectbox('What type of roof is there', roof_option)

# Window
window_type = ['Glazed Aluminium Sliding Window', 'Casement', 'Others', 'Louvers Blade']
window = st.selectbox('What is thw window type', window_type)

# Painting
painting_type = ['Textcote Paint', 'Emulsion Paint', 'Gloss Paint', 'Satin Paint']
painting = st.selectbox('What type of paint is used', painting_type)

# Water
water_condition = ['Good', 'Fair', 'Bad']
water = st.selectbox('What is the water condition', water_condition)

# Electericity
electericity_condition = ['Very good', 'Good', 'Fair', 'Bad']
electricity = st.selectbox('What is the condition of the electricity', electericity_condition)

# Car park
car_park_available = ['Present', 'Not present']
is_carPark = st.selectbox('Car park avalability', car_park_available)

# Security
security_option = ['Gated estate', 'Private gate/fence', 'Street gate']
security = st.selectbox('What type of security is available', security_option)

building_size = st.text_input('What is the size of the building')
bedrooms = st.text_input('How many bedrooms are there')
age = st.text_input('What is the age of the property')
bathrooms = st.text_input('How many bathrooms are there')
toilets = st.text_input('How many toilets are there')

# ################################
#####  Preprocesses ###############
if st.button('Submit'):
    input_data = {
        'building_size': [building_size],
        'type': [type_of_house],
        'bedroom':[bedrooms],
        'age':[age],
        'bathrooms':[bathrooms],
        'toilets': [toilets],
        "Boy'squarter": [boys_quarters],
        'loc_density': [density],
        'condition': [condition],
        'Ceiling ': [ceiling],
        'Floor':[floor],
        'Electricity': [electricity],
        'Car_park': [is_carPark],
        'Security': [security],
        'Roof':[roof],
        'Painting': [painting],
        'Window ':[window],
        'water':[water]
    }

    # data = pd.DataFrame(input_data, index=False)
    data = pd.DataFrame(input_data)
    # data = data[list(input_data.keys())]
    proc_data = wrangle(data)
    prediction = prediction(proc_data)[0]
    if prediction < 0:
        prediction *= -1
        st.write(f'Given the data you have inputed, I\'m able to say that the value for this house is #{prediction[0]}')

    else:
        st.write(f'Given the data you have inputed, I\'m able to say that the value for this house is #{prediction[0]}')
    # print(data)



