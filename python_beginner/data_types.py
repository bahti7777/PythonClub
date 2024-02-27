# 8 основных типов данных

# 1) int- целый числовой тип данных:
#  a) float - числа с плавающей точки 256.50
#  b) complex-числа с буквенным выражением (12345123n)
# 2) str-строковый тип данных -"Строка"
# 3) bool-булевый тип данных/ логический (True/Falce)
# 4) lict-список[]
# 5) tuple-кортеж/ неизменяемый список()
# 6) set-множство{}
# 7) dict-словарь{}
# 8) NoneType-тип данных для обознечения отсутствия значения (None)


#изменямые виды данных (moutable)
# list
# dict
# set

#print("Htllo World") # print() функция для вывщда содеожимого на терминал
#name=input ("Ведите ваше имя")
#print("Hello,"+ name)

print("Привет")

str1 = 'Hello'
str2 = 'World'
print(str1 + str2)

frog = 'Quag'
print(frog * 3) # QuagQuagQuag 

""" Функции и методы строк  
 """
greeting = "Good Evening"

#print(len(greeting))
#len(x) # возвращяет кол-во элементов 

# greeting = "Good Evening"
# print(dir(greeting)) 
# dir(x) - возвращяет список методов предонного объекта

# Метод - функция, принадлежащая определенному типу данных, и может быть вызвана только через объект 

""" my_str = 'Hello#World'
print(my_str.lower()) # hello#world
print(my_str.upper()) # HELLO#WORLD
print(my_str.replace('#', ' ')) # Hello World

my_str2 = '      hello world       '

my_str2.title() #Hello World
my_str2.capitalize() # Helo World
my_str2.count("l") # 3
print(my_str2.strip()) # Удаляет лишние пробелы
my_str2.lstrip()
my_str2.rstrip() 

my_str2 = '      hello world       '

print(my_str2.strip('!'))"""

my_str3 = "my new String"

my_str3.isalpha() # True
my_str3.isdigit() # False
my_str3.isalnum() # False
my_str3.startswith('M') # True
my_str3.endswith('M') # False
# Изменяемые (mutable):
# list
# dict
# set


str1 = 'Hello'
str2 = 'World'
# print(str1 + str2) # HelloWorld


frog = 'Quak'
# print(frog * 3) # QuakQuakQuak


""" Функции и методы строк """

greeting = "Добрый вечер"

# print(len(greeting))
# len(x) - возвращает количество элементов

# print(dir(greeting))
# dir(x) - возвращает список методов переданного объекта


# Метод - функция, принадлежащая определенному типу данных, и может быть вызвана только через объект

my_str = 'Hello#world'

# print(my_str.lower()) # hello#world
# print(my_str.upper()) # HELLO#WORLD
# print(my_str.replace('#', ' ')) # Hello world
# print(my_str.split('#')) # делит строку по разделителю и возвращает список

my_str2 = '!!!hello world  !!!'

my_str2.title() # Hello World
my_str2.capitalize() # Hello world
my_str2.count("l") # 3
# print(my_str2.strip()) # удаляет лишние пробелы
my_str2.lstrip()
my_str2.rstrip()

# print(my_str2.strip('!'))


my_str3 = 'My new String'

my_str3.isalpha() # True
my_str3.isdigit() # False
my_str3.isalnum() # False
my_str3.startswith('M') # True
my_str3.endswith('M') # False


# in

my_str4 = 'Hello World'

# 'Hello' in my_str4 # True


name = input('Имя: ')
party = input('Вечеринка: ')

invite1 = 'Дорогой %s, приглашаем тебя на %s' % (name, party)
print(invite1)

invite2 = 'Дорогой {a1}, приглашаем тебя на {b2}'.format(a1=name, b2=party)
print(invite2)

invite3 = f'Дорогой {name}, приглашаем тебя на {party}'
print(invite3) 

string= 'Python'

