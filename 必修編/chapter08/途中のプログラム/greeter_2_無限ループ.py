def get_formatted_name(first_name, last_name):
    """フォーマットされたフルネームを返す"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# これは無限ループです！
while True:
    print("\nPlease tell me your name:")
    l_name = input("姓を入力してください: ")
    f_name = input("名を入力してください: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nこんにちは{formatted_name}！")
