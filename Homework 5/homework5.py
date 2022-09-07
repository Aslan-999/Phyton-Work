
                            #   LIST, TUPLE & LIST COMPREHENSIONS HOMEWORK




# 1. Aşağıdakı listdən istifadə edərək 6-ya bölünən ədədləri çıxarıb 
# onların kvadratından yeni bir list hazırlayın

# list = [3, 12, 48, 7, 57, 41, 76, 62, 16, 48, 59, 53, 60, 79, 71, 81, 88, 26, 45, 72, 25, 65, 53, 88, 79, 34, 42, 40, 45, 92, 52, 85, 90, 16, 37, 50, 96, 67, 7, 59, 3, 41, 40, 58, 83, 16, 47, 23, 5, 22]

# new_list = []
#                                                          STANDART
# for i in list:
#     if i%6==0:
#         new_list.append(i**2)

# print(new_list)


# new_list = [i**2 for i in list if i%6==0]
#                                                        COMPREHENSIONS
# print(new_list)



# --------------------------------------------------------------------------------------------------------------

# 2.  -100-dən müsbət 100-ə qədər ədədlər arasında 7-yə bölünən ədədlərin 3-ə vurulmasından 
# ibarət bir list qurun. Bunun üçün range və list comprehensions istifadə edin.

# numbers = range(-100,101)

# result = [x*3 for x in numbers if x%7==0]

# print(result)



# --------------------------------------------------------------------------------------------------------------




# 3. data = (1, 2, 3, True, False, 3.3) bu datanı buna çevirin ('asdf', 1, 2, 3, True, False, 3.3, (1, 2))

# data = (1, 2, 3, True, False, 3.3)

# data_2 = ('asdf'),

# data_3 = ((1,2),)

# result = data_2 + data + data_3

# print(result)




# --------------------------------------------------------------------------------------------------------------





# 4. Bildiyimiz kimi dir() funskyası argumentə yazılan datanın metod və attributlarının list daxilində
#  stringlər şəklində adını göstərir. List comprehensions ilə ətrafında cüt altdan xət olan
#  metod adlarının çıxarılmış yeni bir list hazırlayın

# methods = dir(str)

# methods_up = [i for i in methods if not i.endswith("__")]

# print(*methods_up, sep="\n")




# --------------------------------------------------------------------------------------------------------------



#                                  DICTIONARY & DICT COMPREHENSION




# fruits = ['alma', 'heyva', 'nar', 'saftali']

# result = {i:len(i) for i in fruits}

# print(result)

