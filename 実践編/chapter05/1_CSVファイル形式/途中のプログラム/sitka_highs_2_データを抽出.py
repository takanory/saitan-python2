from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 最高気温を取り出す
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)
