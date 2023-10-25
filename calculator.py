# # Функция для сложения
# def add(x, y):
#     return x + y

# # Функция для вычитания
# def subtract(x, y):
#     return x - y

# # Функция для умножения
# def multiply(x, y):
#     return x * y

# # Функция для деления
# def divide(x, y):
#     if y == 0:
#         return "Ошибка! Деление на ноль невозможно."
#     else:
#         return x / y

# #Основная функция калькулятора
# def calculator():
#     print("Выберите операцию:")
#     print("1. Сложение")
#     print("2. Вычитание")
#     print("3. Умножение")
#     print("4. Деление")

#     choice = input("Введите номер операции (1/2/3/4): ")

#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))

#     if choice == '1':
#         print("Результат: ", add(num1, num2))
#     elif choice == '2':
#         print("Результат: ", subtract(num1, num2))
#     elif choice == '3':
#         print("Результат: ", multiply(num1, num2))
#     elif choice == '4':
#         print("Результат: ", divide(num1, num2))
#     else:
#         print("Неверный ввод")

# # Вызов функции калькулятора
# calculator()




                  # 2 Вариант


#  2  while True : print (eval (input("Число жаз :")))
 

def tree (x ,y) :
    return x + y

def con (x,y):
    return x - y

def semm (x,y):
    return x * y

def lino (x,y):
    if y == 0 :
        return "0 го бөлгөнгө болбойт"
    else:
        return x / y 
    

    # Основные  функции калькулятора 
def calculator() :
    return("Выберите операцию :")
print("1. Кошуу")
print("2. Алуу")
print("3. Көбөйтүү")
print("4. Бөлүү")

txt = input("Введите номер операции (1/2/3/4) :")

fool1  = float(input("Биринчи санды тандаңыз: "))
fool2 = float(input("Экинчи санды тандаңыз: "))

if txt == "1":
    print("Жообу: ", tree(fool1 ,fool2))
elif txt == "2 ":
   print("Жообу:", con(fool1 ,fool2))
elif txt =="3":
    print("Жообу:" , semm (fool1, fool2) )
elif txt =="4":
    print("Жообу :" , lino (fool1 ,fool2))
else :
    print("Неверный вод")

# # Вызов функции калькулятора
calculator()