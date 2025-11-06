# 浮点数的计算
f1 = 2.1
f2 = 16.256
print(f1 + f2)


# 四舍五入
f3 = round(f1 + f2, 2)
print("四舍五入:",f3)


import math
# 向上取整 ceil
f4 = math.ceil(f1 + f2)
print("向上取整:",f4)
# 向下取整 float
f5 = math.floor(f1 + f2)
print("向下取整:",f5)