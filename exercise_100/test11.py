# 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 兔子规律为数列：1,1,2,3,5,8,13,21....

def rabbit(month):
    f1 = 1
    f2 = 1
    if month == 1 or month == 2:
        return 1
    else:
        for i in range(month-1):
            f1, f2 = f2, f1+f2
        return f1
print(rabbit(8))