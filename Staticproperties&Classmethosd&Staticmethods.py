'''
静态属性，类方法，静态方法
'''

# 定义一个类
class people:
    name = 'test'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property                   # 通过装饰器的方式将 类 的函数属性变为 数据属性
    def eat(self):
        return 'I am eatting'

    @classmethod              # 类方法
    def shower(cls):
        print(cls.name)

    @ staticmethod            # 静态方法相当于类的一个工具包，没有实质性作用，可以不传入self或cls参数
    def drink(a,b):
        print('I am drinking %s %s' %(a,b))



# 实例化 people

cyx = people('cyx', 18)
result = cyx.eat               # 更改了类的调用方法，不需要再用()去执行该函数属性，直接用"."运算符     起到了封装的作用，
print(result)

people.shower()                # 在没有设置类方法的时候，只有在 对象（实例） 调用函数 或者  类实例化的时候 才会将self自动传入
cyx.shower()                   # 类方法可以自动将 cls 作为参数传入函数，以调用类的原有属性，对象不可以调用 类方法
# 对象调用类函数 之所以可以运行，是因为当对象找不到shower函数时，会自动去类里寻找

people.drink('bear','cola')
cyx.drink('bear','cola')       # 类  和 对象都可以调用该函数



