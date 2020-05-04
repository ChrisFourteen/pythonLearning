'''
装饰器：高阶函数 + 函数嵌套 + 闭包
高阶函数： 函数的参数是一个函数，函数的返回值是一个函数，满足这两个中的任意一个即可称为高阶函数
函数嵌套: 在函数内部 定义 另一个函数
闭包 ： 将变量包裹在一个作用域中

装饰器的两个基本原则：1、不能改变原函数的代码  2、不能改变原函数的调用方式
装饰器的应用场景  ————> 开放封闭原则：即软件代码可以扩展，但是不可以修改，也就是说对扩展是开放的，对修改是封闭的
                    例如在一个已经上线的项目，要加入功能，不可能对已经完成的函数进行修改，而是通过修饰器的方式对原有函数功能进行扩展
'''
# 场景： 记录一个函数的运行时间
import time
# 原函数


# 方案1
def project_1():
    '''
    方案1：    可以实现效果，但是改变了原函数的代码，不符合装饰器的原则     不合格 ！！
    def test():
        start_time = time.time()
        for i in range(10):
            time.sleep(0.1)
        print('test函数执行完毕')
        end_time = time.time()
        print('函数执行时间为: %s' %(end_time-start_time))
    test()'''
    pass
# 方案2
def project_2():
    '''方案二:通过高阶函数来实现效果，但是改变了原函数的调用方式,不符合装饰器的原则    不合格 ！！
    def timer(func):
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数的运行时间为: %s'%(end_time - start_time))

    timer(test)'''
    pass
# 方案3
def project_3():
    '''  方案三：高阶函数返回原函数的地址，再将该地址赋值给原函数的变量名
    虽然没有改变原代码，且没有改变原函数调用方式，但是原函数会被调用两次，不合格！！！
    def timer(func):
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数运行时间为: %s' %(end_time-start_time))
        return func

    test = timer(test)                     # 这里调用timer()  teimr()里面调用了一次
    test()                                 # 这里又调用了一次test'''
    pass
# 方案4
def project_4():
    '''
    通过闭包的形式先再timer内部保存下来，同时在timer内部闭包另一个函数，timer函数运行时返回warper函数的地址，这样 test = time(test)
    其实就是获取了warper的内存地址，test()就是运行warper函数，需要加入返回值时只需要让warper函数返回相应的值即可
    但是当原函数中有参数时，这种方法就会失效！！
    def timer(func):
        def warper():
            start_time = time.time()
            func()
            end_time = time.time()
            print('函数所用的时间为 %s' %(end_time-start_time))
        return warper

    test = timer(test)                      # 这里得到的返回值是 warper函数的返回值，而warper是通过闭包的形式保存再timer函数中
    test()                                  # 这里相当于运行了warper函数，warper函数中保存了test函数的内存地址'''
    pass
# 方案5     终极方案！！！！！
'''
*args  会把接收到的位置参数转化为元组
**kwargs  会把接收到的关键字参数转化为字典
'''
def timer(func):
    def warper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('函数所用的时间为：%s'%(end_time-start_time))
        return res
    return warper


@timer          # 相当于 test = timer(test) 在函数定义前使用
def test(name,age,gender):
    for i in range(20):
        time.sleep(0.1)
    print('test函数执行完毕,name = %s,age = %s,gender = %s' %(name,age,gender))
    return '这里是原函数的返回值'

@timer
def test_1(name,age):
    for i in range(20):
        time.sleep(0.1)
    print('test函数执行完毕,name = %s,age = %s' %(name,age))
    return '这里是原函数的返回值'

test('cyx',18,'man')
test_1('zj',20)




