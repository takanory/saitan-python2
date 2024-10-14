from die import Die

# D6を作成する
die = Die()

# サイコロを転がし、結果をリストに格納する
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 結果を分析する
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
