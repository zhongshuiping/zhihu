class A(object):
    def __init__(self):
        self.content = ['A: B 你在？','A: 你在干嘛啊','A: 今天天气很好，我们去玩把','A: 不知道你在说什么'
            ,'A: 你的觉我写的程序咋样啊','A: 给一点点小小的评价咋样啊','A: 有没有觉得我特别棒啊','A: 你知道什么是python？','A: 我有电话，下了'
            ,'A: 有空聊','A: bye 有空聊']

while True:

    i = 0
    a = A()
    for i in range(10):
        print(a.content[i])

        b_content = input('')
        print('B :' + b_content)
        if'bye' in a.content[i]:
            break
    break
