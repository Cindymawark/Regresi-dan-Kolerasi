import streamlit as st
import pandas as pd
import csv
import os

st.title('Program Pemodelan Regresi Linear Sederhana dan Korelasi Linear Sederhana')
st.write('NRP  : 152017084')
st.write('Nama : Cindy Mawar Kasih')

@st.cache(persist=True)
@st.cache(persist=True)
def exploredata(data):
    df = pd.read_csv(os.path.join(data))
    return df 

def main(filepath):
    with open(filepath, "r+") as fin:
        fin.readline()
        totalX = sum(int(i[1]) for i in csv.reader(fin))
    print("Sigma X :: " + str(totalX))

    with open(filepath, "r+") as fin:
        fin.readline()
        totalY = sum(int(i[2]) for i in csv.reader(fin))
    print("Sigma Y :: " + str(totalY))

    with open(filepath, "r+") as fin:
        fin.readline()
        SigmaX2 = sum(int(i[1])**2 for i in csv.reader(fin))
    print("Sigma X^2 :: " + str(SigmaX2))

    with open(filepath, "r+") as fin:
        fin.readline()
        SigmaY2 = sum(int(i[2])**2 for i in csv.reader(fin))
    print("Sigma Y^2 :: " + str(SigmaY2))

    with open(filepath, "r+") as fin:
        fin.readline()
        SigmaXY = sum(int(i[1])*int(i[2]) for i in csv.reader(fin))
    print("Sigma XY :: " + str(SigmaXY))

    SigmaXKuadrat = totalX**2
    print("(Sigma X)^2 :: " + str(SigmaXKuadrat)) 

    SigmaYKuadrat = totalY**2
    print("(Sigma Y)^2 :: " + str(SigmaYKuadrat)) 

    n = len(list(csv.reader(open(filepath))))-1
    print("n :: " + str(n))

    a = round((totalY*SigmaX2 - totalX * SigmaXY)/(n*SigmaX2 - SigmaXKuadrat), 5)
    b = round((n*SigmaXY - totalX*totalY)/(n*totalX - SigmaXKuadrat), 5)

    r = round(((n*SigmaXY - totalX*totalY)) / ((n*SigmaX2 - SigmaXKuadrat)*(n*SigmaY2 - SigmaYKuadrat))**0.5, 5)

    koefdet = round(((r**2) * 100), 5)
    variabellain = 100 - koefdet

    interkoefdet = ("Jadi kontribusi variabel X terhadap Y adalah " + str(koefdet) + " %" +
                      " dan sisanya sebesar " + str(variabellain) + " %"+" dipengaruhi oleh variabel selain X")

    if(b < 0):
        hasil = ("Y = " + str(a) + " - " + str(-b) + " X")
    else:
         hasil = ("Y = " + str(a) + " + " + str(b) + " X")

    if((r>=0) and (r<0.2)):
        r2 = ("Kekuatan hubungan (r) : Sangat Lemah")
    elif((r>=0.2) and (r<0.4)):
        r2 = ("Kekuatan hubungan (r) : Lemah")
    elif((r>=0.4) and (r<0.6)):
        r2 = ("Kekuatan hubungan (r) : Sedang")
    elif((r>=0.6) and (r<0.8)):
        r2 = ("Kekuatan hubungan (r) : Kuat")
    elif((r>=0.8) and (r<=1)):
        r2 = ("Kekuatan hubungan (r) : Sangat Kuat")

    if(r < 0):
        intrepretasikor = (
            "Jadi Nilai korelasi tersebut adalah negatif yang menyatakan bahwa perbandingannya adalah terbalik")
    else:
        intrepretasikor = (
            "Jadi Nilai korelasi tersebut adalah positif yang menyatakan bahwa perbandingannya adalah searah")

    values = a, b, totalX, totalY, SigmaX2, SigmaXKuadrat, SigmaXY, SigmaY2, n, hasil, SigmaYKuadrat, r, koefdet, r2, intrepretasikor, interkoefdet
    return values

try:
    st.markdown('<style>body{background-color: #E3c7dd;}</style>',unsafe_allow_html=True)
    data_file = st.file_uploader("Upload CSV", type=['csv'])
    data = exploredata(data_file.name)
    xa = main(data_file.name)
    st.write("Data yang digunakan")
    st.write(data)

    st.write("Nilai setiap variabel")

    if st.checkbox("n"):
        st.write(xa[8])
    if st.checkbox("ΣXi"):
        st.write(xa[2])
    if st.checkbox("ΣYi"):
        st.write(xa[3])
    if st.checkbox("ΣXiYi"):
        st.write(xa[6])
    if st.checkbox("ΣXi2"):
        st.write(xa[4])
    if st.checkbox("ΣYi2"):
        st.write(xa[7])
    if st.checkbox("(ΣXi)2"):
        st.write(xa[5])
    if st.checkbox("(ΣYi)2"):
        st.write(xa[10])

    st.write("Regresi Linear Sederhana")
    if st.checkbox("Konstanta a"):
        st.write(xa[0])
    if(st.checkbox("Koefisien b")):
        st.write(xa[1])
    if(st.checkbox("Y = a + bx")):
        st.success(xa[9])

    st.write("Kolerasi Pearson")
    if(st.checkbox("r")):
        st.success(xa[11])
        st.write(xa[14])
        st.write(xa[13])
    if(st.checkbox("Koefisien Determinasi")):
        st.success(xa[12])
        st.write(xa[15])

except:
    st.write("Masukan dahulu data file csv yang akan digunakan")