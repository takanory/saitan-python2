requested_toppings = ['マッシュルーム', 'ピーマン', 'エクストラチーズ']

for requested_topping in requested_toppings:
    if requested_topping == 'ピーマン':
        print("申し訳ありません、ピーマンは品切れです。")
    else:
        print(f"ピザに{requested_topping}を追加します。")

print("\nピザができました！")
