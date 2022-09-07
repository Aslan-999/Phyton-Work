



















# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]

# # user = input("Istifadeci adinizi daxil edin : ")

# # print(users[0]['username'])



# for i in users:
#     username = input("Istifadeci adinizi daxil edin : ")
#     if not username == users[0]['username']:
#         print("istifadeci adi duzgun deyil")
#         break
#     elif username == users[0]['username']:
#         password = input("sifrenizi daxil edin : ")
#     elif password == users[0]['password']:



user_info = {
    'firstname': 'Elvin',
    'lastname': 'Huseynov',
    'username': 'elivin_h_ov',
    'password': '12345',
    'birthday': '19-08-1997'
}

new_info = input("Melumati daxil edin: ")

new_infoup = new_info.split(", ")

info = [i.split() for i in new_infoup]

info = dict(info)

user_info.update(info)

print(user_info)