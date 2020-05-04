# Python字符串方法
# Python字符串必须掌握的十种方法
# *********1、Join方法*********
print('在Python中字符串在内存中一但创建，则无法修改，所谓的修改都是重新开辟内存空间创建一个新的字符串\n\n')
print('************************python中重要的字符串方法和技巧***********************')
test = 'abcdefg'
separator = '_'
result = separator.join(test)
print('Join的作用是将字符串按照自定规则拼接,如：',result)
print("*"*40)

# *********2、find方法***********
test = 'alexalexalex'
result = test.find('exa')
print('find方法的作用是找到参数中的子序列并返回原字符串中第一个出现该子序列的位置,若返回值为-1则表示未找到',result)
result = test.find('ale',2,7)
print('find方法还可以增加两个参数，是匹配子序列的范围，左闭右开区间',result)
print("*"*40)

# *********3、upper方法**********
test = 'abcdefght'
result = test.upper()
print('upper的作用是将小写字母转换为大写',result)
print("*"*40)

# **********4、lower方法**********
test = 'ABcdEgHt'
result = test.lower()
print('lower的作用是将大写字母转换为小写',result)
print("*"*40)

# **********5、split**********
test = 'absgliosoijslsm'
result = test.split('s')
print('split可以将字符串按照参数指定的字符进行分割，但是使用的分割字符无法获取',result)
result = test.partition('s')
print('partition功能和split类似，但是只能匹配第一个分隔符且只完成一次分割，但其分隔符是可以获取的',result)
print("*"*40)

# **********6、strip**********
test = ' absftdrsdfsf '
result = test.strip()
print('strip的作用是去除原字符串左右两边的目标字符串，目标字符串就是strip方法的参数，默认为空格',result)
result = test.rstrip()
print('相应的也有rstrip，它只去除右边的目标字符串',result)
print("*"*40)

# **********7、切片**********
test = 'abseraldfakldf'
result = test[0:2]
print('字符串切片时中括号内的范围是左闭右开的',result)
result = test[2:-1]
print('-1表示字符串的最后一位',result)
print("*"*40)

# *********8、len()******
test = 'asdfaweradsr'
result = len(test)
print('len()方法可以返回字符串的长度，同样也可以返回列表的长度',result)
print("*"*40)

# *********9、for ... in ...*****
test = "dfsa"
for item in test:
    print(item)
print('字符串也支持for in 循环')
print("*"*40)

# ************10、range************
result = range(100)
print('range可以获取一串连续数字',result,'但再python中采用一种优化机制，不会立即创建range的内存，而是在使用for循环时逐渐创建内存')
result = range(0,100,6)
for item in result:
    print(item)
print('range也可以获取一串间隔相同的数字',result)


test = 'i am {},age {}'.format('alex',18)
print(test)






