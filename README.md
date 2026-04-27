# multiple-disease-prediction-streamlit-app
This repository contains the codebase for "Multiple Disease Prediction Streamlit App". The training notebooks &amp; the datasets are also provided in the respective folders. 

app.py is the streamlit app code.
run the command "**pip install -r requirements.txt**" to install the required dependencies for the streamlit app.

You may need to install additional libraries for running the jupyter notebooks.

## Add more diabetes data and retrain

If you download extra diabetes rows (for example from Kaggle), the file must use the same columns and order:

`Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome`

1. Put extra `.csv` files in `dataset/extra_diabetes/`
2. Run:
   - `python retrain_diabetes.py`
3. The script validates columns, merges data, trains, evaluates, and updates:
   - `saved_models/diabetes_model.sav`
