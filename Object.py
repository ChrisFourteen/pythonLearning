'''
三大编程派系各有千秋
1、面向过程编程   2、面向对象编程   3、函数式编程
编程语言是面向过程的还是面向对象的并会会影响 编程者采用哪种编程方式
'''

Mood = 'bad'
# python中的对象定义
class people:
    health = True
    Mood = 'Nice'
    def __init__(self, name, age, country, gender):
        '''
            __init__() 函数中，一定一定不能有返回值，不然会和实例化的返回值冲突！！
            定义私有的数据属性
            __init__()中的操作只有在实例化时才会运行
        '''
        self.name = name
        self.age = age
        self.country = country
        self.gender = gender
        print('这里的Mood不是使用"."调用的,因此遵循的是普通的作用域理论',Mood)

    # 函数属性
    def eat(self, food):
        print('I am eatting %s' % food)

    def shower(self):
        print('I am taking a shower')


p_1 = people('Chris', '24', 'China', 'male')  # 实例化 people 类

print(people.__dict__)  # __dict__()是内置方法，可以查看类，或实例的属性字典
print(p_1.__dict__)  # 注意：实例中没有函数属性，实例要用类中的函数时候会自己去类中找
print(p_1.health)  # 实例p_1的属性字典中并没有health属性，但是它会自己去类中寻找health属性

# 属性的增删改查  略

p_1.eat('包子') # 实例在调用类中的函数属性时，会传参给self
p_1.shower()

# p_1.__dict__['name'] = 'cyx'    # 不要这样修改实例底层的字典结构，会造成对象不稳定！！


