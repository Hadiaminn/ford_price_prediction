import streamlit as st
import pandas as pd
import pickle

# Dictionary to map displayed year values to encoded values
year_mapping = {
    '1996': 0, '1998': 1, '2000': 2, '2002': 3, '2003': 4, '2004': 5,
    '2005': 6, '2006': 7, '2007': 8, '2008': 9, '2009': 10, '2010': 11,
    '2011': 12, '2012': 13, '2013': 14, '2014': 15, '2015': 16, '2016': 17,
    '2017': 18, '2018': 19, '2019': 20, '2020': 21}

# Dictionary to map displayed model names to encoded values
model_mapping = {
    'B-MAX': 0, 'C-MAX': 1, 'EcoSport': 2, 'Edge': 3, 'Escort': 4, 'Fiesta': 5,
    'Focus': 6, 'Fusion': 7, 'Galaxy': 8, 'Grand C-MAX': 9, 'Grand Tourneo Connect': 10,
    'KA': 11, 'Ka+': 12, 'Kuga': 13, 'Mondeo': 14, 'Mustang': 15, 'Puma': 16,
    'Ranger': 17, 'S-MAX': 18, 'Streetka': 19, 'Tourneo Connect': 20, 'Tourneo Custom': 21,
    'Transit Tourneo': 22
}

# Dictionary to map displayed transmission names to encoded values
transmission_mapping = {
    'Automatic':0, 'Manual':1, 'Semi-Automatic':2}

# Dictionary to map displayed fuel names to encoded values
fuelType_mapping = {
    'Diesel':0, 'Electric':1, 'Hybrid':2, 'Other':3, 'Petrol':4}

st.write("""
# Ford Car Price Prediction App

This app predicts the **Price** for type of advertising stratergy!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    #st.write('The Model are 0=B-MAX, 1=C-MAX, 2=EcoSport, 3=Edge, 4=Escort, 5=Fiesta, 6=Focus, 7=Fusion, 8=Galaxy, 9=Grand C-MAX, 10=Grand Tourneo Connect, 11=KA, 12=Ka+, 13=Kuga, 14=Mondeo,15=Mustang, 16=Puma, 17=Ranger, 18=S-MAX, 19=Streetka,20=Tourneo Connect, 21=Tourneo Custom, 22=Transit Tourneo')
    model = st.sidebar.selectbox ('Select car model',list(model_mapping.keys()))

    #st.write('The Year are 0=1996, 1=1998, 2=2000, 3=2002, 4=2003, 5=2004, 6=2005, 7=2006, 8=2007, 9=2008, 10=2009, 11=2010, 12=2011, 13=2012, 14=2013,15=2014, 16=2015, 17=2016, 18=2017, 19=2018,20=2019, 21=2020')
    year = st.sidebar.selectbox ('Selec year of registration',list(year_mapping.keys()))
    
    #st.write('The Transmission are 0=Automatic, 1=Manual, 2=Semi-Auto=')
    transmission = st.sidebar.selectbox ('Select transmission type',list(transmission_mapping.keys()))

    mileage = st.sidebar.slider('Mileage', 1.0, 177644.0, 15.0)
    
    #st.write('The Fuel Type are 0=Diesel, 1=Electric, 2=Hybrid, 3=Other, 4=Petrol')
    fuelType = st.sidebar.selectbox ('Select Fuel type',list(fuelType_mapping.keys()))
    
    engineSize = st.sidebar.slider('Engine Size', 0.0, 5.0, 1.0)
    
    data = {
        'model':model,
        'year': year,
        'transmission': transmission,
        'mileage': mileage,
        'fuelType' : fuelType,
        'engineSize': engineSize
        }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("ford_price_prediction_unscale_model.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

