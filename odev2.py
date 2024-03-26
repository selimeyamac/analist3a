 # -*- coding: utf-8 -*-

# 4 Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi=int(input("Sayıyı Girin : "))
if sayi > 1:

   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayı Değildir.")
           break
   else:
       print(sayi," Asal Sayıdır.")
 
else:
   print(sayi," Asal Sayı Değildir.")


#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
birinciSayi = int(input("Birinci Sayiyi Giriniz : "))
ikinciSayi = int(input("İkinci Sayiyi Giriniz : "))
 
if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi
for i in range(1,kucuksayi+1):
    if (birinciSayi % i==0) and (ikinciSayi%i ==0):
        ebob = i
        ekok = (birinciSayi*ikinciSayi)//ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)


#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
fibonacci=[1,1]  # İlk iki elemanı 1'e eşit olan Fibonacci serisi
while len(fibonacci)<20:  # En az 20 elemanlı olana kadar devam edecek
    next_num= fibonacci[-1]+fibonacci[-2] # Son iki elemanın toplamı bir sonraki elemanı oluşturur
    fibonacci.append(next_num)  # Yeni elemanı listeye ekle
print(fibonacci)

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi = int(input("Sayi Giriniz:"))
 
toplam=0
 
for i in range(1,sayi):
    if(sayi%i == 0):
        toplam +=i

if(sayi == toplam):
    print("Mükemmel Sayidir.")
else:
    print("Mükemmel Sayi Degildir")

#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
def asal_carpanlara_ayir(sayi):
    asal_carpanlar = []
    bolen = 2
    while sayi > 1:
        while sayi % bolen == 0:
            asal_carpanlar.append(bolen)
            sayi //= bolen
        bolen += 1
    return asal_carpanlar
girilen_sayi = int(input("Lütfen asal çarpanlarına ayırmak istediğiniz sayıyı giriniz: "))
asal_carpanlar = asal_carpanlara_ayir(girilen_sayi)
print("Asal Çarpanlar:", asal_carpanlar)
