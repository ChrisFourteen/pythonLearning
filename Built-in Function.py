print(abs(-1))                            # 取绝对值
print(bin(10))                            # 10进制 ————> 二进制
print(oct(10))                            # 10进制 ————> 八进制
print(hex(10))                            # 10进制 ————> 十六进制
print(all(['ads',2,'asd']))               # 检测列表中是否都为真值
print(any([1,2,3,4,15,7]))                # 检测李彪中是否存在真值
print(eval('1+2*4'))                      # eval()函数的第一个作用，可以把计算字符串中的数学运算
print(eval('{"name":"cyx"}'))             # eval()函数的第二个作用，将字符串中的数据类型还原
print(bytes('你好',encoding='utf8'))       # 按照规定的编码方式将字符串转换为字节
# \x表示16进制  utf8中表示一个汉字要用3个字节 一个字节八位
print(divmod(10,3))                       # 返回一个元组，第一个元素为商，第二个元素为余数
print(dict([('name','age'),('cyx',18)]))  # dict函数传入列表（列表中为两个元组，一一对应）
print(dict(name='cyx',age=18))            # dict函数传入关键字，最后会生成字典的形式

# zip函数：像拉链一样，将传入的两个可迭代对象一一对应生成列表，列表中全部是元组
test = zip(['name','age','sex'],['cyx',18,'male'])
print(test,'zip函数返回的是一个迭代器',list(test))
test = {
    'name':'cyx',
    'age':18,
    'sex':'male'
}

res = zip(test.values(),test.keys())
print(list(res))

# Max() 和 Min() 函数的用法
# 最简单的max()和min()函数的用法
'''
max()函数将可迭代参数进行for循环，然后对每个元素进行比较
不同数据类型无法比较
比较字符串时会一位以为进行比较，当某一位比较大时会停止比较，并且判定该字符串大
字符串比较的规则参照ASCii码
'''
print(max([1,2,3,4,5,6,7]))
a = [('bname','cyx'),('age',18),('cname',20)]
# 当max比较的参数是元组或数组时，它会默认比较第一个元素
# 当max比较的参数是字典时，它会默认比较key值

# 场景：输出以下字典中age最大的人
people = [
    {'name':'cyx','age':25,'sex':'male'},
    {'name':'ts','age':18,'sex':'female'},
    {'name':'zj','age':24,'sex':'male'},
    {'name':'jch','age':26,'sex':'male'}
]

# max()内有key参数，可以先对for循环出的元素进行指定的函数处理，再进行比较，并返回该元素

def com_age(dict):
    return dict['age']

result = max(people,key=com_age)['name']
print(result)

# sorted()函数，可以将有序可迭代对象进行排序并返回一个迭代器
test = [1,2,3,4,5,6,7]
result = sorted(test,reverse=True)
print(result,'此时test为：',test,'并没有改变')

test.sort(reverse=True)
print('用列表自带的sort函数会导致列表改变',test)
print(list(reversed(test)))
print('内置函数reversed和sorted相似，也不会改变原有test的值，但是列表自带的reversed就会改变原有test的值')

'''
引入文件时，import的原理是，结合系统，找到__import__()函数，然后运行
__import__()函数可以接收字符串，并引入该字符串代表的文件

'''