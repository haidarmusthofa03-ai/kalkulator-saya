import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="Kalkulator Web Saya", page_icon="🔢")

st.title("🔢 Kalkulator Web Sederhana")
st.write("Aplikasi ini dibuat menggunakan Python dan Streamlit.")

# Membuat kolom untuk input angka
col1, col2 = st.columns(2)

with col1:
    angka1 = st.number_input("Masukkan angka pertama:", value=0.0)

with col2:
    angka2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilihan operasi matematika
operasi = st.selectbox("Pilih operasi matematika:", 
                       ["Tambah (+)", "Kurang (-)", "Kali (x)", "Bagi (/)"])

# Tombol hitung
if st.button("Hitung Hasil"):
    if operasi == "Tambah (+)":
        hasil = angka1 + angka2
    elif operasi == "Kurang (-)":
        hasil = angka1 - angka2
    elif operasi == "Kali (x)":
        hasil = angka1 * angka2
    elif operasi == "Bagi (/)":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Error (Tidak bisa bagi nol)"
    
    # Menampilkan hasil
    st.success(f"Hasil dari {operasi} adalah: **{hasil}**")