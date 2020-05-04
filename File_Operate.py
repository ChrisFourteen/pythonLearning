'''
文件操作
文件操作分三步:1、打开文件 2、执行操作 3、关闭文件
文件的基本操作有 可读(r),可写(w),追加(a),读写(r+),追加可读(a+)
默认为可读模式，
可写模式会将该文件清空
追加模式不会将该文件清空
'''
f = open('file/test','r',encoding='utf-8')                   # 一定要指定编码模式
# 文件是保存在硬盘中的，保存形式为二进制，编码方式为Unicode
print(f.readable())   # 判断文件是否可读
print(f.readline())   # 读取一行并将光标移动到下一行开始
print(f.readline())
print(f.readline())
# f.read()会将光标移动到文档最后，再使用readlines是不起作用的
print(f.readlines())
f.close()

# f = open('file/test','w',encoding='utf-8')
# print(f.writable())
# f.write('你好你好，我是新来的\n')
# f.writelines(['你好我是第二行\n','你好我是第三行\n','你好我是第四行\n'])
# f.close()

# f = open('file/test','a',encoding='utf-8')          # 追加模式的光标默认在文档最后
# print(f.writable())
# print(f.readable())                     # 追加模式不能读，只能写
# f.write('我是追加的第一行\n')
# f.writelines(['我是追加的第二行\n','我是追加的第三行\n'])
# f.close()

# 上下文管理系统
with open('file/test','r+',encoding='utf8') as f:    # r+ 模式可读可写
    print('读写模式')
    print(f.readline())
    print(f.readline())
    # f.read()
    f.write('我是r+的第四行\n')
    f.write('我是r+的第五行\n')
print('*'*80)
'''
以二进制的方式打开文件
对于图像，视频等文件，我们需要用二进制的形式打开文件
'''
# f = open('file/test','rb')    # 二进制形式打开文件，不需要进行编解码！！！
# data = f.read()
# print(data)
# # 二进制解码  decode()函数
# print(data.decode('utf8'))
# f.close()

f = open('file/test','wb')
# 字符串编码为二进制的方法
# 1、encode()函数       2、bytes()函数
data = '我是二进制增加的一行，我编码的方法是encode函数\n'.encode('utf8')
f.write(data)
data = '我是二进制增加的第二行，我编码的方式是bytes函数\n'
data = bytes(data,encoding='utf8')
f.write(data)
f.close()


# 文件处理的其他方法
'''
在文件处理句柄中，只有read函数是以字符为单位额，其他都是以字节为单位的！！
'''
f = open('file/test','rb')
print('当前光标的位置:',f.tell())    # tell()函数的作用是输出当前光标所在的字节处
print(f.seek(10,0),f.tell())       # seek()函数用于移动光标
print(f.seek(10,1),f.tell())
print(f.seek(-10,2),f.tell())
'''
seek第一种方式（第二个参数为0）,从头开始移动光标
seek的第二种方式（第二个参数为1）,从当前位置开始移动光标
seek的第三种方式（第三个参数为2）,从文档末尾开始移动光标，移动值为负
seek只能在二进制模式下使用！！
'''



