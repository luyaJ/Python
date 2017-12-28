# 随机生成一个数字，猜测数字的大小

import random
num = random.randint(0, 100)
# print(num)

while True:
    guess = int(input("please input a number(1~100): "))
    if guess > num:
        print("你的数字猜大了", guess)
        tmp = guess
    elif guess < num:
        print("你的数字猜小了", guess)
        tmp = guess
    else:
        print("恭喜你，终于猜对了!")
        break
