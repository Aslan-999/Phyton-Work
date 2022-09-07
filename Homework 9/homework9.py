
# ------------------------------Task 1------------------------------



# user_inp = input("Cumleni daxil edin: ")

# def special_text(text):
#     result = ''
#     text = text.split()
#     for i in text:
#         i = i.capitalize()
#         for j in i:
#             if j.isupper():
#                 result += j
    
#     return result

# print(special_text(user_inp))





# ------------------------------Task 2------------------------------











# ------------------------------Task 3------------------------------





# def find_percent(first, second):
#     ferq = first - second
#     faiz = ferq * 100 // first
#     if faiz > 0:
#         return f'Qiymetde {faiz}% endirim olmusdur'
#     else:
#         return f'Qiymetde {abs(faiz)}% artim olmusdur'
        

# print(find_percent(100, 60))





# ------------------------------Task 4------------------------------




# eq = {'ə': 'e', 'ü': 'u', 'ç': 'ch', 'ş': 'sh', 'ı': 'i', 'ğ': 'gh', 'ö': 'o'}
# def ascii_letters(text):
#     result =''
#     for i in text.lower():
#         result += eq.get(i, i)
#     return result

# def lang_change(f):
#     def wrapper(*args, **kwargs):
#         result = f(*args, **kwargs)
#         result = ascii_letters(result)
#         return result()
#     return wrapper


# @lang_change
# def welcome(name, surname):
# 	return f'Salam hörmətli {name:.1}. {surname}, necəsiniz?'

# print(welcome('Ələmdar', 'Hacızadə'))






# ------------------------------Task 5------------------------------


# user_list = list(input('Ededleri girin: '))

# def max_min(list):
#     return int(max(list)) - int(min(list))

# print(max_min(user_list))




# ------------------------------Task 6------------------------------

# from math import inf 

# max = -inf
# min = inf

# numbers = [3,5,2,7,8,24,43,4,6]

# for i in numbers:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
        
# print(max - min)


# user = input("Yoxlanılacaq sözü daxil edin: ")

# count = 0

# for i in user:
#     if i == 'T' or i == 't':
#         count += 1


# if count == 1:
#     print("Cümlədə sadəcə 1 ədəd 't' hərfi var")
# elif count > 1:
#     print("Cümlədə birdən çox 't' hərfi var")
# else:
#     print("Cümlədə 't' hərfi yoxdur")



# l = ['1','2','3','4','5','6','7','8','9','0']

# pn = ''.join(l)


# print(f'({pn[:3]}) {pn[3:6]}-{pn[6:]}')

# myTuple = ("John", "Peter", "Vicky")

# x = " ".join(myTuple)

# print(x)


# user = input("")

# month = ['January', 'February', 'March', 'April', 'May', 'June', 'Jule', 'August', 'September', 'October', 'November' ,'December']


# if user in month[:3]:
#     print(user,'ilin 1. rubundedir')
# elif user in month[3:6]:
#     print(user,'ilin 2. rubundedir')
# elif user in month[6:9]:
#     print(user,'ilin 3. rubundedir')
# elif user in month[9:]:
#     print(user, 'ilin 4. rubundedir')








# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
        
# text = "The greatest victory is that which requires no battle"
    
# def reverseWords(str):
#     return " ".join(str.split(" ")[::-1])

# print(reverseWords(text))



# def printer_error(s):
#     errors = 0
#     count = len(s)
#     for i in s:
#         if i > "m":
#             errors += 1
#     return str(errors) + "/" + str(count)

# print(printer_error('qwerrtuuios'))


from hashlib import new


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

new_list = []

for i in a:
    if i in b:
        new_list.append(i)

for i in b:
    if not i in a:
        new_list.append(i)
        
print(new_list)