import plotly.express as px

from die import Die


# D6とD10のサイコロを作成する
die_1 = Die()
die_2 = Die(10)

# サイコロを転がし、結果をリストに格納する
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# 結果を分析する
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

frequencies = [results.count(value) for value in poss_results]

# 結果を可視化する
title = "6面と10面サイコロを50,000回転がした結果"
labels = {'x': '結果', 'y': '発生した回数'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# グラフをさらにカスタマイズする
fig.update_layout(xaxis_dtick=1)

fig.show()
