prompt = "\n何か書いてください。繰り返してお返事します。"
prompt += "\nプログラムを止めるには '終了' と入力してください。 "

message = ""
while message != '終了':
    message = input(prompt)
    print(message)