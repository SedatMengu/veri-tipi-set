# set veri tipinin en önemli özellikleri her elemandan 1 tane olmsası ve indexlenme özelliğinin olmamasıdır.
# süslü parantezler içinde yazılır.

set ={"konya","karaman","aksaray"}

print(type(set))
# <class 'set'>

# önemli not: set elemanının listelerinde index olmadığı için her print ifadesinde print ekranı yeniden düzenlenir.

print(set)
# / {'konya', 'karaman', 'aksaray'}
print(set)
# {'karaman', 'aksaray', 'konya'}

print(dir(set))

# 1  - add () metodu
# 2  - clear () metodu
# 3  - copy () metodu
# 4  - difference () metodu
# 5  - difference_update () metodu
# 6  - discard () metodu
# 7  - intersection () metodu
# 8  - intersection_update () metodu
# 9  - isdisjoin () metodu
# 10 - tissubset () metodu () metodu () metodu
# 11 - issuperset () metodu
# 12 - pop () metodu
# 13 - remove () metodu
# 14 - symmetric_difference () metodu
# 15 - symmetric_difference_update () metodu
# 16 - union () metodu
# 17 - update () metodu