'''
os模块和  sys模块
os 模块主要用于和系统交互
sys 模块主要用于和解释器交互
'''
import os
import sys

# os.makedirs('os_test/test1')          # 用于创建目录   当路径已经存在时候会报错，可以创建多层的目录
# os.mkdir('os_test_1/test1/test1_1')   # 只能创建单层的目录，如果父目录不存在 则会报错
# os.chdir('os_test_1/test1/test1_1')     # 更改当前的工作目录
print(os.getcwd())  # 返回当前工作路径
print(os.path.isdir('os_test/test1')) # 返回路径是否存在
print(os.path.isfile('os_test/test1/a.txt')) # 判断文件是否存在
print(os.path.split('os_test/test1/a.txt')) # 将路径和文件名分开放到一个元组中

# os.remove('os_test/test1')                  # 当文件非空时，不能删除！
# # os.removedirs('os_test/test1')              # 删除到 非空的 一级 即停止删除

print(sys.argv)                             # 返回当前执行的文件路径
print(sys.path)                             # 获取环境变量！！




