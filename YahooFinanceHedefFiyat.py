import pandas as pd
from yahooquery import Ticker
import requests
from io import StringIO

#Bist100 Hisse kodlarını alıp, yahoo finance için uygun hale getirir
def hisseler():
    url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?endeks=01#page-1"
    html_text=requests.get(url).text
    html_io=StringIO(html_text)
    tablo=pd.read_html(html_io)[2]["Kod"]
    for i in range(len(tablo)):
        tablo[i] += ".IS"
    hissekod=tablo.to_list()
    return hissekod

#Hisselerle ilgili gerekli bilgileri alır ve dataframe olarak yazdırır
def hedef_fiyat():
    hisse=Ticker(hisseler())
    hisse_dict=hisse.financial_data
    df=pd.DataFrame.from_dict(hisse_dict).T.reset_index().iloc[:,[0,2,24,25,26,27]]
    df.columns=["Hisse Adı","Güncel Fiyat","En Yüksek Tahmin","En Düşük Tahmin",
            "Ortalama Tahmin","Medyan Tahmin"]
    df["Hisse Adı"]=df["Hisse Adı"].str.replace(".IS","",regex=False)
    df.dropna(axis=0,inplace=True)
    df.reset_index(drop=True,inplace=True)
    
    return print(df)


hedef_fiyat()

