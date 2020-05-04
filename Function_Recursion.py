import time
people_list = ['陈云翔','唐帅','张竣','蒋诚横','彭祖郎','黄智昌','曾靓']
def ask_way(list):
    if(len(list) == 0):
        return '没有人知道怎么走'      # 设置递归的第一个约束条件
    people = list.pop(0)             # 每次从list中删除第一个元素并赋值给people
    print('请问 %s 知道荔枝住在哪里吗？' % people)    # 字符串拼接
    if people == '彭祖郎':
        return '我知道，荔枝住在黎郡新宇熙春园10栋1103'
    print('%s说：我也不知道，但我可以帮你问问 %s' % (people,people_list))        # 字符串拼接——元组
    time.sleep(1)
    next = ask_way(list)                      # 在没有得到return前，next都在等待，一层一层等待，直到某一层拿到了return，再一层一层返回
    return next


res = ask_way(people_list)
print(res)

