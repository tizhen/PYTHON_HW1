# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# n = int(input())
 
# suma = 0
 
# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     n = n // 10
 
# print("Сумма:", suma)


n = input("Введите трехзначное число: ")
n = int(n)
 
d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
 
print("Сумма цифр числа:", n + d1 + d2)