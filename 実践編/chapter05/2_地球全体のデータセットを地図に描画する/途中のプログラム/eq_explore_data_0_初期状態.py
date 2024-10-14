from pathlib import Path
import json

# データを文字列として読み込み、Pythonのオブジェクトに変換する
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# より読みやすいデータファイルを作成する
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
