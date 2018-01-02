# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

n = int(input("输入几个数字相加："))
a = int(input("输入数字："))
sum = 0
total = 0

for i in range(n):
    # n = 2, a = 2 ;
    # sum = 0 + 10 ** 0 + 10 ** 1
    sum += 10 ** i
    print(sum*a)
    # total = 0 + sum * 2
    total += sum * a
print(total)

