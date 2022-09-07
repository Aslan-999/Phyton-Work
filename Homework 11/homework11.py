# ---------------------------TASK 1-----------------------------------------

# Aşağıdakı düsturladan 10-unu seçib, valueləri lambda ilə yazılmış 
# funksya olan, 10 itemdən ibarət dictionary düzəldin. Daha sonra həmin funksiyaları istifadə edin.


# physic = {
#     'F' : lambda m, a: m * a,
#     's'  : lambda a, t: a * (t**2) / 2,
#     'W' : lambda F, s: F * s,
#     'p' : lambda m , V: m / V,
#     'Ep' : lambda m , g , h : m * g * h,
#     'T' : lambda f : 1 / f,
#     'I' : lambda q, t : q / t,
#     }


# print(physic.get('F')(4,5))   







# ---------------------------TASK 2-----------------------------------------




# Lambda ilə factorial hesablayan recursive function hazırlayın.


    
# factorial = lambda n : n * factorial(n - 1) if n > 1 else 1
    
# print(factorial(1))







# ---------------------------TASK 3-----------------------------------------


# Dictionary datalarını düzləşdirən bir recursive funksiya hazırlayın. 


# letdict = {'a': 1, 'v': {'b': 2}, 'c': {'f': 3, 'c': 3, 'h': {'r': 5}, 'p': 3}, 'y': 9} 


# def flat(d):
#     for i in letdict:
#         if type(i) != dict:

# # print(type(letdict.get('v')))

# print(new_dict)



# ---------------------------TASK 4-----------------------------------------




# Aşağıdakı ədədlər arasında rəqəmlərinin cəmi ən yüksək olanı çıxarın.



# numbers = [85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]




# print(max(numbers, key=lambda number: sum(int(i) for i in str(number))))



# print(max_sum(numbers))

# for i in numbers:
#     print(sum(list(i)))




# ---------------------------TASK 5-----------------------------------------



# Şaxta baba uşaqlara hədiyyələr paylayır, ancaq bu təsadüfi şəkildə olduğu üçün bəzi ədalətsizliklər yaranır 
# və uşaqlar şikayət üçün list hazırlamaq istəyirlər. Bu listi hazırlamaq üçün sizə müraciət edib, 
# bahadan ucuza kimə hansı hədiyyəni və hansı qiymətə olduğunu yazmağınızı istəyiblər. Hədiyyələr və uşaqların 
# adlarının indeksləri eynidir. Datalardan istifadə edərək məlumatı hazırlayın.




# children = ['Arif', 'Babek', 'Hesen', 'Rufet', 'Sahin', 'Eldeniz', 'Turan', 'Sahmar', 'Kamal', 'Ruslan']
# gifts = ['Ball', 'Iphone', 'Bicycle', 'Ball', 'Piano', 'Bicycle', 'Socks', 'Play Station', 'Ball', 'Socks']
# prices = {'Ball': 10, 'Iphone': 1100, 'Bicycle': 500, 'Piano': 1500, 'Sock': 10, 'Play Station': 1200}

# print(f'{children[5]}, {prices.get(gifts[5])}AZN deyerinde {gifts[5]} goturub')
    
    
    
