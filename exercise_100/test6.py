# 斐波那契数列（Fibonacci sequence)
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、55
#                   (0、1、2、3、4、5、6、7、 8、 9、10)

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(7))