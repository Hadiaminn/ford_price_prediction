import streamlit as st
import pandas as pd
import pickle

st.write("""
# Ford Car Price Prediction App

This app predicts the **Price** for type of advertising stratergy!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    st.write('The Model are 0=B-MAX, 1=C-MAX, 2=EcoSport, 3=Edge, 4=Escort, 5=Fiesta, 6=Focus, 7=Fusion, 8=Galaxy, 9=Grand C-MAX, 10=Grand Tourneo Connect, 11=KA, 12=Ka+, 13=Kuga, 14=Mondeo,15=Mustang, 16=Puma, 17=Ranger, 18=S-MAX, 19=Streetka,20=Tourneo Connect, 21=Tourneo Custom, 22=Transit Tourneo')
    model = st.sidebar.selectbox ('Select car model',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])

    st.write('The Year are 0=1996, 1=1998, 2=2000, 3=2002, 4=2003, 5=2004, 6=2005, 7=2006, 8=2007, 9=2008, 10=2009, 11=2010, 12=2011, 13=2012, 14=2013,15=2014, 16=2015, 17=2016, 18=2017, 19=2018,20=2019, 21=2020')
    year = st.sidebar.selectbox ('Selec year of registration',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])

    st.write('The Transmission are 0=Automatic, 1=Manual, 2=Semi-Auto=')
    transmission = st.sidebar.selectbox ('Select transmission type',[0,1,2])

    st.write('The Fuel Type are 0=Diesel, 1=Electric, 2=Hybrid, 3=Other, 4=Petrol')
    fuelType = st.sidebar.selectbox ('Select transmission type',[0,1,2,3,4])
    engineSize = st.sidebar.slider('Engine Size', 0.0, 5.0, 1.0)
    mileage = st.sidebar.slider('Mileage', 1.0, 177644.0, 15.0)
    data = {
        'Model':model,
        'Year': year,
        'Transmission': transmission,
        'Fuel Type' : fuelType,
        'Engine Size': engineSize,
        'Mileage': mileage}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("ford_price_prediction_model.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

