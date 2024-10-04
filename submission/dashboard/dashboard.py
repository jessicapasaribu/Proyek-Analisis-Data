# Jessica Pasaribu

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Muat data
customers = pd.read_csv('customers_dataset.csv')
order_payments = pd.read_csv('order_payments_dataset.csv') 

# Judul Dashboard
st.title('Dashboard Analisis Data Pelanggan')

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Kota Pelanggan", "Rata-rata Pembayaran", "Sebaran Metode Pembayaran"])

# Beranda
if page == "Beranda":
    st.write("""
        Selamat datang di Dashboard Analisis Data Pelanggan!
        
        Di sini Anda dapat mengeksplorasi data pelanggan dan pembayaran.
        Pilih opsi di sebelah kiri untuk mulai menjelajahi analisis.
    """)

# Kota Pelanggan
elif page == "Kota Pelanggan":
    st.subheader('1. Kota dengan Jumlah Pelanggan Terbanyak')

    # Mengitung jumlah pelanggan per kota
    city_counts = customers['customer_city'].value_counts()

    # Mengmbil kota dengan pelanggan terbanyak
    top_city = city_counts.idxmax()
    top_city_count = city_counts.max()

    # Menampilkan hasil
    st.write(f"Kota dengan jumlah pelanggan terbanyak adalah **{top_city}** dengan **{top_city_count}** pelanggan.")

    # Visualisasi
    plt.figure(figsize=(12, 6))
    sns.barplot(x=city_counts.index[:10], y=city_counts.values[:10], palette='viridis')
    plt.xticks(rotation=45)
    plt.title('10 Kota dengan Jumlah Pelanggan Terbanyak', fontsize=16)
    plt.xlabel('Kota', fontsize=12)
    plt.ylabel('Jumlah Pelanggan', fontsize=12)
    st.pyplot(plt)

#Rata-rata Pembayaran
elif page == "Rata-rata Pembayaran":
    st.subheader('2. Rata-rata Nilai Pembayaran untuk Setiap Tipe Pembayaran')

    # menghitung rata-rata nilai pembayaran berdasarkan tipe
    payment_avg = order_payments.groupby('payment_type')['payment_value'].mean().reset_index()

    # menampilkan hasil
    st.write("Rata-rata nilai pembayaran untuk setiap tipe pembayaran adalah sebagai berikut:")
    st.dataframe(payment_avg)

    # Visualisasi
    plt.figure(figsize=(12, 6))
    sns.barplot(x='payment_type', y='payment_value', data=payment_avg, palette='mako')
    plt.title('Rata-rata Nilai Pembayaran untuk Setiap Tipe Pembayaran', fontsize=16)
    plt.xlabel('Tipe Pembayaran', fontsize=12)
    plt.ylabel('Rata-rata Nilai Pembayaran', fontsize=12)
    st.pyplot(plt)

#Sebaran Metode Pembayaran
elif page == "Sebaran Metode Pembayaran":
    st.subheader('3. Sebaran Penggunaan Metode Pembayaran')

    # menghitung jumlah penggunaan setiap metode pembayaran
    payment_distribution = order_payments['payment_type'].value_counts().reset_index()
    payment_distribution.columns = ['payment_type', 'count']

    # Menampilkan hasil
    st.write("Sebaran penggunaan metode pembayaran oleh pelanggan:")
    st.dataframe(payment_distribution)

    # Visualisasi sebaran metode pembayaran
    plt.figure(figsize=(10, 6))
    plt.pie(payment_distribution['count'], labels=payment_distribution['payment_type'], autopct='%1.1f%%', startangle=90)
    plt.title('Sebaran Penggunaan Metode Pembayaran', fontsize=16)
    plt.axis('equal') 
    st.pyplot(plt)

# Footer
st.write("### Terima kasih telah melihat dashboard ini!")
