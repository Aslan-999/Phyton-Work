# 1. İstifadəçinin girdiyi ədədin həm 7 həm 3 həm də 8-ə eyni anda bölünüb bölünmədiyini istifadəçiyə bildirən kod yazın.

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# ----------------------------------------------------------------------------------------------------------




# 2. İstifadəçinin girdiyi şəxsiyyət vəsiqəsinin düzgünlüyünü yoxlayan kod yazın. Şəxsiyyət vəsiqəsi:
    # 1. Şəxsiyyət vəsiqəsi 10 characterdən ibarət olmalıdır. 
    # 2. Bunun ilk 3 characteri hərhansı bir ölkənin qısaltması olmalıdır. Misal AZE, TUR, USA. Həmin qısaltmalar böyük hərflə yazılan ingilis şriftləridir. 
    # 3. Daha sonrakı 7 character isə ancaq rəqəmlərdən ibarət olmalıdır


# user_pasp = input("Vesiqenin seriya nomresini daxil edin : ")

# if len(user_pasp) > 10 & len(user_pasp) < 10:
#     print("Nomrenin uzunlugu 10'dan boyuk ve kicik ola bilmez'")
# elif not user_pasp[2].isalpha() & user_pasp[2].isupper():
#     print("Ilk 3 character mutleq boyuk herf olmalidir")
# elif not user_pasp[3:].isnumeric():
#     print("Son 7 character yalniz reqemlerden ibaret olmalidir")
# else:
#     print("tesdiq olundu")


# --------------------------------------------------------------------------------------------------------------

# 3. Bank sistemi hazılayırsınız və istifadəçinin aldığı kredit miqdarına görə ödəyəcəyi yekun borcu hesablamalsınız. Faizlər aşağıdakı kimidir:
#     1. 2000 AZN altına kredit verilmir
#     2. 2000 - 10000 AZN arası 5 faiz
#     3. 10000 - 50000 AZN arası 4 faiz
#     4. 50000 - 200000 AZN arası 3 faiz
#     5. 200000 - 500000 AZN arası 2 faiz
#     6. 500000 AZN yuxarısında kredit verilmir
    
#     Örnək hesablama 13000 kredit alan şəxs yekunda 13650 AZN ödəniş edəcək


# credit = input("Goturmek istediyiniz kredit miqdarini yazin : ") 

# result = int(credit)

# a = result * 0.05 + result
# b = result * 0.04 + result
# c = result * 0.03 + result
# d = result * 0.02 + result

# if 2000 > result:
#     print("Teessuf ki, 2000 AZN altinda kredit verilmir")
# elif 2000 <= result < 10000:
#     print("Sizin yekunda odeyeceyiniz mebleg :" + str(a))
# elif 10000 <= result < 50000:
#     print("Sizin yekunda odeyeceyiniz mebleg :" + str(b))
# elif 50000 <= result < 200000:
#     print("Sizin yekunda odeyeceyiniz mebleg :" + str(c))
# elif 200000 <= result <= 500000:
#     print("Sizin yekunda odeyeceyiniz mebleg :" + str(d))
# else:
#     print("Kredit verilmesi mumkun deyil")




# --------------------------------------------------------------------------------------------------------------------------


# 4. İstifadəçinin şifrəsinin düzgün olub olmadığını yoxlayan kod yazın. Şifrə aşağıdakı qaydalara uymaldır. Əgər uymazsa istifadəçiyə səhvini print edərək bildirin:
#     1. Ən az 8 ən çox 40 characterdən ibarət olmalıdır
#     2. Ancaq ingilis sriflərindən ibarət olmalıdır
#     3. Ancaq hərf və rəqəmlərdən ibarət olmalıdır
#     4. Mütləq şəkildə ən az bir böyük və bir kiçik hərf olmalıdır
    # 5. Mütləq şəkildə ən az 1 hərf və ən az 1 rəqəm olmalıdır


# password = input("Sifrenizi daxil edin : ")

# if not 8 <= len(password) <= 40:
#     if len(password) < 8:
#         print("Sifreniz 8'den kicik ola bilmez")
#     else:
#         print("Sifre 40'dan boyuk ola bilmez")    
# elif not password.isascii():
#     print("Ingilis sriftlerinden ibaret olmalidir")
# elif not password.isalnum():
#     print("Ancaq herf ve reqemlerden ibaret olmalidir")
# elif password.isalpha():
#     print("En az 1 reqem olmalidir") 
# elif password.isnumeric():
#     print("en az 1 herf olmalidir")
# elif password.islower():
#     print("En az 1 boyuk herf olmalidir")
# elif password.isupper():
#     print("En az 1 kicik herf olmalidir")
# else:
#     print("Sifre duzgundur")




# -----------------------------------------------------------------------------------------------------------------



counter = 0

while counter >= 100:
    counter -=1 
    counter
