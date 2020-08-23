# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:29:48 2020

@author: kerem
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

dataset = pd.read_excel("tecrübe.xlsx")
print(dataset)
x = dataset["İş tecrübesi"]# Verimizdeki 1.sütün
y = dataset["maaş"]#Verimizdeki 2.sütün
x=np.array(x)
y=np.array(y)

x = np.reshape(x,15)#X ekseninde yer alan eleman sayısı kadar array oluşturur.
y = np.reshape(y,15)#Y ekseninde yer alan eleman sayısı kadar array oluşturur.


 
lineer = lr() # Lineer Regresyonu çağırdık.

 
y=y.reshape(-1,1) #(-1,1) yazmamızın sebebi numpy kütüphanesi
                  # grafiğimizin boyutlarını arrayimizin boyutuna göre ayarlamasıdır.
x=x.reshape(-1,1)  
lineer.fit(x,y)  

lineer.predict(y) 

m = lineer.coef_ # Eğrimizin eğimini bulduk.  

b= lineer.intercept_ # Eğim denklemindeki +b dir.

a = np.arange(20) 

a=a.reshape(-1,1)  

deneyim="e"

while(deneyim=="e"):
    tecrübe = float(input("İş tecrübeniz kaç yıldır?")) #
    if(tecrübe>100):
        print("Çalışılan yıl 100'den büyük. ")
    tahmin = m*tecrübe+b  
    print(tahmin)  
    plt.scatter(x,y,c="red")
    
    plt.scatter(tecrübe,tahmin,c="blue",marker="|") #noktamızın şeklini belirtiyoruz
    plt.xlabel("İş tecrübesi")
    plt.ylabel("Maaslar")
    plt.title("Bilgisayar Mühendislerini maaş tahmini  ")
    plt.plot(a,m*a+b) #eğim doğrusunu çizdirmemiz için gerekli
    plt.show() #grafiğimizi gösteriyoruz
    
    
    plt.show()
    print("y=",m,"x+",b) #fonksiyonu(eğimi) bastırıyoruz
    deneyim=input("Tekrardan maaş tahmini yapmak ister misiniz ? ")  
    if(deneyim!="e"):
        break
