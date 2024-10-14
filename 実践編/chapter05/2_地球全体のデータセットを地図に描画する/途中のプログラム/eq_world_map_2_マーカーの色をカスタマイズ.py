from pathlib import Path
import json

import plotly.express as px

# データを文字列として読み込み、Pythonのオブジェクトに変換する
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# データセットにあるすべての地震を調べる
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = '世界の地震'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color': 'マグニチュード'},
        projection='natural earth',
    )
fig.show()
