import plotly.express as px

from die import Die

# 2個のD6サイコロを作成する
die_1 = Die()
die_2 = Die()

# サイコロを転がし、結果をリストに格納する
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 結果を分析する
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 結果を可視化する
title = "2個の6面サイコロを1,000回転がした結果"
labels = {'x': '結果', 'y': '発生した回数'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
