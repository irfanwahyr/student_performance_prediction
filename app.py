import streamlit as st
import pandas as pd
import joblib

loaded_kmeans = joblib.load('decisiontree_model.joblib')

def predict_cluster(data):
    predicted_cluster = loaded_kmeans.predict(data)
    return predicted_cluster[0]

def predict_outcome(predict):
    if predict == 0:
        return 'Mahasiswa diprediksi akan Graduate'
    else:
        return 'Mahasiswa diprediksi akan Dropout'

st.title('Prediksi Cluster Mahasiswa')

input_data = {
    'memiliki Hutang?': st.radio('Debtor', options=['Tidak', 'Ya']),
    'Biaya Kuliah terkini?': st.radio('Biaya Kuliah Terkini', options=['Tidak', 'Ya']),
    'Tingkat Pengangguran': st.number_input('Tingkat Pengangguran', min_value=0.0, value=50.0),
    'Inflation_rate': st.number_input('Inflation Rate', value=0.0),
    'GDP': st.number_input('GDP', value=0.0)
}

input_data['memiliki Hutang?'] = 1 if input_data['memiliki Hutang?'] == 'Ya' else 0
input_data['Biaya Kuliah terkini?'] = 1 if input_data['Biaya Kuliah terkini?'] == 'Ya' else 0

input_df = pd.DataFrame(input_data, index=[0])

if st.button('Prediksi'):
    predicted = predict_cluster(input_df)
    prediction = predict_outcome(predicted)
    st.write(prediction)
