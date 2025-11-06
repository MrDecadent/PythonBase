# 创建字符串
str1 = "hello,MrDecadent"
print(str1[0])
print(str1[4])
print(str1[-1])
# 切片 变量名[起始索引:结束索引+1:步数]
# 步数默认为1 可不写
# 起始索引默认0 可不写
# 结束索引默认None 可不写
print(str1[0:5]) # 从0开始取到第5 不包括第5个
print(str1[6:16])

str2 = "123456789"
print(str2[0:9:2])
print(str2[1:None:])

# 字符串反转
print(str2[-1:None:-1])
print(str2[::-1])