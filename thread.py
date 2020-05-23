import threading                    # 线程引入的包
import time
# 创建一个新的线程
'''
Python中加入了GIL，也就是说一个进程中在同一时刻只能运行一个线程
在IO密集型任务中，CPU遇到IO任务时会存在空闲期，这时GIL的机制可以使多线程的效果更好
但是在计算密集型任务中，GIL的机制反而会使得多线程的耗时比单串行还要长
一般不推荐使用大量的进程，因为进程会消耗大量的资源
'''
def music():
    print('I am listening music')
    time.sleep(3)               # 模拟IO操作
    print('music finished')

def read():
    print('I am reading\n')
    time.sleep(5)
    print('read finished')

# t1 = threading.Thread(target=music)             # 创建线程
# t2 = threading.Thread(target=read)
# t1.start()                                      # 运行线程开始
# t1.join()               # join()线程t1结束后才可以运行其他线程
# t2.start()                                      # 线程开始运行
#
# print('I am a computer')

##  关于同步锁
# 思考场景： 100个线程，每个线程执行一次  -1 操作，将global变量100 变为0

num = 100
A = threading.Lock()
B = threading.Lock()
def reduce():
    A.acquire()
    global num
    temp = num
    time.sleep(0.001)
    '''
    加入i/o操作，CPU有了切换的动作，导致多个线程还没有完成计算就被剥夺CPU使用权，除非它计算够快，否则直到它再次拿到CPU使用权
    才可以继续进行计算，才能改变num的值给下一个线程，因此其实大多数线程拿到的num都是100，而不是上一个线程操作后了的值
    这种情况，我们定义同步锁，被同步锁锁定的程序在执行时不会进行CPU的切换
    '''
    temp-=1
    num = temp
    A.release()

l = []
for i in range(100):
    t = threading.Thread(target=reduce)
    t.start()
    l.append(t)

for i in l:
    i.join()                    # 保持了线程运行的顺序性，对于非守护线程是没有作用的

print(num)

C = threading.RLock()
# 死锁，当两个线程分别拿到两个锁并等待对方释放时候，双方都不会释放，会进入等待状态，这个时候用递归锁来解决这个问题
# 递归锁  rlock


class Thread(threading.Thread):

    def operate_1(self):
        C.acquire()
        print(self.name,'GotA')
        time.sleep(1)
        C.acquire()
        time.sleep(1)
        print(self.name,'GotB')
        C.release()
        C.release()



    def operate_2(self):
        C.acquire()
        time.sleep(1)
        print(self.name,'GotB')
        C.acquire()
        time.sleep(1)
        print(self.name,'GotA')

        C.release()
        C.release()

    def run(self):
        self.operate_1()
        self.operate_2()


l = []

for i in range(5):
    t = Thread()
    t.start()
    l.append(t)

for i in l:
    i.join()


