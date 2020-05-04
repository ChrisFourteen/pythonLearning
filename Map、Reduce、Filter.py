# 假设现有需求，将一个只包含数字的列表中的所有元素都自加1
# 函数式编程的思想实现如下
test = [3,6,4,5,7,8,9,12,3]

def add_one(x):
    return x+1

def squ(x):
    return x**2

def map_list(func,list):
    res = []
    for i in list:
        a = func(i)
        res.append(a)
    return res

result = map_list(add_one,test)
result_2 = map_list(squ,test)
print('原列表元素都自加1：',result,'\n原列表元素都平方：',result_2)

print('&&&&&其实python中自带了Map()函数可以实现此功能&&&&')

a = map(lambda x:x+1,test)
print('map函数默认返回的是一个迭代器',a,'\n用list函数将其转换为列表:',list(a))

# ****************************************************************************
print('-'*80)
# 假设现在有需求，将列表中后缀为del的字符串删除
test = ['cyx','tsts','zj_del','jch_del','pzl','hzc_del','zxf']

# def del_del(list):
#     res = []
#     for i in list:
#         if not str(i).endswith('del'):
#             res.append(i)
#     return res
#
# a = del_del(test)
def del_ends(x):
    if not str(x).endswith('del'):
        return x

def s_sta(x):
    if not str(x).startswith('z'):
        return x

def filter_list(func,list):
    res = []
    for i in list:
        a = func(i)
        if a is not None:
            res.append(a)
    return res

result = filter_list(del_ends,test)
result_2 = filter_list(s_sta,test)
print('原列表中删除del结尾的字符串:',result,'\n原列表中删除开头的字符串：',result_2)

print('&&&&&&&其实python中自带了filter函数&&&&&&&&')

result_3 = filter(del_ends,test)
result_4 = filter(lambda x:not str(x).startswith('z'),test)    # filter默认是将返回为true的结果输出，因此要删除时，在前面加not取反
print('用python自带的filter函数运行的结果也是一个迭代器：',result_3,'用list将其转换为列表：',list(result_3))
print('另一个用匿名函数的执行结果：',list(result_4))

from functools import reduce
print('-'*80)
# 假设有一个需求，将一个列表中所有的元素相加
test = [1,2,3,4,5]

def add_all(list):
    res = 0
    for i in list:
        res += i
    return res

result = add_all(test)
print('使用reduce函数，要调用functools模块')
print(result)

result = reduce(lambda x,y:x*y,test)
print(result)


