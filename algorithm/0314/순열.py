import itertools

hello = ['a', 'a', 'b', 'c', 'd', 'e']
print(list(map(''.join, itertools.permutations(hello))))
print(list(map(''.join, itertools.combinations(hello, 3))))

print(list(map(''.join, itertools.permutations(set(hello)))))

hi = 0
hi2 = 0
hi = hi2 = 1
print(hi, hi2)