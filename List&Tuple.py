# ***********************列表的几大用法***************************
# 1、列表是可迭代的，可以用for和while循环进行遍历
test = ['111',45,'alex',555,66,[45,55],'aser',5463,'asder']
for item in test:
    print(item)
print('可以使用for循环来遍历列表中的所有元素')
print("*"*40)

# 2、列表也可以使用切片
result = test[2:6]
print('列表也可以使用切片的方式进行分割，分割的结果也是一个列表',result)
print('*'*40)

# 3、列表可以通过join方法连接
list_str = ['asd','asr','qwe','qwerd']
link = '_'
result = link.join(list_str)
print('可以通过join方法把列表中每个元素连接起来(当列表中只有字符串时)',result)
print('*'*40)

# 4、当列表中包含数字时，就需要自己写for循环来遍历
s = ''
for item in test:
    s += str(item)
print('当列表中包含数字，要想把列表中的元素连接起来，就需要自己写循环',s)
print('*'*40)


# 5、列表的存储方式和字符串不同，列表是可以修改的而字符串不可以修改
# 列表的存储方式是无序的链表式，而字符串的存储方式是连续的
# 列表可以通过索引的方式进行赋值  如： test = [1,2,3,4,5,6,7]   test[0] = 1
# 字符串不可以通过索引的方式进行赋值  如： test = 'asdfasgdasg'   test[0] = 'E'   结果会报错

# 6、列表中常用的内置方法
result = test.clear()
print('clear()方法可以清除列表中的内容',test,'clear不需要赋值给一个新的变量，会直接作用在list上')
test = ['111',45,'alex',555,66,[45,55],'aser',5463,'asder']
result = test.count('alex')
print('count()可以统计列表中某元素出现的次数',result)
result = test.append('aer')
print('test :',test)
print('append()方法可以将参数作为字符串追加到列表的最后',result)
result = test.extend('sadrqr')
print('test :',test)
print('extend()方法的参数必须是一个可迭代对象，该方法会把参数进行迭代然后依次添加到列表最后',result)
result = test.copy()
print('copy()可以复制列表，但是为浅复制',result)
result = test.pop()
print('test :',test)
result_2 = test.pop(5)
print('pop()方法默认在列表最后删除一个元素，但也可以为pop方法添加一个参数，来确定要删除元素的位置',result,result_2,'pop()方法的返回值是被删除的元素')
print('test :',test)
test.remove('s')
print('remove()用于删除列表中的某个元素，只删除一次且左侧优先',test)
test.reverse()
print('reverse()方法直接作用于list，不需要返回赋值，它将list反转',test)
test_s = [1,5,6,7,3,4,9,2]
test_s.sort()
print('sort()方法可以将由纯数字组成的列表进行从小到大排序，',test_s)
test_s.sort(reverse=True)
print('可以通过设置参数reverse=True，选择将list从大到小排序',test_s)
test.insert(5,'cyx')
print('insert()方法可以将某个元素插入特定的索引前',test)

# 元组——————>誓言，一旦创建，无法修改，删除，增加
# 元组是列表的二次加工品，元组中的元素可以是任何形式的
# 元组的一级元素无法修改，但是一级元素内部的元素还是可以修改，比如（1,2,'3',[4,5,6]）,该元素的第三个元素是个列表，列表可以修改
# 元组是有序的，列表也是有序的
# 元组是可遍历的，因此元组也可以用extend()   join()    for循环  等方法进行遍历





