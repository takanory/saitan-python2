from survey import AnonymousSurvey

# 質問文を定義し、アンケート調査を作成する
question = "最初に勉強した言語は何ですか？"
language_survey = AnonymousSurvey(question)

# 質問を表示し、質問に対する回答を保存する
language_survey.show_question()
print("'q' を入力すると終了します\n")
while True:
    response = input("言語: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# アンケート調査の結果を表示する
print("\nアンケート調査にご協力ありがとうございます！")
language_survey.show_results()
