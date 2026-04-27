import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Risk Check')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('How many times pregnant')

    with col2:
        Glucose = st.text_input('Blood sugar level (glucose)')

    with col3:
        BloodPressure = st.text_input('Blood pressure')

    with col1:
        SkinThickness = st.text_input('Skin fold thickness')

    with col2:
        Insulin = st.text_input('Insulin level')

    with col3:
        BMI = st.text_input('Body Mass Index (BMI)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Family history score for diabetes')

    with col2:
        Age = st.text_input('Age')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Check Diabetes Risk'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Result: High chance of diabetes. Please consult a doctor.'
        else:
            diab_diagnosis = 'Result: Low chance of diabetes.'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Health Risk Check')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Gender (0 = female, 1 = male)')

    with col3:
        cp = st.text_input('Chest pain type (0-3)')

    with col1:
        trestbps = st.text_input('Resting blood pressure')

    with col2:
        chol = st.text_input('Cholesterol (mg/dl)')

    with col3:
        fbs = st.text_input('Fasting blood sugar over 120? (1 = yes, 0 = no)')

    with col1:
        restecg = st.text_input('Resting ECG result (0-2)')

    with col2:
        thalach = st.text_input('Maximum heart rate')

    with col3:
        exang = st.text_input('Chest pain during exercise? (1 = yes, 0 = no)')

    with col1:
        oldpeak = st.text_input('ECG drop during exercise (oldpeak)')

    with col2:
        slope = st.text_input('Exercise ST slope (0-2)')

    with col3:
        ca = st.text_input('Number of major vessels seen (0-3)')

    with col1:
        thal = st.text_input('Thal value (0 = normal, 1 = fixed defect, 2 = reversible defect)')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Check Heart Risk'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'Result: High chance of heart disease. Please consult a doctor.'
        else:
            heart_diagnosis = 'Result: Low chance of heart disease.'

    st.success(heart_diagnosis)

