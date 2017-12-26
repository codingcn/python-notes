from random import randint

'''
如何在列表，字典，集合中根据条件筛选数据
'''

'''
过滤列表[-52, -105, 99, 63, ...]中的负数
'''
# 创建一个随机列表
data = [randint(-110, 100) for _ in range(10)]
print(data)
# 1.通过for循环迭代的方式，略过（效率低）
# 2.通过filter函数
res = filter(lambda x: x >= 0, data)
print(list(res))
# 3.通过列表解析（相对于filter函数，效率较高）
res = [x for x in data if x >= 0]
print(list(res))

'''
筛选出字典{'Bob':79,'Jim':80,'Tim':92...}中值高于90的项
'''
data = {x: randint(60, 100) for x in range(1, 10)}
print(data)
# 字典解析
res = {k: v for k, v in data.items() if v > 90}
print(res)

'''
筛选出集合{55,85,63,66,33,...}中能被3整除的元素
'''
data = {randint(0, 100) for x in range(10)}
print(data)
# 集合解析
res = {x for x in data if x % 3 == 0}
print(res)
