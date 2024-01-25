
#Factorial
# def factorial(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact *= i
#     return fact
# res = factorial(5)
# print(res)


#multiplication table
# def calculator(num):
#     if num <= 0:
#         print("invalid number")
#         return
#     for i in range(1, 11):
#         print(f" {num} x {i} = {num * i}")
#
# res = calculator(5)
# print(res)

#multiplication table-2
# def calculator(num):
#     if num <= 0:
#         print("Invalid number")
#     for i in range(1,num+1):
#         for j in range(1, 11):
#             print(f"{i} x {j} = {i *j} ")
# res = calculator(10)
# print(res)

# def sum_of_number(num):
#     suma = 0
#     while num != 0:
#         remainder = num % 10
#         suma = suma + remainder
#         num = num // 10
#     return suma
# res = sum_of_number(67)
# print(res)

#Fibonacci

# def fibonacci(num):
#     num1 = 0
#     num2 = 1
#     next = 0
#     if num in(1,2):
#         return num-1
#
#     for _ in range(2, num):
#         next = num1 + num2
#         num1, num2 = num2, next
#     return next
#
# res = fibonacci(8)
# print(res)







