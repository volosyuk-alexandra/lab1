print('1. Вычислите сумму цифр введенного натурального числа.')
print('Введите число:')
N = int(input())
sum = 0

while N!= 0:
   p = N % 10
   sum = sum + p
   N = N // 10

print("Сумма цифр числа : \n", sum)

print('\n2. Ввести строку текста. Вывести на экран все слова палиндромы :')
def is_palindrome(word):
    return word == word[::-1]

text = input("Введите строку текста: ")

words = text.split()

palindromes = [word for word in words if is_palindrome(word)]

for palindrome in palindromes:
    print(palindrome)

print('\n3. Найдите произведение элементов списка с нечетными номерами.'
     'Найдите наибольший элемент списка, затем удалите его и выведите'
     'новый список. Выведите на экран три наибольших элемента.')

arr = [int(input('Введите элемент списка: '))
      for i in range(int(input('\nВведите длину списка: ')))]

print(f'Весь список: {arr}')

print(f'Произведение элементов списка:')
prod = 1
for i in range(len(arr)):
   if i % 2 != 0:
       prod *= arr[i]
print(prod)

sorted_arr = sorted(arr, reverse=True)

for i in range(3):
   print(f' ', i+1 ,'-й наибольший элемент : ', sorted_arr[i])

i = 0
while i < 3:
   max_number = max(arr)
   print(f'Максимальный элемент: ', max_number)
   arr.remove(max_number)
   print(f'Весь список: {arr}')
   i = i + 1

print('\n4. Даны два списка одинаковой длины. Необходимо создать из них'
     'словарь таким образом, чтобы элементы первого списка были'
     'ключами, а элементы второго — соответственно значениями нашего словаря.')

list1 = input("\nВведите элементы первого списка через пробел: ").split()
list2 = input("\nВведите элементы второго списка через пробел: ").split()

dictionary = dict(zip(list1, list2))
print(dictionary)

print('\n5. Реализуйте программу «Ювелирный магазин», которая будет включать в себя шесть '
      'пунктов меню. У вас есть словарь, где ключ – название изделия. Значение – список, '
      'который содержит состав изделия(золото, серебро,и т.п.), цену и кол-во (шт),которое есть в магазине.'
      '1. Просмотр описания: название – описание'
      '2. Просмотр цены: название – цена.'
      '3. Просмотр количества: название – количество.'
      '4. Всю информацию.'
      '5. Покупка В пункте «Покупка» необходимо совершить покупку, с клавиатуры вводите '
      'название изделия и его кол-во, n – выход из программы. Посчитать цену выбранных товаров'
      ' и сколько товаров осталось в изначальном списке.'
      '6. До свидания')

shop = {
   "Кольцо": ["золото", 5000, 10],
   "Цепочка": ["серебро", 2000, 5],
   "Браслет": ["сталь", 1000, 3],
   "Серьги": ["серебро", 1500, 8]
}

print("Добро пожаловать в ювелирный магазин 'Мечта любой девушки'!!!\n")
while True:
   print("Меню:")
   print("1. Просмотр описания")
   print("2. Просмотр цены")
   print("3. Просмотр количества")
   print("4. Вся информация")
   print("5. Покупка")
   print("6. До свидания")

   choice = input("\nВыберите пункт меню: ")

   if choice == "1":
       print('Все товары нашего магазина: ')
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

       name = input("\nВведите название изделия: ")
       if name in shop:
           description = shop[name][0]
           print(f"Описание: {description}")
       else:
           print("Такого изделия нет в магазине")

   elif choice == "2":
       print('Все товары нашего магазина: ')
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

       name = input("Введите название изделия: ")
       if name in shop:
           price = shop[name][1]
           print(f"Цена: {price} руб.")
       else:
           print("Такого изделия нет в магазине")

   elif choice == "3":
       print('Все товары нашего магазина: ')
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

       name = input("Введите название изделия: ")
       if name in shop:
           quantity = shop[name][2]
           print(f"Количество: {quantity} шт.")
       else:
           print("Такого изделия нет в магазине")

   elif choice == "4":
       for name, info in shop.items():
           description = info[0]
           price = info[1]
           quantity = info[2]
           print(f"{name}: {description}, Цена: {price} руб., Количество: {quantity} шт.")

   elif choice == "5":
       name = input("Введите название изделия (или 'n' для выхода): ")
       if name == "n":
           break
       if name not in shop:
           print("Такого изделия нет в магазине")
           continue
       quantity = int(input("Введите количество: "))
       if quantity > shop[name][2]:
           print("Недостаточно товара на складе")
           continue
       price = shop[name][1] * quantity
       shop[name][2] -= quantity
       print(f"\nВы купили {quantity} шт. {name}.\nСумма покупки: {price} руб.")

   elif choice == "6":
       break

   else:
       print("Неверный пункт меню")

print("Создайте кортеж из случайных 10 чисел. Найдите его максимальный минимальный элемент")
import random

numbers = tuple(random.randint(1, 100) for _ in range(10))
print(numbers)

max_number = max(numbers)
min_number = min(numbers)

print(f"Максимальный элемент: {max_number}")
print(f"Минимальный элемент: {min_number}")



