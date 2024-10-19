prompt = "\nトッピングは何がいいですか？"
prompt += "\n終了するには「終了」と入力してください: "

while True:
    topping = input(prompt)
    if topping != '終了':
        print(f"  ピザに{topping}を追加します。")
    else:
        break
