# -*- coding: utf-8 -*-

import pickle
import joblib
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = joblib.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',value=None,placeholder="")
        
    with col2:
        Glucose = st.number_input('Glucose Level',value=None,placeholder="")
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value',value=None,placeholder="")
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value',value=None,placeholder="")
    
    with col2:
        Insulin = st.number_input('Insulin Level',value=None,placeholder="")
    
    with col3:
        BMI = st.number_input('BMI value',value=None,placeholder="")
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value',value=None,placeholder="")
    
    with col2:
        Age = st.number_input('Age of the Person',value=None,placeholder="")
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'

        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age',value=None,placeholder="")
        
    with col2:
        sex = st.number_input('Sex',value=None,placeholder="")
        
    with col3:
        cp = st.number_input('Chest Pain types',value=None,placeholder="")
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure',value=None,placeholder="")
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',value=None,placeholder="")
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',value=None,placeholder="")
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',value=None,placeholder="")
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',value=None,placeholder="")
        
    with col3:
        exang = st.number_input('Exercise Induced Angina',value=None,placeholder="")
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',value=None,placeholder="")
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',value=None,placeholder="")
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',value=None,placeholder="")
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',value=None,placeholder="")
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col1:
        Jitter_percent = st.number_input('MDVP:Jitter(%)',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col2:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col3:
        RAP = st.number_input('MDVP:RAP',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col1:
        PPQ = st.number_input('MDVP:PPQ',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col2:
        DDP = st.number_input('Jitter:DDP',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col3:
        Shimmer = st.number_input('MDVP:Shimmer',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col1:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col2:
        APQ3 = st.number_input('Shimmer:APQ3',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col3:
        APQ5 = st.number_input('Shimmer:APQ5',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col1:
        APQ = st.number_input('MDVP:APQ',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col2:
        DDA = st.number_input('Shimmer:DDA',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col3:
        NHR = st.number_input('NHR',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col1:
        HNR = st.number_input('HNR',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col2:
        RPDE = st.number_input('RPDE',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col3:
        DFA = st.number_input('DFA',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col1:
        spread1 = st.number_input('spread1',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col2:
        spread2 = st.number_input('spread2',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col3:
        D2 = st.number_input('D2',value=None,placeholder="",step=1e-6,format="%.6f")
        
    with col1:
        PPE = st.number_input('PPE',value=None,placeholder="",step=1e-6,format="%.6f")
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


