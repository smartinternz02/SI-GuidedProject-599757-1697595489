# app.py
from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model from the pickle file
with open('model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

# Load your updated dataset (make sure the column names match your dataset)
df_test = pd.read_csv('Training.csv')
X_train = df_test.drop('prognosis', axis=1)
y_train = df_test['prognosis']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form.getlist('symptoms')
    predicted_disease = predict_disease(symptoms)
    return render_template('result.html', disease=predicted_disease)

def predict_disease(symptoms):
    # Drop the "Unnamed: 133" column if it exists
    if 'Unnamed: 133' in X_train.columns:
        X_train.drop('Unnamed: 133', axis=1, inplace=True)

    input_data = pd.DataFrame(0, index=[0], columns=X_train.columns)

    for symptom in symptoms:
        if symptom in input_data.columns:
            input_data[symptom] = 1

    predicted_disease = rf_model.predict(input_data)

    return predicted_disease[0]

if __name__ == '__main__':
    app.run(debug=True)
