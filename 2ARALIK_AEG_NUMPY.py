#NUMPY#

#NumPy, Python için sayısal hesaplama kütüphanesidir.
# ML Kütüphaneleri veriyi genellikle numPy dizisi olarak belirler
# Normal listelere göre daha hızlı ve az yer kaplar.
# #

import numpy as np #np olarak numpy kütüphanesini çağırdık.
dizi = np.array([1,2,3,4,5,6]) #1 BOYUTKU DİZİ OLUŞTURDUK
print(dizi)
print(type(dizi)) #class = ndarray olarak çıkar. ONE DİMENSION ARRAY?

#YENİ:  dtype dizi içerisindeki elemanların veri tipini gösterir.

d1 = np.array([1, 2, 3]) #int olarak da, (int numpy dizisi)
d2 = np.array([2.11, 3.2, 7.3]) #float olarak da yazabiliriz (float numpy dizisi)

print(d1, d1.dtype) #int64
print(d2, d2.dtype) #float64
#NOT: eğer bir dizinin içerisine hem float hem integer koyulursa,
# python hepsini float64'e dönüştürür. 1 =>  1.0 gibi.#

#YENİ:  2 Boyutlu Diziler, shape(şekil) ve ndim(dimension, boyut)
# 2B diziler matris gibi düşünülebilir (satırxsütun
# ndim: kaç boyutlu olduğğunu gösterir.#

ikiboyutludizi = np.array([[1,2,3],[4,5,6]])
print("matris:  ", ikiboyutludizi)
print("boyut:   ", ikiboyutludizi.ndim)  #boyut:    2
print("şekil:   ", ikiboyutludizi.shape) #şekil:    (2, 3) 2 SATIR 3 SÜTUN (satır,sütUN)

#YENİ:  np.arange ile düzenli aralıklarla sayı üretebiliriz tıpkı range gibi [) şeklinde.
#YENİ:  reshape ile dizinin şeklini değiştirebiliriz. Not: (Toplam eleman sayısı değişmez.)

d3 = np.arange(10) #0,1,2,3....,9 toplam 10 sayı
print("d3:   ", d3) #d:    [0 1 2 3 4 5 6 7 8 9] şeklinde yazdırır. Tek boyutlu bir dizi oluşturdu.
d4 = np.arange(0,30,2) #0,dan başla 30, a kadar 2'şer 2'şer git.
print("d4:   ", d4) #d:    [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28] yazdırır.

#YENİ: 1 BOYUTLU DİZİYİ 2 BOYUTLU YAPMAK:
try:
    d5 = d3.reshape(3,4) #OLUŞACAK MATRİS 3 SATIR 4 SÜTUN OLSUN.
    print("d5:  ", d5.shape) #HATA VERECEK!!: HER DİZİYİ İTEDİĞİMİZ GİBİ AYIRAMAYIZ MANTIKEN!!!
except ValueError:
    print("HATA VERECEK!!: HER DİZİYİ İTEDİĞİMİZ GİBİ AYIRAMAYIZ MANTIKEN!!!")
d6 = dizi.reshape(2,3)
print(d6) #RESHAPED SEQUENCE MATRİS FORMU ALIR
print(d6.shape) #MATRİSİN (SATIR,SÜTUN) BİLGİSİNİ YAZAR

#YENİ: HAZIR MATRİSLER: (zeros, ones, eye)
# zeros(shape): sıfırlardan oluşan bir dizi
# ones(shape): birlerden oluşan bir dizi
# eye(n): nxn birim matris oluşturur. (koşegen 1, diğerleri 0)#
z = np.zeros((3,3))
o = np.ones((3,3))
e = np.eye(3) #3x3 birim matrix
print(z)
print(o)
print(e)
#NOT:  print(e) [[1. 0. 0.] Şeklinde print eder. ÖRÜNTÜ BELLİ OLUYOR. 
#                [0. 1. 0.]
#                [0. 0. 1.]] #


#YENİ:  İNDİSLEME
# NumPy dizilerinde python listeleri gibi indexleme yapabiliriz. 2 boyurlu dizilerde,
# dizi[satır,sütun] şeklinde veriye erişim sağlanabilir.#

#küçük alıştırma yaptım kendime. Diziyi elle oluşturmak yerine dönüştürücem:
dizi1 = np.arange(10,91,10) #10,20,...90 olarak 1 boyutlu dizi oluşturur
redizi1 = dizi1.reshape(3,3) #102030,405060,708090 diye alt alta matris çıkaracak:
print(redizi1.shape) #sağlama: 3,3 olduğunu söyledi
print(redizi1) #[[10 20 30] ŞEKLİNDE PRİNT ETTİ ARTIK DİZİM HAZIR ***
#                [40 50 60]
#                [70 80 90]#
print("(0,0) konumundaki eleman (birinci sütun birinci satır): ", redizi1[0,0]) #10 printler****
print("BİRİNCİ SATIR (0):   ", redizi1[0])

#YENİ:  DİLİMLEME
#Bir kısmını görmek için kullanılan bir metottur.
#YENİ:  SADECE BİR YERE KADAR OLAN SATIRLARI GÖRMEK İÇİN: dizi[satır:satır] yapılır#
print("satırlar: ",redizi1[0:2]) #ilk 2 satırı gösterecek** (0. ve 1. satırlar) 102030,405060
#YENİ:  SADECE SÜTUNDAKİ DEĞERLER İÇİN: dizi[:,sütun]
print("sütun değerleri: ",redizi1[:,1]) #sadece 2. sütunun (ortadaki) değerlerini gösterecek 20,50,80

#YENİ: TEMEL İSTATİSTİKLER (MİN MAX SUM MEAN VAR STD)
print("min: ",redizi1.min())
print("max: ",redizi1.max())
print("mean: ",redizi1.mean())
print("sum: ",redizi1.sum())
print("varyans: ",redizi1.var()) #ne olduğunu bilmiyorum
print("standart sapma: ",redizi1.std()) #ne olduğunu bilmiyorum
