# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 12:46:28 2026

@author: dell
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the file
diabetes_model=pickle.load(open('C:/Users/dell/OneDrive/Desktop/multiple disease predictor/trained_model.sav','rb'))
heart_disease_model=pickle.load(open('C:/Users/dell/OneDrive/Desktop/multiple disease predictor/heart_disease_model.sav','rb'))
cancer_model=pickle.load(open('C:/Users/dell/OneDrive/Desktop/multiple disease predictor/breast_cancer_model.sav','rb'))

#sidebar for app
with st.sidebar:
    selected=option_menu('Multiple Disease predictor by Gaurika Thakur',
                         ['heart disease predictor',
                         'diabetes predictor',
                         'cancer predictor'],
                         icons=['activity','heart','person'],
                         default_index=0)
    
#diabetes predictor 
if (selected) == ('heart disease predictor'):
    st.title('heart disease predictor using Ml')
    col1,col2,col3=st.columns(3)
    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Sex (1=Male,0=Female)')
        cp = st.text_input('Chest Pain type')
        trestbps = st.text_input('Resting BP')
        chol = st.text_input('Cholesterol')

    with col2:
        fbs = st.text_input('Fasting Blood Sugar')
        restecg = st.text_input('Rest ECG')
        thalach = st.text_input('Max Heart Rate')
        exang = st.text_input('Exercise Angina')
        oldpeak = st.text_input('Oldpeak')

    with col3:
        slope = st.text_input('Slope')
        ca = st.text_input('Major vessels (0-3)')
        thal = st.text_input('Thal value')

    if st.button('Heart Test Result'):

        if age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal:

            input_data = [[
                float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(slope), float(ca), float(thal)
            ]]

            prediction = heart_disease_model.predict(input_data)

            if prediction[0] == 1:
                st.error("Person has Heart Disease")
            else:
                st.success("Person does NOT have Heart Disease")
        else:
            st.warning("Please fill all values")
    
          
    #diabetes
    
if (selected)== ('diabetes predictor'):
    st.title('Diabetes Predictor using ML')
    
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
        
    with col2:
        Insulin = st.text_input("Insulin value")
    with col3: 
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
        
    with col2:
        Age = st.text_input("Age of the person")
        
        
          
        
        
    
    
    
    
    

   
    if st.button('Diabetes Test Result'):

        # check empty
        if Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age:

            input_data = [[
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]]

            prediction = diabetes_model.predict(input_data)

            if prediction[0] == 1:
                st.error("The person is diabetic")
            else:
                st.success("The person is NOT diabetic")

        else:
            st.warning("Please fill all fields")

if (selected)==('cancer predictor'):
    st.title('cancer predictor using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.text_input('radius_mean')
        texture_mean = st.text_input('texture_mean')
        perimeter_mean = st.text_input('perimeter_mean')
        area_mean = st.text_input('area_mean')
        smoothness_mean = st.text_input('smoothness_mean')
        compactness_mean = st.text_input('compactness_mean')
        concavity_mean = st.text_input('concavity_mean')
        concave_points_mean = st.text_input('concave points_mean')
        symmetry_mean = st.text_input('symmetry_mean')
        fractal_dimension_mean = st.text_input('fractal_dimension_mean')

    with col2:
        radius_se = st.text_input('radius_se')
        texture_se = st.text_input('texture_se')
        perimeter_se = st.text_input('perimeter_se')
        area_se = st.text_input('area_se')
        smoothness_se = st.text_input('smoothness_se')
        compactness_se = st.text_input('compactness_se')
        concavity_se = st.text_input('concavity_se')
        concave_points_se = st.text_input('concave points_se')
        symmetry_se = st.text_input('symmetry_se')
        fractal_dimension_se = st.text_input('fractal_dimension_se')

    with col3:
        radius_worst = st.text_input('radius_worst')
        texture_worst = st.text_input('texture_worst')
        perimeter_worst = st.text_input('perimeter_worst')
        area_worst = st.text_input('area_worst')
        smoothness_worst = st.text_input('smoothness_worst')
        compactness_worst = st.text_input('compactness_worst')
        concavity_worst = st.text_input('concavity_worst')
        concave_points_worst = st.text_input('concave points_worst')
        symmetry_worst = st.text_input('symmetry_worst')
        fractal_dimension_worst = st.text_input('fractal_dimension_worst')

    if st.button('Cancer Test Result'):

        values = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                  compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
                  radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se,
                  concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                  radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                  compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]

        if all(values):

            input_data = [[float(x) for x in values]]

            prediction = cancer_model.predict(input_data)

            if prediction[0] == 1:
                st.error("Cancer detected (Malignant)")
            else:
                st.success("No Cancer detected (Benign)")

        else:
            st.warning("Please fill all values")

     