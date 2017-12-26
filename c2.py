from collections import namedtuple, Counter
from random import randint

'''
如何为元祖中的每个元素命名，提高程序的可读性
'''

# 1. 通过常量
NAME, AGE, GENDER = range(3)
student = ('Bob', '18', '男')
print(student[NAME])

# 2. 通过collections.namedtuple
Student = namedtuple('Student', ['name', 'age', 'gender'])
res = Student('Bob', '18', '男')
print(res.name)

'''
统计序列中元素的出现次数
'''

data = [randint(15, 20) for _ in range(12)]
print(data)
# 1.通过字典
c = dict.fromkeys(data, 0)
for x in data:
    c[x] += 1
print(c)

# 2.通过collections.Counter.most_common
print(Counter(data).most_common(2))

'''
如何根据字典中值的大小，对字典中的项排序

某班英语成绩以字典形式存储为{'Bob':66,'Alan':78,'Jim':33...}，根据成绩高低，计算学生排名
使用内置函数sorted
'''
data = {x: randint(20, 100) for x in 'ABCDEFG'}
print(data)
# 1.使用zip将字典转元组再排序
new_data = zip(data.values(), data.keys())
res = sorted(new_data)
print(res)

# 2.利用sorted函数的key参数
res = sorted(data.items(), key=lambda i: i[1])
print(res)
