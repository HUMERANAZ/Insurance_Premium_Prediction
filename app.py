import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import pickle
import xgboost as xg
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


model = pickle.load(open('model.pkl','rb'))
encoder = pickle.load(open('target_encoder.pkl','rb'))
transformer = pickle.load(open('transformer.pkl','rb'))


st.title("Health Insurance Premium")
html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Enter details to get Quote of Health Insurance</h2>
    </div>
    """

st.markdown(html_temp,unsafe_allow_html=True)

age = st.text_input('Enter Age', "18")
age = int(age)

sex = st.selectbox(
    'Please select gender',
    ('male', 'female'))

    
bmi = st.text_input('Enter BMI', 18)
bmi = float(bmi)

children = st.selectbox(
    'Please select number of children ',
    (0,1,2,3,4,5))
children = int(children)


smoker = st.selectbox(
    'Please select smoker category ',
    ("yes","no"))
# smoker = encoder.transform(smoker)

region = st.selectbox(
    'Please select region ',
    ("southwest", "southeast", "northeast", "northwest"))


l = {
    'age' : age,
    'sex' : sex,
    'bmi' : bmi,
    'children' : children,
    'smoker' : smoker,
    'region' : region,
    }


df = pd.DataFrame(l, index=[0])

df['region'] = encoder.transform(df['region'])
df['sex'] = df['sex'].map({'male':1, 'female':0})
df['smoker'] = df['smoker'].map({'yes':1, 'no':0})

df = transformer.transform(df)

y_pred = model.predict(df)


if st.button("Get Quote"):
    
    st.header(f"{round(y_pred[0],2)} INR")