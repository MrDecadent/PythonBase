# while True:
#     print("1111")
#     break


# for i in range(1, 11):
#     if i > 0 and i % 3 == 0:
#         print(i)
#         break

# 判断一个数字n是否是质数
n = 9
for i in range(1, n):
    if i > 1 and n % i == 0:
        print("%s不是质数" % n)
        break
else :
    print("%s是质数" % n)
