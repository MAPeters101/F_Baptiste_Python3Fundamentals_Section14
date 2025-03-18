l = [1,2,3,4,5]
t = (10, 20, 30)

result = zip(l, t)
print(result)
print(type(result))
print(next(result))
print(next(result))
print(next(result))
#print(next(result))
print('-'*80)

print(list(zip(l,t)))
combo = list(zip(l,t))
print(combo)
print(combo)
print('-'*80)

from time import perf_counter
start = perf_counter()
l1 = range(100_000_000_000)
l2 = range(100_000_000_000)
combo = zip(l1, l2)
end = perf_counter()
print(f'elapsed: {end - start}')
print()

start = perf_counter()
l1 = range(1_000_000)
l2 = range(1_000_000)
combo = list(zip(l1, l2))
end = perf_counter()
print(f'elapsed: {end - start}')
print('='*80)

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print()

data = [
    ('item1', 10, 100.0),
    ('item2', 5, 25.0),
    ('item3', 100, 0.25)
]
schema = ('widget', 'num_sold', 'unit_price')



schema = ('widget', 'manufacturer', 'num_sold', 'unit_price', 'discount')
d = {}
for item in data:
    d[item[0]] = {'num_sold': item[1], 'unit_price': item[2]}
print(d)
print('-'*80)


schema = ('widget', 'num_sold', 'unit_price')
for row in data:
    print(list(zip(schema, row)))
print()

for row in data:
    widget_name = row[0]
    remaining = zip(schema[1:], row[1:])
    print(widget_name, list(remaining))
print()

for row in data:
    widget_name = row[0]
    sub_dict = dict(zip(schema[1:], row[1:]))
    print(widget_name, sub_dict)
print('-'*80)

data_dict = {}
for row in data:
    widget_name = row[0]
    sub_dict = dict(zip(schema[1:], row[1:]))
    data_dict[widget_name] = sub_dict
print(data_dict)
print('-'*80)

data_dict = {}
for row in data:
    data_dict[row[0]] = dict(zip(schema[1:], row[1:]))
print(data_dict)
print('-'*80)


