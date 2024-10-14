from die import Die

# D6を作成する
die = Die()

# サイコロを転がし、結果をリストに格納する
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
