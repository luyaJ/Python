# 假设一个机器人从原点(0,0)出发自由行走(只有 UP, DOWN, LEFT, RIGHT四种动作)。
# 文件 moves.txt 记录了机器人行走的轨迹，每行记录了机器人的一次行走动作.
# 例如 moves.txt 的记录为：
# UP 5
# DOWN 3
# UP 1
# LEFT 3
# 请编写一个函数 calcDist( moves.txt ),
# 输入值是 moves.txt， 输出值是机器人距离原点的距离。
# 例如 calcDist(moves.txt) 的返回值应该等于 4.242。

import re
import math
def calcDist(file_path):
    fp = open(file_path, 'r')  # 打开文件
    count_x = 0
    count_y = 0
    for line in fp:
        x = 0
        y = 0
        digit = re.findall(r'([0-9]+)', line)  # 读数字
        letter = re.findall(r'([a-zA-Z]+)', line)  # 读字母
        if 'UP' in letter:
            y1 = y + int(digit[0])
            print('向上移了 %d 个单位:' % y1)
            count_y += y1
            print('纵坐标方向位移为：', count_y)
        if 'DOWN' in letter:
            y1 = y - int(digit[0])
            print('向下移了 %d 个单位:' % y1)
            count_y += y1
            print('纵坐标方向位移为：', count_y)
        if 'LEFT' in letter:
            x1 = x - int(digit[0])
            print('向左移了 %d 个单位:' % x1)
            count_x += x1
            print('横坐标方向位移为：', count_x)
        if 'RIGHT' in letter:
            x1 = x + int(digit[0])
            print('向右移了 %d 个单位:' % x1)
            count_x += x1
            print('横坐标方向位移为：', count_x)
    fp.close()
    d = count_x ** 2 + count_y ** 2
    return '机器人距离原点的距离: %f' % math.sqrt(d)

if __name__ == '__main__':
    print(calcDist(r'moves.txt'))
