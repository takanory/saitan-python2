# LinuxでのPythonインストール手順

Linuxはプログラミングのために設計されており、たいていのLinuxにはすでにPythonがインストールされています。
Linuxを使用する人は、プログラミングをすることが期待されています。
このため、プログラミングを開始する際に設定を変更したりインストールしたりする必要がほとんどありません。

## Pythonのバージョンを確認する

ターミナルアプリケーションを起動します（Ubuntuでは`Ctrl`＋`Alt`＋`T`キーを押す）。
どのバージョンのPythonがインストールされているかを確認するために、小文字の`p`から始まる`python3`を入力します。
Pythonがインストールされている場合は、このコマンドによってPythonインタープリタが起動します。
すると、インストールされているPythonのバージョンが次のように表示されます。
また、Pythonプロンプト（`>>>`）が表示されて、Pythonのプログラムが入力できるようになります。

```bash
$ python3
Python 3.10.4 (main, Apr  . . . , 09:04:19) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

この表示は、初期状態でPCにPython 3.10.4がインストールされていることを示しています。
表示を確認したら、`Ctrl`＋`D`キーを押すか`exit()`を入力してPythonプロンプトを抜け、ターミナルのプロンプトに戻ります。
本書で`python`コマンドを見かけた場合は、代わりに`python3`と入力してください。

## Pythonをターミナル上で動かす

ターミナル上に`python3`と入力して短いPythonコードを実行してみましょう。 
Pythonのバージョンを事前に確認してください。
Pythonが起動したら、ターミナル上に次のように入力します。

```bash
>>> print("こんにちはPythonインタープリタ！")
こんにちはPythonインタープリタ！
>>>
```
メッセージがターミナル画面に直接表示されます。 
Pythonインタープリタを終了する際には、`Ctrl`＋`D`キーを押すか`exit()`を入力することを忘れないでください。

## VS Codeをインストールする

Ubuntu Linuxでは、Ubuntu Software CenterからVS Codeをインストールできます。
メニューのUbuntu Softwareアイコンをクリックし、**vscode**を検索します。 
［Visual Studio Code］（**code**と表示される場合もあります）というアプリをクリックし、［Install］をクリックします。
インストール後は**VS Code**を検索してアプリを起動します。
