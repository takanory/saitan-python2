from pathlib import Path


path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("誕生日をmmddyyフォーマットで入力してください: ")
if birthday in pi_string:
    print("円周率の最初の100万桁にあなたの誕生日が見つかりました！")
else:
    print("円周率の最初の100万桁にあなたの誕生日は見当たらないようです。")