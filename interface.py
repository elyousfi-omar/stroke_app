from pyexpat import model
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.sidebar.header("Informations about the client :")
st.title("Stroke predicition")

st.header("Wijdane Bijou")
st.subheader("Master Sciences des données et systèmes intelligents")

marriage = st.sidebar.radio("Ever married?", ["Yes", "No"])

gender = st.sidebar.selectbox("Gender", ["Female", "Male"])

age = st.sidebar.number_input("Age")

tension = st.sidebar.radio("hypertension", ["Yes", "No"])

disease = st.sidebar.radio("heart disease", ["Yes", "No"])

work = st.sidebar.selectbox("Work type", ["Private", "Self-employed", "Never worked", "Govt_job"])

residence = st.sidebar.radio("Residence type", ["Urban", 'Rural'])

glocuse = st.sidebar.slider("Glocuse level", 50, 300)

bmi = st.sidebar.slider("Body Mass", 0, 50)

smoking = st.sidebar.selectbox("Smoker?", ["formerly smoked", "never smoked", "smokes", "unknown"])

marriage_dict = {"No": 0, "Yes": 1}
gender_dict = {"Female": 0, "Male": 1}
tension_dict = {"No": 0, "Yes": 1}
disease_dict = {"No": 0, "Yes": 1}

prv, self_emp, never, govt = 0, 0 ,0 ,0

if work == "Private":
    prv = 1
elif work == "Self-employed":
    self_emp = 1
elif work == "Never worked":
    never = 1
else:
    govt = 1

residence_dict = {"Rural": 0, "Urban": 1}

unknown, form, never, smoke = 0, 0, 0 ,0

if smoking == "formerly smoked":
    form = 1
elif smoking == "never smoked":
    never = 1
elif smoking == "smokes":
    smoke = 1
elif smoking == "unknown":
    unknown = 1


@st.cache(suppress_st_warning=True)
def get_value(val, dict):
    for key,value in dict.items():
        if val == key:
            return value

data = {
    "marriage": marriage, 
    "gender": gender,
    "age": age,
    "tension": tension,
    "disease": disease,
    "work": [prv, self_emp, never, govt],
    "residence": residence, 
    "glocuse": glocuse, 
    "bmi": bmi,
    "smoking": [unknown, form, never, smoke]
    }

features = [
            get_value(gender, gender_dict), 
            age, 
            get_value(tension, tension_dict),
            get_value(disease, disease_dict),
            get_value(marriage, marriage_dict),
            data["work"][3],
            data["work"][2], 
            data["work"][0],
            data["work"][1],
            get_value(residence, residence_dict),
            glocuse,
            bmi,
            data["smoking"][0],
            data["smoking"][1], 
            data["smoking"][2],
            data["smoking"][3],
             ]

sample = np.array(features).reshape(1, -1)
if st.button("Predict"):
    st.write("Need a model")
    model = pickle.load(open('model_rf', 'rb'))
    prediction = model.predict(sample)
    if prediction[0] == 0:
        st.success("Congratulations, you are less likely to get a stroke")
    else:
        st.error("According to ur calculations, you are more likely to get a stroke! Please visit a doctor.")



        
    

