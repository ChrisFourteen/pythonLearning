# 字典
# 字典里的元素是K，V键值对，V 可以是所有类型的值，K只能只不可改变的类型

info = {
    'k1':'v1',             # value 为字符串   key 为字符串 （不可改变）
    'k2': 2,               # value 为数字类型
    'k3': ['a','b','c'],   # value 为列表
    'k4': ('a','b',),      # value 为元组
    'k5': {'kk1':'vv1',
           'kk2':'vv2',
           'kk3':'vv3'},    # value 为字典
    'k6': True,             # value 为布尔值
    ('k7'): 'v7',           # key 为元组（不可改变）
    8 : 'v8',               # key 为数字 (不可改变)
    True: 'v9'              # key 为布尔值 （不可改变）
    # key 不可以是列表，字典等可以修改的对象
    # key 在内存中是以哈希表的形式存储的，可修改的对象不可哈希
}

print('字典是无序的',info)
print('*'*40+'\n')

for item in info:
    print(item)
print('字典可以用for循环进行遍历，但不可以用while循环进行遍历,for循环默认遍历的是所有的key值')

for item in info.keys():
    print(item)
print('也可以用keys()方法取出字典中所有key值进行遍历')

for item in info.values():
    print(item)
print('通过values()方法取出字典中所有的value值进行遍历')

for k,v in info.items():
    print(str(k) + ':' + str(v))
print('通过items()方法可以同时遍历字典中的key值和value值')
print('*'*40 + '\n')

print('字典中常用的方法')

# info.clear()             清空字典
# print(info)

# a = info.pop('k1','None')        根据第一个参数指定的key删除指定的K，V键值对，并返回被删除的value值，如果指定的key在第一个参数中不存在，则返回第二个参数
# print(info)

# a = info.popitem()                随机删除一个键值对，并以元组的形式返回该键值对
# print(a,b,c)
# print(info)

# info = dict.fromkeys(['k1','k2','k3'],'values')      遍历第一个参数生成多个key，将value值作为它们公共的值
# print(info)

# a = info.get('k1')                           # 使用索引的方式取值，若索引不存在则程序报错
# b = info.get('adsf')                          # 使用get方法取值，若不存在 则不会报错,并返回第二个参数的值，若第二个参数没有设置，返回None
# print(a,b)

# info.update({'k1':'v1_updated','k2':'v2_updated','k100':'v100_new'})
# info.update(k1='v1',k2='v2',k100='')
# print(info)                                   # 更新字典，其中如果key已经存在，则更新value，如果key不存在则创建

# info.setdefault('k_set','v_set')              添加键值对，如果key已经存在，则更新并返回原来的value值，如果不存在则添加该键值对并返回第二个参数
# print(info)

print('集合：用大括号包括的 数据类型必须是不可改变的的 元素不可重复的 可迭代的 无序的 数据集合')
s = set('hello')
print('创建集合的方法一：通过set函数',s)
s = {'alex',1,(1,'2',)}
print('创建集合的方法二：直接通过大括号创建',s)
for item in s:
    print(item)
print('集合可以使用for循环来遍历')

print('集合常用的方法')
# s.clear()                     清空集合
# print(s)

# s.pop()                       随机删除集合中某个元素
# print(s)

# s.remove('alex')              删除集合中指定的元素，如果指定元素不存在，则会报错
# print(s)
# s.remove('asr')

# s.discard('alex')               删除集合中指定的元素，如果指定元素不存在，则什么都不做

# s.add('cyx')                    将指定元素添加到集合中去
# print(s)

print('集合的运算关系')
python = {'cyx','ts','zj','jch','wzy','oyll'}
linux = {'cyx','ts','zj'}

result = python.intersection(linux)
# 相当于python & linux
print('求交集',result)

result = python.union(linux)
# 相当于 python | linux
print('求并集',result)

result = python.difference(linux)
# 相当于python - linux
print('求差集',result)

result = python.symmetric_difference(linux)
# 相当于 python^linux
print('求差补集',result)

result = linux.isdisjoint(python)
print('判断是否没有交集',result)

result = linux.issubset(python)
print('判断是否为参数的子集',result)

result = linux.issuperset(python)
print('判断是否为参数的父集',result)

# python.intersection_update(linux)             找到python和linux的交集，并将集合python更新为 该集合
# print(python)

# python.difference_update(linux)               找到python和linux的差集，并将集合python更新为 该集合
# print(python)
#
# python.symmetric_difference_update(linux)      找到python和linux的差补集，并将python 更新为该集合
# print(python)


print('Python中布尔类型为False的几种情况',bool(0),bool(''),bool({}),bool([]),bool(()),bool(None))

