# 10个苹果 小A拿走2个，小B拿走4个，小C拿走剩下所有
# 求：小A和小B两人一共拿走几个；小C能拿走多少个
apple = 10
a = 2
b = 4
c = apple - (a + b)

print("小A和小B两人一共拿走%d个苹果" %(a+b))
print("小C能拿走%d个苹果" %c)

# mia支付宝账户有100元。经过了以下操作
# 往里存了10元；购物花了20元；把里面的钱全取出来
# 请在每次操作后输出账户余额
miaBalance = 100
print("mia支付宝账户余额:%d" %miaBalance)
miaBalance = miaBalance + 10
print("mia支付宝账户余额:%d" %miaBalance)
miaBalance = miaBalance - 20
print("mia支付宝账户余额:%d" %miaBalance)
miaBalance = miaBalance - miaBalance
print("mia支付宝账户余额:%d" %miaBalance)