import pickle
import streamlit as st

#membaca model

mobil_model = pickle.load(open('mobil_bekas.sav', 'rb'))

#Nama Web
st.title('Prediksi Mobil Bekas Rusak Eropa')


col1, col2 = st.columns(2)

with col1 :
    year = st.text_input('Masukan Tahun?(skala : 2015 - 2019)')
    mileage = st.text_input('masukan Jarak tempuh(skala : 10000 - 100000)')
    tax = st.text_input('masukan harga pajak (skala : 0 - 200)')
with col2 :
    price = st.text_input('masukan harga (skala : 10000-30000)')    
    mpg = st.text_input('masukan nilai konsumsi bahan bakar miles/gallon (skala : 40.0 - 75.0)')
    engineSize = st.text_input('masukan ukuran mesin (skala : 1.0-3.0)')

ket_harga = ''

# membuat Tombol Untuk Prediksi
if st.button('Test'):
    ket_prediction = mobil_model.predict([[year, mileage, tax, price, mpg, engineSize]])
    if(ket_prediction[0]==0):
        ket_harga = 'Mobil Mulus'
    else : 
        ket_harga = 'Mobil Rusak/Lecet'

    st.success(ket_harga)

# st.success(ket_harga)
