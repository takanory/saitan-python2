sandwich_orders = ['野菜', 'ハム', '玉子', 'ツナ']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"{current_sandwich}サンドを作っています。")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich}サンドができました。")
