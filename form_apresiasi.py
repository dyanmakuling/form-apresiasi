import streamlit as st
import csv

st.title("🎭 Form Feedback Penonton Pertunjukan")

nama = st.text_input("Siapa namamu?")
asal = st.text_input("Dari mana asalmu?")
puas = st.radio("Apakah kamu puas dengan pertunjukan?", ["Ya", "Tidak"])
minat = st.radio("Apakah kamu tertarik bergabung dengan kami?", ["Ya", "Tidak"])

umur = skill = kontak = motivasi = "-"

if minat == "Ya":
    umur = st.text_input("Berapa usiamu?")
    skill = st.text_input("Apa keahlian/kekuatanmu?")
    kontak = st.text_input("Boleh tahu kontakmu?")
    motivasi = st.text_area("Kenapa kamu ingin bergabung?")

if st.button("Kirim"):
    with open("data_penonton.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, asal, puas, minat, umur, skill, kontak, motivasi])
    st.success("🎉 Data berhasil dikirim. Terima kasih ya!")
