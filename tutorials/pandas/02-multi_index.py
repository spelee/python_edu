# Creating MultiIndex

import pandas as pd
import numpy as np

# Explicitly
mi_1 = pd.MultiIndex.from_arrays([['a', 'b', 'b', 'b'], ['one', 'two', 'three', 'four']])
print(mi_1)
print()
print(pd.DataFrame(np.random.rand(4, 2), index=mi_1))

print('-' * 80)

mi_2 = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], ['one', 'two', 'one', 'four']], names=['idx1', 'idx2'])
print(mi_2)
print()
df = pd.DataFrame(np.random.rand(4, 1), index=mi_2)
df.index.names = ['new_col1', 'new_col2']
print(df)

print('-' * 80)

dat = np.random.rand(4,6)
print(dat)
print()
dat = np.round(dat, 1)
print(dat)
print()
print(dat[:, ::2])
