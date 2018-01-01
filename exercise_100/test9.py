# 暂停一秒输出（会有暂停效果）
# 使用time模块的sleep()函数

import time
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)  # 暂停1秒
