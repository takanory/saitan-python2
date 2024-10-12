my_foods = ['ピザ', 'だんご', 'ケーキ']

# これはコピーとしては正しく動作しません
friend_foods = my_foods

my_foods.append('チョコレート')
friend_foods.append('アイスクリーム')

print("私の好きな食べ物")
print(my_foods)

print("\n友達が好きな食べ物")
print(friend_foods)
