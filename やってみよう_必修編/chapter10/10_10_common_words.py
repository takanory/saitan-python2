from pathlib import Path

def count_common_words(filename, word):
    """テキスト内の単語の出現回数を数える。"""
    # 注: これは非常に大雑把な推定値なので、実際の数よりも
    # 大きな値が返されます。
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}'は{filename}内で約{word_count}回出現します。"
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')