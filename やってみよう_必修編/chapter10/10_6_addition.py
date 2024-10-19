try:
    x = input("何か数を教えてください: ")
    x = int(x)

    y = input("もう一つ何か数を教えてください: ")
    y = int(y)
except ValueError:
    print("すみません、数字でお願いします。")
else:
    sum = x + y
    print(f"{x}と{y}の合計は{sum}です。")