# for i in range(10):
#     print("hello")
#     print(i)
#
# print(list(range(10)))

# sum_num = 0
# for i in range(101):
#     sum_num += i
# print(sum_num)

# 1!+2!+3!+..+n!

# n = 20
# result = 0
# for n in range(1, n + 1):
#     sum_num = 1
#     for i in range(1,n+1):
#         sum_num *= i
#     print(sum_num)
#     result += sum_num
# print(result)

n = 4
result = 0
while n > 0:
    i = n
    sum_num = 1
    while i > 0:
        sum_num *= i
        i -= 1
    print(sum_num)
    result += sum_num
    n -= 1
print(result)