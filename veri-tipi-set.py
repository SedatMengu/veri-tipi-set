# set veri tipinin en önemli özellikleri her elemandan 1 tane olmsası ve indexlenme özelliğinin olmamasıdır.
# süslü parantezler içinde yazılır.

set ={"konya","karaman","aksaray"}

print(type(set))
# <class 'set'>

# önemli not: set elemanının listelerinde index olmadığı için her print ifadesinde print ekranı yeniden düzenlenir.

print(set)
# / {'konya', 'karaman', 'aksaray'}
print(set)
# / {'karaman', 'aksaray', 'konya'}

print("trabzon" in set) # / True ya da False olarak döner.

print(dir(set))

# 1  - add () metodu , bir küme nesnesine verilen bir öğeyi ekler. Eğer öğe zaten kümede mevcut ise bir değişiklik yapılmaz.
set ={"konya","karaman","aksaray"}
set.add("tokat")
print(set)
# / {'aksaray', 'konya', 'tokat', 'karaman'} (her çalışmada sıralama farklı)


# 2  - clear () metodu bir setin tüm elemanlarını siler ve None döner
set ={"konya","karaman","aksaray"}
clearset = set.clear()
print(type(clearset))
print(clearset)
# / <class 'NoneType'>
# / None


# 3  - copy () metodu bir kümenin kopyasını oluşturur. Bu metot, orijinal kümenin kopyasını oluşturduğu için, iki kümenin birbirinden bağımsız olarak değiştirilmesine izin verir.
set1 = {1, 2, 3}
set2 = set1.copy()
set1.add(4)
print(set2) 
# / {1, 2, 3}



# 4  - difference () metodu bir setin diğer setten farkını döndürür. Yani, A kümesinin B kümesinden farkını alarak A-B kümesini oluşturur.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = A.difference(B)
print(C)
# / {1, 2, 3}


# 5  - difference_update () metodu



# 6  - discard () metodu remove dan tek farkı hata döndürmüyor olmasısıdr.
set ={"konya","karaman","aksaray"}
set.discard("ankara")
print(set)
# / {'aksaray', 'konya', 'karaman'} listede bulamadığı için silemedi , hata da vermedi.


# 7  - intersection () metodu bir set'in başka bir set ile kesişim kümesini oluşturmak için kullanılır.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print(intersection_set)
# / ( 4 , 5 )


# 8  - .intersection_update () metodu



# 9  - isdisjoin () metodu iki kümenin kesişiminin boş olup olmadığını kontrol eder. Eğer kesişim boş ise True döndürür, aksi takdirde False döndürür.
a = {1, 2, 3, 4}
b = {5, 6, 7, 8}
c = {3, 4, 5}

print(a.isdisjoint(b)) 
print(a.isdisjoint(c)) 
# / True
# / False


# 10 - tissubset () metodu  bir setin diğer setin alt kümesi olup olmadığını kontrol eder. Alt küme ise, bir setin elemanlarının başka bir sette de bulunduğu anlamına gelir. (kapsıyor mu ?)
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7, 8}

print(set1.issubset(set2)) # True
print(set2.issubset(set1)) # False
print(set1.issubset(set3)) # False



# 11 - issuperset () metodu bir kümenin diğer kümenin üst kümesi olup olmadığını kontrol eder. Yani, bir küme, diğer kümenin tüm elemanlarını içeriyor mu kontrol eder. Eğer öyleyse, True değeri döndürür, aksi takdirde False değeri döndürür.
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {2, 4, 6}

result = set1.issuperset(set2)
print(result)  # True

result = set2.issuperset(set1)
print(result)  # False



# 12 - pop () metodu kümeden rastgele bir öğe çıkarır ve bu öğeyi kümeden kaldırır. Eğer küme boş ise KeyError hatası fırlatır. Metodun kullanımı aşağıdaki gibidir:
my_set = {1, 2, 3, 4, 5}
popped_item = my_set.pop()
print(popped_item)  # örn. 3
print(my_set)  # örn. {1, 2, 4, 5}



# 13 - remove () metodu bir kümeden belirtilen bir öğeyi kaldırır. Eğer kümede öğe yoksa KeyError hatası verir.
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set) 
# / {"apple", "cherry"}


# 14 - symmetric_difference () metodu



# 15 - symmetric_difference_update () metodu



# 16 - union () metodu bir set'e diğer bir set veya iterable'ın elemanlarını ekler ve sonuç olarak yeni bir set oluşturur.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(union_set)
# / {1, 2, 3, 4, 5, 6, 7, 8}


# 17 - update () metodu