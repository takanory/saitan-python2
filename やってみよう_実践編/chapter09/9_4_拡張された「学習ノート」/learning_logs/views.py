from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """学習ノートのホームページ"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """現在のユーザーのすべてのトピックを表示し、他のユーザーのトピックのうち
    公開されたものを表示する。
    """
    # 適切なトピックをすべて取得する。
    # もしユーザーがログインしていたら、そのユーザのすべてのトピックと、
    # 他のユーザからのすべての公開トピックを取得。
    # ユーザーがログインしていない場合, 全ての公開トピックを取得。
    if request.user.is_authenticated:
        topics = Topic.objects.filter(owner=request.user).order_by('date_added')
        # 現在のユーザーが所有していない公開トピックをすべて取得する。
        # 注: クエリーを括弧で囲むことで、長いクエリーを複数行に分割することが
        # できます。
        public_topics = (Topic.objects
            .filter(public=True)
            .exclude(owner=request.user)
            .order_by('date_added'))
    else:
        # ユーザーは認証されていないのですべての公開トピックを返す。
        topics = None
        public_topics = Topic.objects.filter(public=True).order_by('date_added')

    context = {'topics': topics, 'public_topics': public_topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """1つのトピックとそれについてのすべての記事を表示"""
    topic = Topic.objects.get(id=topic_id)

    # 現在のユーザーがこのトピックを所有している場合にのみ
    # new_entryとedit_entryのリンクを表示したい。
    is_owner = False
    if request.user == topic.owner:
        is_owner = True

    # トピックが他の人のもので、かつ公開されていない場合、
    # エラーページを表示する。
    if (topic.owner != request.user) and (not topic.public):
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, 'is_owner': is_owner}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """新規トピックを追加する"""
    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = TopicForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # 空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """特定のトピックに新規記事を追加する"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = EntryForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # 空または無効のフォームを表示する
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """既存の記事を編集する"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初回リクエスト時は現在の記事の内容がフォームに埋め込まれている
        form = EntryForm(instance=entry)
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)