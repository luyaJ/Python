import random
num = random.randint(0, 100)
# print(num)

while True:
    try:
        guess = int(input("Please input a number(1~100): "))
    except ValueError as e:
        print("输入格式不正确，请重新输入数字Input 1~100")
        continue
    if guess > num:
        print("你的数字猜大了", guess)
        tmp = guess
    elif guess < num:
        print("你的数字猜小了", guess)
        tmp = guess
    else:
        print("恭喜你，终于猜对了!")
        break