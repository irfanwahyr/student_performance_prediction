import streamlit as st
import pandas as pd
import joblib

loaded_kmeans = joblib.load('kmeans_model.joblib')

def predict_cluster(data):
    predicted_cluster = loaded_kmeans.predict(data)
    return predicted_cluster[0]

st.title('Prediksi Cluster Mahasiswa')

age = st.number_input('Umur saat mendaftar', min_value=0, max_value=100, value=13)
gender = st.selectbox('Jenis Kelamin', [0, 1], format_func=lambda x: 'Perempuan' if x == 0 else 'Laki-laki')

input_data = pd.DataFrame({
    'Age_at_enrollment': [age],
    'Gender': [gender]
})

features = ['Age_at_enrollment', 'Gender']
X = input_data[features]

if st.button('Prediksi'):
    predicted_cluster = predict_cluster(X)
    st.write(f"Cluster untuk Mahasiswa: {predicted_cluster}")
