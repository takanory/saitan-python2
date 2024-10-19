party_size = input("今晩のディナーは何名ですか？ ")
party_size = int(party_size)

if party_size > 8:
    print("申し訳ありませんが、お待ちいただくことになります。")
else:
    print("お席を準備できます。")
