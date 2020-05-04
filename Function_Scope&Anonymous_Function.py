'''***********函数作用域*************'''
name = 'alex'

def foo():
    name = 'cyx'

    def test():
        name = 'tsts'
        print(name)

        def bar():
            name = 'zj'
            print(name)

        return bar  # 这里拿到的是bar 函数的内存地址

    return test  # 返回test的内存地址


# foo()()
# foo()运行返回的是test函数的内存地址  foo()()是运行test函数，
foo()()()  # 拿到了bar的内存地址  foo()()()  运行bar函数，输出bar函数声明时作用域中的name
# 函数的作用域 只和它声明的地方有关，和被调用的地方无关

'''！！！匿名函数！！！'''
func = lambda name: name + '_sb'  # 匿名函数可以这么用，但是一般不这么用
print(func('alex'))
# 匿名函数一般是和其他函数联合使用，一般不独立存在，因为独立存在时会被立即释放



def fun(x,y):
    return x+1,y+1,6
a=fun(1,2)
print(a)