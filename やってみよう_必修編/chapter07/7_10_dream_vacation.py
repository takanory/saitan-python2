name_prompt = "\nあなたのお名前は？ "
place_prompt = "世界中どこでも好きなところに行けるとしたらどこに行きたいですか？ "
continue_prompt = "\n誰か他に回答してくれる人はいますか？ (yes/ no) "

# 回答は {name: place} の形式で保存される
responses = {}

while True:
    # ユーザーに行きたい場所を聞く
    name = input(name_prompt)
    place = input(place_prompt)

    # 回答を保存する
    responses[name] = place

    # 誰か他に回答する人がいるか確認する
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# アンケート結果を表示する
print("\n--- アンケート結果 ---")
for name, place in responses.items():
    print(f"{name.title()}さんが行きたいのは{place.title()}です。")
