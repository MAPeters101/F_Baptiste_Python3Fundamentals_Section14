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
print()



