data = []
lenth = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
	for wide in range(len(data)):
		lenth += len(data[wide])
#	for d in data:
#		lenth += len(d)
print(lenth)
print('每条留言平均为: ', lenth / len(data))
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '笔资料字小于100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
#good = [d for d in data if 'good in d']
#list comprehension清单快写法
print('一共有', len(good), '笔留言提到good')
print(good[0])