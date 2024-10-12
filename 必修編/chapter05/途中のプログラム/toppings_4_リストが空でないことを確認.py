requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"トッピングに{requested_topping}を追加します。")
    print("\nピザができました！")
else:
    print("プレーンピザでよろしいですか？")
