 # -*- coding: utf-8 -*-

# 4 Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

def asalSayi(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    num = int(input("Lutfen bir sayi girin: "))
    if asalSayi(num):
        print(num, "bir asal sayidir.")
    else:
        print(num, "bir asal sayi değildir.")
except ValueError:
    print("Lütfen geçerli bir sayi girin!")


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