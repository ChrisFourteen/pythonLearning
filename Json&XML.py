'''
xml和Json是比较常用的字符串序列化方式
主要用于数据的转换传输
支持各种语言之间的转换
功能类似于eval()
'''

import json
import xml.etree.ElementTree as EF

# json中最重要的方法有两个，一个是 dumps，一个是 loads

test = 'hello'
b = json.dumps(test)
print(json.dumps(test))         # json中 只有双引号！！！
test = {'name':'cyx','age':18,'gender':'male'}
a = json.dumps(test)
print(json.dumps(test))

# json完成的工作 ： 1、将拿到的所有类型中的单引号改为双引号   2、在外层加上引号变为字符串格式

print(json.loads(a))
print(json.loads(b))

f = open('os_test/test1/a.txt','r+')
f.write(a)
f.write('\n' + b)
f.close()

print('*'*80)

# root = EF.parse('test.xml')
root = EF.parse('test.xml')
# print(EF.iselement('name'))
print(root)
