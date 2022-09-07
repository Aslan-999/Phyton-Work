# user_inp = input("Zehmet olmasa metni daxil edin: ").lower()

# result = ''

# for char in user_inp:
#     if 97 <= ord(char) <= 122:
#         result += str(ord(char)- 96)
#     else:
#         result += char
#     result += ','

# print(result)


# user_int = input("Enter Something: ")

# print(' '.join([bin(ord(i))[2:] for i in user_int = input("Enter Something: ")]))

user_rgb = input("Bura nese yazin: ")

user_rgb = user_rgb[11:-1]

r,g,b = [hex(int(i))[2:].zfill(2) for i in user_rgb.split(", ")]

print("color: ", r, g, b, sep='')