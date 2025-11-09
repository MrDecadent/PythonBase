# 纸的厚度
n = 0.1
w = n
for i in range(1, 50):
    w *= 2
    print(w)

# 国王麦粒
g = 1   # 当前格子应该放麦粒数
total = 0
a = 1 # 棋盘格子
while a <= 100:
    total += g
    print("在放满了%d个格子后，总麦粒数量为%d" % (a , total))
    g *= 2
    a += 1