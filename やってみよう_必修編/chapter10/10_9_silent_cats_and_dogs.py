from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nファイルを読み込んでいます: {filename}")
        print(contents)