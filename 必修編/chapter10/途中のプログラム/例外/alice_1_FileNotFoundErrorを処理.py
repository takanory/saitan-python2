from pathlib import Path


path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError: 
    print(f"ごめんなさい。{path} は見当たりません。")