

a = dict()
a['1'] = 12
a['2'] = 23

b = dict()
b['a'] = 'asd'
b['as'] = 'fds'

c = {**a, **b}
print(c)