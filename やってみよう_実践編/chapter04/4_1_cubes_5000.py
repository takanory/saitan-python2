import matplotlib.pyplot as plt

# データを定義する
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# グラフを作成する
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# グラフのタイトルと軸ラベルを設定する
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# 目盛りラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)

# グラフを表示する
plt.show()
