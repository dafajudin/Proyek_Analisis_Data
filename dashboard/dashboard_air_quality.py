import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import requests
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config (
    page_title='Air Quality Dashboard',
    page_icon=':bar_chart:',
)

#judul data dashboard
st.title('Air Quality in district Changpi')

def load_data():
    # Ganti 'nama_file.csv' dengan nama file yang sesuai
    df = pd.read_csv('air_quality_changpi.csv')
    return df

# Main function
def main():
    # Load data
    df = load_data()

    # Pilihan menu
    option = st.sidebar.selectbox('Pilih Pertanyaan',
                                [
                                    'Hubungan Polutan dengan Waktu',
                                    'Distribusi Polutan di Distrik Changpi',
                                    'Tren Curah Hujan di Distrik Shunyi'
                                ])

    # Pertanyaan 1: Hubungan Polutan dengan Waktu
    if option == 'Hubungan Polutan dengan Waktu':
        st.subheader('Hubungan Polutan dengan Waktu')
        st.write("Dalam pengembangan.")

    # Pertanyaan 2: Distribusi Polutan di Distrik Changpi
    elif option == 'Distribusi Polutan di Distrik Changpi':
        st.subheader('Distribusi Polutan di Distrik Changpi')
        # Membuat histogram untuk distribusi polutan PM10, SO2, dan NO2
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 3, 1)
        sns.histplot(df['PM10'], bins=20, kde=True, color='blue')
        plt.title('Distribusi PM10')
        plt.xlabel('Konsentrasi PM10')
        plt.subplot(1, 3, 2)
        sns.histplot(df['SO2'], bins=20, kde=True, color='green')
        plt.title('Distribusi SO2')
        plt.xlabel('Konsentrasi SO2')
        plt.subplot(1, 3, 3)
        sns.histplot(df['NO2'], bins=20, kde=True, color='red')
        plt.title('Distribusi NO2')
        plt.xlabel('Konsentrasi NO2')
        plt.tight_layout()

        # Menampilkan plot menggunakan Streamlit
        st.pyplot(plt)

    # Pertanyaan 3: Tren Curah Hujan di Distrik Changpi
    elif option == 'Tren Curah Hujan di Distrik Changpi':
        st.subheader('Tren Curah Hujan di Distrik Changpi')
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='RAIN', data=df)
        plt.title('Tren Curah Hujan di Distrik Changpi')
        plt.xlabel('Tahun')
        plt.ylabel('Curah Hujan (mm)')
        plt.grid(True)
        plt.xticks(df['year'].unique().astype(int))

        # Menampilkan plot menggunakan Streamlit
        st.pyplot(plt)

# Menjalankan main function
if __name__ == '__main__':
    main()

st.caption('Created by Muhammad Dafa Sirajudin')