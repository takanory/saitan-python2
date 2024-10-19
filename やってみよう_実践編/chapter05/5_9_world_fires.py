from pathlib import Path
import csv

import plotly.express as px


path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 緯度経度と明るさを取り出す
lats, lons, brights = [], [], []
for row in reader:
    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
    except ValueError:
        # 無効な行の日付情報を表示する
        print(f"無効なデータ: {row[5]}")
    else:
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# 世界地図に明るさをプロットする
title = "世界の山火事の活動"
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
        color=brights,
        color_continuous_scale='YlOrRd',
        labels={'color':'明るさ'},
        projection='natural earth',
    )

fig.show()
