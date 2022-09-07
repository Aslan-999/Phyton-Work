# 1. ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci'] şəklində fermaya
#  sahib bir fermer bizdən bəzi köməkliklər istəyir. Fermerə kömək etmək üçün aşağıdakı tapşırıqları
#  yerinə yetirin.


ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']

# a. fermada kecinin sirasini tapin 

# print(ferma.index("keci"))


# ---------------------------------------------------------------


# b. fermadaki heyvanlari ad sirasina gore siralayin 

# ferma.sort()
# print(ferma)


# ---------------------------------------------------------------


# c. fermadan 1 at cixardib, en soldan 1 toyuq elave edin

# ferma.remove("at")
# ferma.append("toyuq")

# print(ferma)


# ---------------------------------------------------------------


# d. en soldan 1 keci elave edin

# ferma.insert(0, "keci")
# print(ferma)



# ---------------------------------------------------------------


# e. fermanin yarisini dinamik bir sekilde silin

# del ferma[0:(int(len(ferma)/2))]

# print("Yarisi silindi : ",ferma)



# ---------------------------------------------------------------




# f. Yeni gələn ['at', 'qoyun', 'inek', 'inek', 'qoyun'] heyvanları fermaya əlavə edin

# newanimals = ['at', 'qoyun', 'inek', 'inek', 'qoyun']

# ferma.extend(newanimals)

# print(ferma)



# ---------------------------------------------------------------




# g. Fermadakı heyvanları 3 qatına çıxarın

# bigfarm = ferma*3

# print(bigfarm)



# ---------------------------------------------------------------




# h. Fermadakı heyvanları tərsinə sıralayın

# ferma.sort(reverse=True)

# print(ferma)




# ---------------------------------------------------------------



# i. Fermadakı ineklerin sayının ümumi fermanın neçə faizi olduğunu tapın

print(int(ferma.count("inek")) * 100 // int(len(ferma)))



# ---------------------------------------------------------------



# j.Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verin

# ferma_x = ferma.copy()

# print(ferma_x)


# ---------------------------------------------------------------



# k. Fermada təmir işi getməlidi, heyvanları çölə çıxarmaq üçün fermanı təmizləyin

# print(ferma.clear())


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------



# 2. Aşağıdakı result listinin 0-cı indexinə numbers listi daxilindəki müsbət ədədlərin cəmini, 
# 1-ci indexə isə mənfi ədədlərin cəmini yerləşdirin. 


# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]



# ---------------------------------------------------------------



# 3. İstifadəçinin girdiyi ədədi tək ədədlərdən ibarət tərsinə çevirilmiş list şəklinə salın. 
# Listin bütün elementlərinin integer olmasına diqqət edin.

# user_num = input("Ededleri daxil edin: \n")

# user_list = []

# for num in user_num:
#     user_list.append(int(num))

# print(user_list[::-1])



# ---------------------------------------------------------------



# 4. numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62] 
# list içərisindəki ən böyük və ən kiçik ədədi dinamik şəkildə tapın.

# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

# max_num = max(numbers)
# min_num = min(numbers)

# print("En boyuk eded :", max_num ,"\nEn kicik eded :", min_num)




# ---------------------------------------------------------------



# 5. Aşağıda tələbələrin semestr nəticələri qeyd edilmişdir. 
# Buna əsasən qeyd olunmuş statistik məlumatları eyni anda print edin.

# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]

# # a. Tələbə sayı

# stu = len(r)

# # b. Ümumi ortalama.

# ortalama = sum(r) / stu


# # c. Kəsilən tələbələrin ümumi faizi (51- qiymət alanlar)

# # d. Yüksək nəticə göstərən tələbələrin ümumu faizi (80+ qiytət alanlar)

# kesilen = []

# yuksek = []

# for char in r:
#     if char >= 81:
#         yuksek.append(char)
#     elif char < 51:
#         kesilen.append(char)

# kesilen_faiz = int(len(kesilen) * 100 / stu)

# yuksek_faiz = int(len(yuksek) * 100 / stu)



# print(stu, "telebeden", len(kesilen), "nefer imtahandan kesildi. Bu umumi telebelerin", 
# kesilen_faiz,"%-ni", "teskil edir.\n",len(yuksek),"nefer telebe ise yuksek netice ile bitirdiler.", 
# "Yuksek netice gosteren telebeler umumi qrupun", yuksek_faiz,"%-ni teskil edir. \nQrupun umumi ortalamasi ",ortalama)


# result = """
# Telebelerin sayi : {}
# Umumi ortalama : {}
# Kesilen telebelerin sayi : {}
# Kesilenlerin 
# """

