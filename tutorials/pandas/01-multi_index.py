import pandas as pd

index = index = [('California', 2000), ('California', 2010),
                 ('New York', 2000), ('New York', 2010),
                 ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]

pop = pd.Series(populations, index=index)
pop = pop.reindex(pd.MultiIndex.from_tuples(index))
print(pop)
print('-' * 80)

pop_df = pd.DataFrame({'total': pop})
print(pop_df)

print('-' * 80)

und_18 = [9267089, 9284094, 4687374, 4318033, 5906301, 6879014]
pop_df = pop_df.assign(under18=und_18)
print(pop_df)

print('-' * 80)
print('another way...')
print(pd.DataFrame({'total': pop, 'under18': und_18}))


print('-' * 80)

f_u18 = pop_df['under18'] / pop_df['total']
print('->', type(f_u18), '<-')
print(f_u18)
print(f_u18.unstack())


print('-' * 80)

data = {('California', 2000): 1,
        ('California', 2010): 2,
        ('Texas', 2000): 3,
        ('Texas', 2010): 4,
        ('New York', 2001): 5,
        ('New York', 2010): 6}

print(pd.Series(data))
print('\n***\n')
print(pd.DataFrame(data, index=['one', 'two']))

print('=' * 80)
print('| setting columns to be the MultiIndex')
print('-' * 20)
print()
df = pd.DataFrame([['2000-01-03', 'Michael', 200],
                   ['2000-01-03', 'George', 500],
                   ['2000-01-03', 'Lisa', 450],
                   ['2000-01-04', 'Michael', 180.5],
                   ['2000-01-04', 'George', 450]],
                  columns=['Date', 'Name', 'Dollars'])
print(df)
print()
print(df.set_index(['Date', 'Name']))
