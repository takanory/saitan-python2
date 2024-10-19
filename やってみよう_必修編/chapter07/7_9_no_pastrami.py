sandwich_orders = [
    'パストラミ', '野菜', 'ハム', 'パストラミ',
    '玉子', 'ツナ', 'パストラミ']
finished_sandwiches = []

print("申し訳ありません。今日はパストラミは売り切れです。")
while 'パストラミ' in sandwich_orders:
    sandwich_orders.remove('パストラミ')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"{current_sandwich}サンドを作っています。")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich}サンドができました。")
