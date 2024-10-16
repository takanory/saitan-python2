from pathlib import Path


def count_words(path):
    """ファイルに含まれるだいたいの単語の数を数える。""" 
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"ごめんなさい。{path} は見当たりません。")
    else:
        # ファイル内のだいたいの単語の数を数える
        words = contents.split()
        num_words = len(words)
        print(f"ファイル {path} には約{num_words}の単語が含まれます。")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)