prompt = "\n何歳ですか？"
prompt += "\n終了するには「終了」と入力してください: "

while True:
    age = input(prompt)
    if age == '終了':
        break
    age = int(age)

    if age < 3:
        print("  無料で入場できます！")
    elif age < 13:
        print("  料金は1000円です。")
    else:
        print("  料金は1500円です。")
