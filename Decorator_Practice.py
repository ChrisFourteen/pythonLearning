'''
Author:ChrisChan
Date:2020-4-28
用修饰器为函数添加判断功能
'''
user_list = [
    {'username':'cyx','pwd':'ai683683','shopping_car':['Tensorflow','Numpy','Deeplearning']},
    {'username':'tsts','pwd':'tsshigoushi','shopping_car':['tsts',1,'tsts']},
    {'username':'zj','pwd':'zj123123','shopping_car':['szjzj',1,'zjzj']},
    {'username':'jch','pwd':'root','shopping_car':['jjj',1,'sdfss']}
]
user = {'username':'','pwd':'','shopping_car':''}

def loginin(func):
    def warper(*args,**kwargs):
        if (user['username'] == '' and user['pwd'] == '' ) \
                or ((user['username'],user['pwd']) not in [(i['username'],i['pwd']) for i in user_list]):
            print('请输入用户名')
            user['username'] = input()
            print('请输入密码')
            user['pwd'] = input()
            if (user['username'],user['pwd']) in [(i['username'],i['pwd']) for i in user_list]:
                print('登录成功 %s')
                for i in user_list:
                    if i['username'] == user['username']:
                        user['shopping_car'] = i['shopping_car']
                func(*args,**kwargs)
            else:
                print('用户名或密码错误，登录失败')
        else:
            func(*args,**kwargs)
    return warper

def index():
    print('欢迎访问')

@loginin
def shopping_car():
    print('您的购物车里有 %s' %user['shopping_car'])

@loginin
def home():
    print('欢迎 %s 登录'%user['username'])


if __name__ == '__main__':
    index()
    while True:
        print('请输入要进行的操作\n 1 for home \n 2 for shoppingcar \n 3 for quie')
        a = input()
        if a == '1':
            home()
        if a == '2':
            shopping_car()
        if a == '3':
            break
