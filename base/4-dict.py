
# key 可以是 string, int, float
dic = {'name': 'dog', 'age': 100, 4000: 'the 4000'}

# 遍历字典
for k in dic:
    print(k)

# 变成key,value的迭代
for k, v in enumerate(dic):
    print(k, v)

print(dic)
print(dic['age'])

# 防止取没有的key
# print(dic['age2']) # 报错
print(dic.get('age2'))  # None
print(dic.get('age2', 100))  # 100
# 如果age2在dic中
if 'age2' in dic:
    print(dic['age2'])

# create delete update find
b = dic.get(4000)
print(b)
dic.pop('age')
dic['bbbb'] = 'creaet'
dic['name'] = 'update'
print(dic)
