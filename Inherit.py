'''
面向对象的三大特征：继承，多态，封装
普通的继承会导致程序耦合严重
推荐的做法是使用  归一化继承
定义一个模板，使用abc模块,
当字类的格式与父类不同时，不允许实例化
'''
import abc

class father:                                   # python中的类都是新式类，都会继承object对象  class father(object):  只是省略了而已
    dolor = 100

    def __init__(self,addr):
        self.addr = addr

    def learning(self):
        print('I am learning')

class son(father):

    def __init__(self,name,addr):
        super().__init__(addr)                        # 这段代码在父类中已经有了,我们想调用父类的方法，应该用super
        self.name = name
# python可以多继承，而java和c#中只可以单继承
# son 会继承 father的所有东西，子类中找不到的方法，会自动去父类中寻找
print(son.dolor)
s = son('cyx','changsha')
s.learning()
# 子类中的 方法 或者 属性和父类重名时，不会修改父类的方法或属性
son.dolor = 1000000
print(s.dolor)

# 继承顺序分为：深度优先和广度优先      python中都是广度优先
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
class E(C):
    pass
class F(B,C):
    pass

print(F.__mro__)             # 打印出类F 的 mro 链表，也就是它的继承顺序

# 子类中调用父类的方法：super()
# 相当于调用了父类，而且当父类名称更改时候不需要修改代码，同时也不需要调用self
print(s.addr)







