# 1. kart = “5382-1739-9201-9017” bank kartı məlumatını daşıyan variablein ilk 8 nömrəsini ulduzlanmış şəkildə print edin.

# kart = '5382-1739-9201-9017'

# kart8 = kart[9:]

# end = "*"*8 + kart8

# print(end)

# -------------------------------------------------------------------------------------------------------------------------------------------

# 2. 15 ədədinin 4-ə bölünməsindən çıxan qalığın kubunu tapın



# a = 15 
# b = 4

# calc = (15 % 4)**3

# print(calc) # 27

# -------------------------------------------------------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------------------------------------------------------


# 3. 256.91872 ədədinin nöqtədən sonrakı və əvvəlki 2-ci ədədə qədər yuvarlaqlaşdırın. (2 fərqli cavab almalısınız)


# eded = round(256.91872, 2)

# print(eded) # 256.92

# eded2 = round(256.91872, -1)

# print(eded2) # 260.00


# -------------------------------------------------------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------------------------------------------------------


# 4. 34 ədədinin əvvəlinə string metodlarının köməyilə 3 sıfır əlavə edin


# eded = "34"

# print(eded.zfill(5)) #00034



# -------------------------------------------------------------------------------------------------------------------------------------------

# 5. Girilən floatın tam hissəsinin neçə ədəddən ibarət olduğunu göstərən program hazırlayın. Bunun üçün input və print funksiyalarından istifadə edin.



# -------------------------------------------------------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------------------------------------------------------

# 6. Girilən websaytın əvvəlindəki https:// və sonundakı .com hissələrini silən və istifadəçiyə göstərən program hazırlayın. (input və print ilə)



# user = input("Web saytinizi daxil edin :")
# website = user.removeprefix('https://').removesuffix('.com')

# print(website)
# print('Elmeddin '*10)
# print('Menim adim ' + '*'*10)

# -------------------------------------------------------------------------------------------------------------------------------------------





# -------------------------------------------------------------------------------------------------------------------------------------------

# 7. İstifadəçi yazacağınız inputlar vasitəsilə dəyişmək istədiyi sözü, nəyə dəyişmək istədiyini və mətni daxil edəcək, qurduğunuz program isə mətndə həmin sözləri dəyişib istifadəçiyə print edəcək

soz = input("Cumlenizi daxil edin : ") # Men C# oyrenirem
deyisilen= input("Deyisecek soz : ") # C#
deyisen = input("Hansi sozle : ") # Phyton

netice = soz.replace(deyisilen , deyisen)

print(netice) # Men Phyton oyrenirem

 
# ------------------------------------------------------------------------------------------------------------------------------------------


