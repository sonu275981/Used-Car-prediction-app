import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsRegressor

model = pickle.load(open("old_car.pkl", "rb"))  # here wb means read binary

st.title('Used Car prediction')
from PIL import Image
image = Image.open('car_pic.jpg')
st.image(image)

form = st.form(key='my_form')

year = form.number_input('Insert a Year of Manufacture', min_value=1996, max_value=2020, value=2007)

transmission = form.selectbox('Selected your Transmission',
                            ('Manual', 'Automatic', 'Semi-Auto'))
#st.write('You selected:', transmission)
if (transmission == 'Manual'):
    transmission = 0
elif (transmission == 'Automatic'):
    transmission = 1
else:
    transmission = 2

mileage = form.number_input('Insert a mileage (Kilometer Runs)', min_value=1, max_value=177644, value=19470)

fuelType = form.selectbox('Selected your FuelType',
                        ('Petrol', 'Diesel', 'Hybrid', 'Electric', 'Other'))
#st.write('You selected:', fuelType)
if (fuelType == 'Petrol'):
    fuelType = 0
elif (fuelType == 'Diesel'):
    fuelType = 1
elif (fuelType == 'Hybrid'):
    fuelType = 2
elif (fuelType == 'Electric'):
    fuelType = 3
else:
    fuelType = 4

mpg = form.number_input('Insert a mpg (Miles per gallon)', min_value=20.8, max_value=201.8, value=28.8)

value = (model.predict(np.array([[year, transmission, mileage, fuelType, mpg]])))
value=round(value[0],2)

st.header(f"Your requested car price is {value} US Dollor")
submit_button = form.form_submit_button(label='Submit')

