import pandas as pd
import numpy as np
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins, right = False)

print(cats)

print(cats.codes)

print(cats.categories)

print(pd.value_counts(cats))

gn = ['Youth', 'YoungAdult', 'Middleage', 'Senior']

c = pd.cut(ages, bins, labels=gn)

print(c.codes)

data = np.random.randn(20)

s = pd.cut(data, 4, precision=2)

print(s)

a = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])

print(a)


data = pd.DataFrame(np.random.randn(1000, 4))

print(data.describe())

col = data[2]

print(data[np.abs(col) > 3).any(1)])

