from pathlib import Path


path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"ごめんなさい。{path} は見当たりません。")
else:
    # ファイル内のだいたいの単語の数を数える
    words = contents.split() 
    num_words = len(words) 
    print(f"ファイル {path} には約{num_words}の単語が含まれます。")