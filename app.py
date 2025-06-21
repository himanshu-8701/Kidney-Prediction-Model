import numpy as np
import pickle
import pandas as pd
import streamlit as st 

import os

model = pickle.load(open('kidney.pkl','rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

rep = {'abnormal': 1, 'normal': 0, 'present': 1, 'notpresent': 0, 'yes': 1, 'no': 0, 'good': 1, "poor":0}

def welcome():
    return "  Welcome to Chronic Kidney Disease Detection "

def main():
    st.title("  ")
    html_temp = """

    <div style="background-color:brown;padding:10px;border: 2px solid blue;">
    <h2 style="color:white;text-align:center;color:yellow;text-transform: uppercase;"> Welcome to Kidney Disease Detection </h2>
    </div>
    """
    
    

    # st.sidebar.title("Kidney Disease Detection ")

    st.markdown(html_temp,unsafe_allow_html=True)

    age = st.slider("Select Age")
    if not age:
        st.warning('Please enter your age!')
        
    blood_pressure = st.slider('Select Blood Pressure',10,300)
    red_blood_cells = st.radio('Red Blood Cells',['normal','abnormal'])
    pus_cell = st.radio('Pus Cell',['normal','abnormal'])
    pus_cell_clumps = st.radio('Pus Cell Clumps',['present','notpresent'])
    bacteria = st.radio('Bacteria',['present','notpresent'])
    hypertension = st.radio('Hypertension',['yes','no'])
    diabetes_mellitus = st.radio('Diabetes Mellitus',['yes','no'])
    coronary_artery_disease = st.radio('Coronary Artery Disease',['yes','no'])
    appetite = st.radio('Appetite',['good','poor'])
    peda_edema = st.radio('Peda Edema',['yes','no'])
    aanemia = st.radio('Aanemia',['yes','no'])
    albumin = st.number_input('Albumin')
    specific_gravity = st.number_input('Specific Gravity')
    sugar = st.number_input('Sugar')
    blood_glucose_random = st.number_input('Blood Glucose Random')
    blood_urea = st.number_input('Blood Urea')
    serum_creatinine = st.number_input('Serum Creatinine')
    sodium = st.number_input('Sodium')
    potassium = st.number_input('Potassium')
    haemoglobin = st.number_input('Haemoglobin')
    packed_cell_volume = st.number_input('Packed Cell Volume')
    white_blood_cell_count = st.number_input('White Blood Cell Count')
    red_blood_cell_count = st.number_input('Red Blood Cell Count')
        
    if st.button("Get Result"):
        
        inp_dat = [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]
        j = 0
        for i in inp_dat:
            if i in rep.keys(): 
                inp_dat[j] = rep[i]
            j+=1
        
        trans_dat = pd.DataFrame(columns=['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar',
                'red_blood_cells', 'pus_cell', 'pus_cell_clumps', 'bacteria',
                'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium',
                'potassium', 'haemoglobin', 'packed_cell_volume',
                'white_blood_cell_count', 'red_blood_cell_count', 'hypertension',
                'diabetes_mellitus', 'coronary_artery_disease', 'appetite',
                'peda_edema', 'aanemia'],data=[inp_dat])
        
        if trans_dat.bacteria[0]==1 : trans_dat.bacteria = 0 
        else: trans_dat.bacteria = 1

        result = model.predict(scaler.transform(trans_dat))

        print(result)

        if result[0]==1:
            st.text(f"""
            You have a Kidney Disease. 
            Please Consult the Doctor immediately. 
            Make sure of health in your Diet. """)
        else :
            st.text(f"""
            Great You are Healthy.
            There are no marks of Kidney Disease. 
            Enjoy your life full of Happiness. """)

if __name__=='__main__':
    main()