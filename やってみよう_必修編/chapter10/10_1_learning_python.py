from pathlib import Path

print("--- ファイル全体を読み込みます:")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- 各行をループします:")
lines = contents.splitlines()
for line in lines:
    print(line)
