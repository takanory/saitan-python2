# ピザの注文に関する情報を格納する
pizza = {
    'crust': 'レギュラー',
    'toppings': ['マッシュルーム', 'エクストラチーズ'],
    }

# Summarize the order.
print(f"あなたが注文したのは{pizza['crust']}生地のピザで、"
    "トッピングは以下のとおりです。")

for topping in pizza['toppings']:
    print(f"\t{topping}")
