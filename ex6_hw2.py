import scipy as sp
n_rolls = 1 << 22
fair_die = sp.random.randint(1, 7, [1, n_rolls])[0]
sol1 = [len(line) + 1 for line in "".join([str(x) for x in fair_die if x % 2 == 0]).split('6')]
print(sp.mean(sol1))

sol2 = [len(x) + 1 for x in "".join(map(str, fair_die)).split('6') if set.issubset(set(x), set('24'))]
print(sp.mean(sol2))

a=5