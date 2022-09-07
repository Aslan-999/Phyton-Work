
baliqlar = {
    'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}





# *********************************************TASK 1*************************************************




# 1. Quşların xüsusiyyətlərinə "2 ayaq" əlavə edin.

# quslar.add('2 ayaq')

# print(quslar)







# *********************************************TASK 2*************************************************





# 2. Balıqların xüsusiyyətlərindən "4 ayaq" məlumatını çıxarın

# baliqlar.remove('4 ayaq')

# print(baliqlar)






# *********************************************TASK 3*************************************************





# 3. Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın

# print(amfibialar.intersection(cuculer))







# *********************************************TASK 4*************************************************




# 4. Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın

# print(amfibialar.difference(baliqlar))







# *********************************************TASK 5*************************************************





# 5. Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın

# for key, values in sinifler.items():
#     if baliqlar.isdisjoint(values) == True:
#         print('Baliqlarla ortaq ceheti olmayan sinif', key)
#     else:
#         print('Baliqlarla ortaq ceheti olmayan sinif yoxdur')
#         break








# *********************************************TASK 6*************************************************





# 6. Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın

# max_ortaq = 0


# for key, values in sinifler.items():
#     if values == quslar:
#         continue
#     ortaq_cehet = (quslar.intersection(values))
#     if len(ortaq_cehet) > max_ortaq:
#         max_ortaq = len(ortaq_cehet)
#         anim_class = key

# print('Quslarla en cox ortaq cehete sahib olan sinif {}. Ortaq cehetlerin sayi {}'.format(anim_class,max_ortaq))









# *********************************************TASK 7*************************************************





# 7. İstifadəçi input ilə sizə bəzi özəlliklər girəcək. 
# Siz həmin özəlliklərə əsasən heyvanın hansı sinifə aid ola biləcəyini təxmin edən kod yazın.

# user = set(input('Axtardiginiz sinifin xususiyyetlerini girin: ').split(', '))
# found = False
# anim_class = ''

# for key, values in sinifler.items():
#     if user.issubset(values) == True:
#         found = True
#         anim_class += key + ' '
    
        
# if found == True:
#     print('Sizin axtardiginiz sinif {}ola biler'.format(anim_class))
# if found == False:
#     print('Axtardiginiz ozelliklerde sinif tapilmadi')