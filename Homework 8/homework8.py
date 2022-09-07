# ***********************TASK ONE************************

# n1 = 15
# n2 = 13

# print('%s + %s = %s' % (n1,n2,n1+n2))



# ***********************TASK TWO************************

# userData = [
#     {
#         'debt': 12543,
#         'payed': 341.346742,
#         'payed_percent': 0.027214122777644904,
#         'card_number': '5326-6644-1234-6432',
#         'first_name': 'Akif',
#         'last_name': 'Serifov',
#         'father_name': 'Elekber',
#     }
# ]

# user = userData[0]

# print("Hormetli {first_name:.1}. {father_name:.1}. {last_name} sizin {card_number:*<20.9} \
# nomreli kartiniza {payed:.2f}AZN odenis edildi.\nUmumi {debt:,}AZN teskil eden borcunuzdan \
# {payed_percent:.2%} borc silinmisdir.".format_map(user))





# ***********************TASK THREE************************



# for i in range(0,30):

#     print(f"{i} {i:b} {i:o} {i:x}")





# ***********************TASK FOUR************************




# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ['inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek']
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# text = f"""
# Axtarilan Heyvan: {animal}
# Fermadaki {animal} sayi:  {farm.count(animal)}
# Diger heyvanlara olan faizi: {farm.count(animal) / len(farm):.2%}
# {animal} umumi qiymeti: {farm.count(animal) * qiymetler.get(animal)} AZN
# """

# print(text)











# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)


user_inp = int(input("Eded daxil edin: "))

for i in str(user_inp):
    if not i > 9:
        i*i
        
print(type)
        
