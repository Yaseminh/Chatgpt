import pandas as pd
import matplotlib.pyplot as plt


import os

if os.path.isfile('form-data.csv'):
    # CSV dosyasını okuyun
    df = pd.read_csv('form-data.csv')

    # Verileri yazdırın
    print(df)

    # Değişken sayısını yazdır
    a = len(df.columns)

    x = 521;

    plt.figure(figsize=(11, 2))
    for i in range(0, len(df.columns)):
        plt.subplot(2, 5, i + 1)
        plt.pie(df[df.columns[i]].value_counts(), labels=df[df.columns[i]].unique(), autopct='%1.1f%%')
        plt.title(df.columns[i])
    plt.show()

    # Verileri pasta grafiğine dönüştürün
    '''plt.subplot(221)
    plt.pie(df['soru1'].value_counts(), labels=df['soru1'].unique())

    plt.subplot(222)
    plt.pie(df['soru2'].value_counts(), labels=df['soru2'].unique())

    plt.subplot(223)
    plt.pie(df['soru3'].value_counts(), labels=df['soru3'].unique())

    # Grafiği gösterin
    plt.show()'''
    # Verileri sütun ve satır sayısına göre bölmek için boyutları ayarlayın
else:
    print('Dosya yok.')



