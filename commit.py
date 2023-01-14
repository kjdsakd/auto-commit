import time
import random
from os import system as A
def c():
    A('git add .')
    A('git commit --allow-empty -m commit');
    A('git push origin master')
#打开temp.txt文件
f = open('temp.txt', 'w')
#清空文件并随机写入一个数字
f.write(str(random.randint(0, 100)))
f.close()
c()
while True:
    #等待随机事件
    time.sleep(random.randint(1000,9400))
    #打开temp.txt文件
    f = open('temp.txt', 'w')
    #清空文件并随机写入一个数字
    f.write(str(random.randint(0, 100)))
    f.close()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    c()
    print("\n")
