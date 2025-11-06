# 转化为整数int
# 纯数字字符串
str1 = '2024'
print(str1, type(str1))
int1 = int(str1)
print(int1, type(int1))
# 浮点数转整数
str1 = 1.114
print(int(str1))
# 布尔值转整数
bool1, bool2 = True, False
print(int(bool1), int(bool2))

# 转化为浮点数float
str1 = '2024'
print(float(str1))
# 布尔值转float
print(float(bool1), float(bool2))

# 转化为布尔值boolean
str2 = 'abc123'
print(bool(str2)) # 只要有内容就是为真
str3 = ''
print(bool(str3)) # 空串为假
# 数字转布尔值
int1 = 1
print(bool(int1))
int2 = 0
print(bool(int2))
# 浮点数转布尔值
f1 = 1.0
print(bool(f1))

# 转化为字符串string
# 整数转字符串
int3 = 5
print(str(int3))
print(type(str(int3)))
# 浮点数转字符串
f2 = 5.14
print(str(f2))
print(type(str(f2)))
# 布尔值转字符串
bool1 = True
print(str(bool1))
print(type(str(bool1)))

# 进制的转换
str3 = '10'
print(int(str3,2)) # 二进制