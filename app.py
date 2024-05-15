import streamlit as st
import pandas as pd
import joblib

loaded_kmeans = joblib.load('kmeans_model.joblib')

def convert_to_cluster(cluster):
    if cluster in [0]:
        return 0
    elif cluster in [1]:
        return 1
    else:
        return 2

def predict_cluster(data):
    predicted_cluster = loaded_kmeans.predict(data)
    predicted_attrition = convert_to_cluster(predicted_cluster[0])
    return predicted_attrition

st.title('Prediksi Cluster Mahasiswa')

age = st.number_input('Umur saat mendaftar', min_value=0, max_value=100, value=13)
gender = st.selectbox('Jenis Kelamin', [0, 1], format_func=lambda x: 'Laki-laki' if x == 1 else 'Perempuan')
status = st.selectbox('Status', [0, 1, 2], format_func=lambda x: 'Graduate' if x == 0 else ('Dropout' if x == 1 else 'Enrolled'))

input_data = pd.DataFrame({
    'Age_at_enrollment': [age],
    'Gender': [gender],
    'Status': [status]
})

features = ['Age_at_enrollment', 'Gender', 'Status']
X = input_data[features]

if st.button('Prediksi'):
    predicted_cluster = predict_cluster(X)
    st.write("Cluster untuk Mahasiswa: {}".format(predicted_cluster))
