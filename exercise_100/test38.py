# 计算矩阵值

if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input number:")))
    for i in range(3):
        sum += a[i][i]
    print(sum)