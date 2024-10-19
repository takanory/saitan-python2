from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nファイルを読み込んでいます: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("  すみません、ファイルが見つかりません。")
    else:
        print(contents)