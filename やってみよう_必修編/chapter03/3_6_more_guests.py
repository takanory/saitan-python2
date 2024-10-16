guests = ["guido van rossum", "kwon-han bae", "georgi ker"]

name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"\nすいません、{name}さんが夕食に参加できなくなりました。")

# Kwon-Hanさんの代わりにCheukさんを招待します
del guests[1]
guests.insert(1, 'cheuk ting ho')

# 再度、招待メッセージを取得する
name = guests[0].title()
print(f"\n{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

# 大きなテーブルを見つけたので、追加のゲストを招待する
print("\n大きなテーブルを見つけた！")
guests.insert(0, 'deb nicholson')
guests.insert(2, 'denny perez')
guests.append('iqbal abdullah')

name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[3].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[4].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[5].title()
print(f"{name}さん、ぜひ夕食に来てください。")
