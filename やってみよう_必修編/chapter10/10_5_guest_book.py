from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nこんにちは。お名前は? "
prompt += "\nあなたが最後のゲストの場合は「終了」と入力してください。 "

guest_names = []
while True:
    name = input(prompt)
    if name == '終了':
        break

    print(f"{name}さんありがとうございます。ゲストブックに追加します。")
    guest_names.append(name)

# それぞれの名前の最後に "\n" を追加した文字列を作る
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)