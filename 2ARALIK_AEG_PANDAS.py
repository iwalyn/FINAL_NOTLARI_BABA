#PANDAS#

# veri analizi ve veri işlemede kullanılır. 
# Hızlıdır.
# Asıl amacı tablo okumak ve yazmak
# satır ve sütundaki verileri çerçeve/tablolar (dataframing)
# eksik değer işlemleri
# gruplama özetleme ve istatistiksel analiz
# veri görselleştirme için ön hazırlık vb. gibi
# Pandas genellikle veri analistleri ve veri bilimciler tarafından kullanılır.#
# PANDAS NEDEN VAR? pythonda normal listeler veya numpy ileveri tutmak zordur
# pandas ise tek satırda DataFrame olarak çevirir ve veri çerçevesine (tabloya) istediğimiz gibi davranabiliriz.
# pandas içerisindeki iki temel yapı: series ve dataframe

import pandas as pd
import numpy as np

# YENİ: PANDAS SERİES NEDİR? Tek sütunluk verilerdir.
#excel'deki tek sütun gibi. Pandas series olarak tutar.
#parantez içerisinde ilk yazdıklarımız veri, sonrasında yazdıklarımız indeks(başlık) alır.

seri = pd.Series([185,90,48]) #bu bir seri şuan, tablo değil
print(seri) # 0    185    OLARAK PRİNT EDER
#             1     90
#             2     48    #
print(type(seri)) #int64 veri tipi

#YENİ:  İNDEKS DEĞİŞTİRME
seri1 = pd.Series([185,75,19], ["boy","kilo","yaş"]) #ŞİMDİ YAZDIRILAN ŞEY DAHA DETALI:
print(seri1)
#   boy     185
#   kilo     75
#   yaş      19
#   dtype: int64   ŞEKLİNDE EKRANA YAZDIRILIR***#

#YENİ:  DATAFRAME NEDİR? Birden fazla serinin yan yana gelmiş hali yani tam bir tabllo gibi düşünülebilir.*
dataframe = pd.DataFrame({
    "isim": ["Ahmet", "Ayşe", "Mehmet"],
    "yaş": [25,30,22],
    "puan": [90,80,100]

}) #SÖZLÜK VERİ TİPİNDE OLDUĞU İÇİN {} KULLANILDI
print(dataframe)
#     isim  yaş  puan
#0   Ahmet   25    90
#1    Ayşe   30    80
#2  Mehmet   22   100    ŞEKLİNDE BİR TABLO OLUŞTURDU#

#DATAFRAME'de kullanabilmek için numpy ile array(dizi) oluşturalım.

np.random.seed(42) #rastgele üretilen sayıların her run'da aynı kalması için
data = np.random.randn(4,3)
print(data)

dataframe1 = pd.DataFrame(data)
print(dataframe1)

#isimlendirme yapalım

yenidataframe = pd.DataFrame(data, index=["izmit", "derince", "körfez", "gebze"],
                             columns=["sıcaklık", "nem", "rüzgar_hızı"])

print(yenidataframe)
#         sıcaklık       nem  rüzgar_hızı
#izmit    0.496714 -0.138264     0.647689
#derince  1.523030 -0.234153    -0.234137
#körfez   1.579213  0.767435    -0.469474
#gebze    0.542560 -0.463418    -0.465730    ŞEKLİNDE PRİNT EDER#

#YENİ:  BELİRLİ SÜTUNLARI SEÇME
print(yenidataframe[["sıcaklık","nem"]])
#         sıcaklık       nem
#izmit    0.496714 -0.138264
#derince  1.523030 -0.234153
#körfez   1.579213  0.767435
#gebze    0.542560 -0.463418          ŞEKLİNDE PRİNT EDER  #

#YENİ: EĞER SADECE SATIRLARDAN BİR ELEMAN GETİRECEKSEKy
print("GEBZENİN SICAKLIK DEĞER:   ", yenidataframe.loc["gebze"]["nem"])

#YENİ:  EĞER SİLMEK İSTİYORSAK
print(yenidataframe.drop("rüzgar_hızı", axis=1)) #YENİ: AXİS=1 :  SÜTUN / AXİS=0 : SATIR