# 编写python程序，统计在2000和3200之间(包括2000和3200)
# 可以被7整除但不是5的倍数的整数的个数。
count = 0
for i in range(2000, 3201):
    if (i % 7 == 0) & (i % 5 != 0):
        print(i)
        count += 1
print(count)