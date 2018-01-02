# assert断言：是声明其布尔值必须为真的判定，
# 如果发生异常就说明表达式为假。
s = 'Hello World!'
def comp(s):
    res = 0
    for c1 in s:
        res += 2
        for c2 in s:
            res -= 1

    return res

assert type(s) == str
assert comp(s) == 2*len(s) - len(s)**2
