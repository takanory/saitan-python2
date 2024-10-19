from operator import itemgetter

import requests
import plotly.express as px


# API呼び出しを作成してレスポンスを確認する
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"ステータスコード: {r.status_code}")

# 各投稿の情報を処理する
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:20]:
    # 投稿ごとに新規のAPI呼び出しを作成する
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # 各記事の辞書を構築スル
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        # YCの特別な投稿ではコメントは無効
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

# グラフ化のためにデータを処理する
article_links, comment_counts, hover_texts = [], [], []
for submission_dict in submission_dicts:
    # Shorten long article titles.
    title = submission_dict['title'][:30]
    discussion_link = submission_dict['hn_link']
    article_link = f'<a href="{discussion_link}"">{title}</a>'
    comment_count = submission_dict['comments']

    article_links.append(article_link)
    comment_counts.append(comment_count)
    # 完全なタイトルをホバーテキストで表示する
    hover_texts.append(submission_dict['title'])

# 可視化を作成する
title = "Hacker Newsで最も活発なディスカッション"
labels = {'x': '記事', 'y': 'コメント数'}
fig = px.bar(x=article_links, y=comment_counts, title=title, labels=labels,
        hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
