'''
迭代协议：内置一个next函数，执行next方法，要么返回下一个元素，要么抛出Stopiteration错误
之前接触的 列表、字典、字符串、集合等其实都不是可迭代对象
for循环的强大之处：for循环会调用循环体的__iter__()方法，__iter__ ()方法就是将该数据类型转换为迭代器，然后调用内置的__next__()方法
，另外for循环还会自动捕捉StopInteration错误，防止程序报错
'''

# list = ['1','2','3','4',5]
# list_inter = list.__iter__()
# print(list_inter.__next__())

# 用while模拟for循环做的事情
test = [6,7,3,2,4,5,1,8]
test = test.__iter__()
def like_for(list):
    while 1:
        try:
            print(test.__next__())
        except:
            break
like_for(test)

# 生成器：生成器是一种数据类型，它会自动遵循迭代协议
'''
生成器的定义方式有两种：
    1、通过生成器函数，类似于函数的定义方式，用 yeild 语句 代替 return 语句，并通过next函数调用该生成器
    2、通过生成器表达式的方式，即 (三元表达式) 的形式   ————>  这种方式类似于列表推导，只是将列表的中括号换成了小括号
'''

def epoch():
    for i in range(10):
        yield i

list_1 = [i for i in range(10) if i < 4]

list = (i for i in range(10) if i > 5)
# 迭代器方法的好处在于，在数据很多时，它不会把数据一下子都放到内存中，而是在需要时再将他调出来
