# 1) Создать переменную типа String
String = "Nikita"

# 2) Создать переменную типа Integer
Integer = 25

# 3) Создать переменную типа Float
Float = 65.5

# 4) Создать переменную типа Bytes
Bytes = bytes([250, 10, 75])

# 5) Создать переменную типа List
List = list('Yami_yami')

# 6) Создать переменную типа Tuple
Tuple = tuple('Pasta')

# 7) Создать переменную типа Set
Set = set('Yami_yami')

# 8. Создать переменную типа Frozen set
Frozen_set = frozenset('Yami_yami')

# 9) Создать переменную типа Dict
Dict = {1:'December', 2:'January', 3:'February'}
    # or  Dict = dict({1:'December', 2:'January', 3:'February'})

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
Data_Type = [String, Integer, Float, Bytes, List, Tuple, Set, Frozen_set, Dict]
for i in Data_Type:
    print(i, type(i))

# Создать 2 переменные String, создать переменную в которой конкантенируете эти переменные. Вывести в консоль.

name = 'Nikol '
surname = 'Kidman'
actress = name + surname
print(actress)


print(String, Integer, sep=', ')
print(String, Integer, sep=' + ')