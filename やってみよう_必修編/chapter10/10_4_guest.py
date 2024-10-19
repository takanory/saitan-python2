from pathlib import Path

path = Path('guest.txt')

name = input("お名前は? ")
path.write_text(name)