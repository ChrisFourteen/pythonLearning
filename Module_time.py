'''
关于时间的模块
python中常用的包就是time和datetime
时间的形式包括 1、时间戳  2、结构化时间  3、字符串时间
'''
import time
import datetime

print('当前时间戳：',time.time())    # 获取当前的时间戳    这个时间戳是1970年1月1日linux诞生时开始计算的秒数
print(time.gmtime())                # 将当前时间戳转换为 结构化时间  (国际标准时间)
print(time.localtime())             # 将当前时间转换为 当地时间的 结构化时间
print(time.mktime(time.gmtime()))   # 将结构化时间转化为时间戳
a = time.strftime('%Y-%m-%d,%X')
print(a) # 将当前时间转换为字符串时间
print(time.strptime("30 Nov 00", "%d %b %y"))

print(time.ctime())   # 内置的 已经写好的字符串格式的时间


print(datetime.datetime.now())                     # 更符合规范的时间格式

