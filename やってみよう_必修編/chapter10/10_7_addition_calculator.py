print("終了したい時には「終了」と入力してください。\n")

while True:
    try:
        x = input("何か数を教えてください: ")
        if x == 'q':
            break
        x = int(x)

        y = input("もう一つ何か数を教えてください: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("すみません、数字でお願いします。")

    else:
        sum = x + y
        print(f"{x}と{y}の合計は{sum}です。")