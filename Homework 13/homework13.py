

# ************************************************HOMEWORK 13**********************************************************

# **********************************************ERROR HANDLING*********************************************************


try:
    animals = input('Heyvan adini girin: ').split(', ')

    prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }

    result = sum(map(lambda animal: prices[animal], animals))
    if int(len(animals)) >= 10 or int(len(animals)) <= 3:
        raise ValueError("Girilən heyvan sayı 3'dən az və 10'dan çox olmamalıdır")
except ValueError as a:
    print(a)
except KeyError as message:
    print('Axtardığınız heyvan mövcud deyil!',message)
except SyntaxError:
    print("Sintaksis qaydası pozulub")
except Exception as message:
    print('Bilinməyən xəta baş verdi',message)
else:
    print('Umumi qiymet:', result)
    