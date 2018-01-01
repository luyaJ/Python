# 将一个正整数分解质因数。
# 例如：输入90,打印出90=2*3*3*5

n = int(input("输入一个正整数："))
while n not in [1]:
    for k in range(2, n+1):
        if n % k == 0:
            n = int(n/k)
            if n == 1:
                print("%d " % k, end="")
            else:
                print("%d * " % k, end="")
            break
print()
