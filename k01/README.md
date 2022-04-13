# day01: 開発環境

プログラミングの一番の基盤は，IDE（開発環境）．IDEとは

1. Code Editor
    - ソースコードを書くソフトウェア
2. Debugger(Linter, Fomatter, Tester)
    - ソースコードのバグを発見するソフトウェア
    - Linter(リンター): ソースコードの文法チェック
    - Formatter(フォーマッター): 文法に沿ったソースコードの整然化
    - Tester(テスター): プログラムの動きを確認するためのテスト（仮のデータ入力と想定される出力）を走らせるしくみ
3. Interpreter(Compiler,Builder)
    - ソースコードを実行するソフトウェア
の3種のソフトウェアです．

## 1.Python

「Python」（パイソン）には2つの意味があります．（蛇の種類の意味以外に）

1. プログラミング言語
2. インタプリタ・コマンド（実行ファイル）

本来は上記1のプログラミング言語であるPython語のことですが，このPython語で書かれたソースコードを読んでアプリケーション化するコマンドもまたpythonと読んでいます．

Pythonコマンドもまたアプリケーションで，元はソースコードがあり，そのソースコードをビルドすることでpythonコマンドが生成されています．そのソースコードは，さまざまなプログラミング言語で書かれたバージョンがあり，もっとも有名なものはCPython，C言語というプログラミング言語で書かれたものです．その他にはJava言語で書かれたJPythonなどもあります．

ともあれ，自分のPCにpythonコマンドをインストールしましょう．

...とその前に，プログラミング演習Ⅰで，すでにインストールしていましたね．でも，本当に今もそのままですか？

- あとでanacondaとかインストールしたりしていませんか？
- 環境変数PATHとかをいじったりしていませんか？

今後のプログラミング演習Ⅱの進行のために，全員の開発環境を同じものにしたく，まず，現在インストールしてあるすべてのpythonコマンドをアンインストールしたいと思います．

### 1.1. pythonコマンドの種類

windowsで，`python`　とコマンドラインで打ったときに呼び出される`python.exe`は，典型的には次の4つです．

0. MS Python（ダミー）: Windowsに最初から入っているもの
1. MS python    : Microsoft Store から入手したもの
2. Anaconda python : Anaconda に付属してきたもの
3. 素python      : 公式サイト python.org から入手したもの

これらは，インストール先をいじっていなければ，デフォルトのインストール先が決まっています．

> **0. MS Pyton（ダミー）**
> - exeファイルの場所は
> > %LOCALAPPDATA%\Microsoft\WindowsApps\python.exe
> - これはアプリケーション本体ではありません．ただのショートカットです．この`python`を呼ぶと，Microsoft StoreのPythonのページが立ち上がります．「入手」を押すと，1のMS Pythonを入手することになります．
> - 1のMS Pythonをインストールしたあとは，このショートカットの先は「Microsoft StoreのPythonページ」から「1のMS Python」に変わります．

> **1. MS Python本体**
> - exeファイルの場所は 
> > %LOCALAPPDATA%\Microsoft\WindowsApps\PythonSoftwareFoundation.Python(Version)***\python.exe
> - MicosoftStore版python （↓のCの不完全版）
> - 端末で何の気なしに `python` と打つと連れていかれるMicrosoftStoreのPython売り場で手に入れるPython本体

> **2のAnaconda python**
> - exeファイルの場所は
> > %USERPROFILE%\anaconda3\Scripts\python.exe

> **3の素Python**
> - exeファイルの場所は
> > %LOCALAPPDATA%\Programs\Python\Python(Version)\python.exe

コマンドプロンプトで，それぞれの場所，

```{.sh}
> %LOCALAPPDATA%\Microsoft\WindowsApp\python.exe
```

などと打ってみてください．

ここで出てきた種類だけのPythonがあなたのPCにはインストールされているということです．

では，このpythonたちをアンインストールします．

1. 上記の確認作業で，Anaconda pythonの存在が確認された人は，最初にanacondaをアンインストールします．Anacondaをインストールした覚えのない人も念の為に次のコマンドをどこかで動かしてください．

```{.sh}
> conda install -c anaconda anaconda-clean
> anaconda-clean
```

2. 一般的にWindowsでインストールしたものはギアアイコンの「設定」から「アプリと機能」，「python」を検索すると出てきます．ここでアンインストールを選びます．複数見つかることもあります．

3. 環境変数のPATHにpythonに関する記述があれば，その部分を削除します．

### 1.2. pythonコマンドのインストール

ぶっちゃけ何でも構いませんが，皆と同じ環境にしたいなら，演習Ⅱでは「素python」をおすすめします．すなわち[公式サイト](https://www.python.org/) からインストールしてください．

**その際にPATHの設定を加えるか聞かれるかもしれませんが，「いいえ」です．また，インストール後に手動でPATHの設定を加える必要もありません．**

**windowsの人は，今後，pythonコマンドは`python`ではなく，`py`を使います．**

- `python foo.py`ではなく，  `py foo.py` です．
- `python -m mod` ではなく，`py -m mod`　です．
- `python -VV`　ではなく，`py -VV`です．

(macの人向けのお話）

```{.sh}
> brew install pyenv
> pyenv install 3.10
> pyenv global 3.10
```

## 2. vscode

[Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)

Microsoft Windowsには昔々から，Visual StudioというIDE（頭で紹介したエディタ・デバッガ・インタプリタ）すべての入ったソフトウェアがあります[Visual Studio](https://azure.microsoft.com/ja-jp/products/visual-studio/)．ただし，WindowsOS専用です．また，とても大きなソフトウェアであり，手軽に扱えるものではありません．

Visual Studio Code (以下，`vscode`や`code`)は，そのエディタに特化したものとなります．
ただし，拡張機能を多く備えることができ，エディタでありながら，デバッグ，ビルドも可能なものとなっています．さらに，WindowsOSだけでなく，MacOS，LinuxOSでも同じように使用できます．

### 2.1. vscodeの使い方

vscodeはエディタですが，プログラミングに特化したエディタです．

プログラミングでは，あるアプリケーションを作ろうとなった場合に，
「プロジェクト」と呼ぶフォルダを作り，その中にソースコードやらリソースファイル（アイコンや画像や音楽ファイルなど），説明書(Readme)，ライセンス(License)を入れます．

vscodeでは，ファイルを一つ一つ開くのではなく，この「プロジェクト」のフォルダを開きます．

フォルダを開いたあと，そのフォルダルート（根っこ）を起点として，その下にあるソースコードを編集したり，ファイルを加えたり削除したりの整理をしたりします．

### 2.2. vscodeの拡張機能

以下の拡張機能をインストールしてください．

[日本語パック拡張機能](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)

[Python用拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 3. poetry

演習ⅠやWeb上のいろんなサイトで，numpyその他のパッケージをインストールする際に`pip`や`conda`を使っているかもしれませんが，この演習Ⅱでは`poetry`を使います．

まず，poetryをインストールしましょう．

> `py -m pip install poetry`

macやlinuxの人は，`python -m pip install poetry`

インストールの最後に，「PATHに〜を追加せよ」と表示されるので，「虫眼鏡」アイコンから「環境変数」を検索し，「環境変数を編集」から
PATHについて「新規」で上記の「〜」の部分を追加してください．

```
C:\Users\kotaro\AppData\Local\Programs\Python\Python310\Scripts\
```

### 3.1. poetry の使い方

poetryは単なるパッケージインストーラではなく，むしろ「プロジェクト」フォルダのマネージャです．

何はともあれ，最初に次のようにしてください．どのフォルダでもいいです．

```{.sh}
> poetry config virtualenvs.in-project true
```

**プロジェクトを始めるときには，**

0. とりあえずプロジェクトフォルダを作ります．これはエクスプローラでもいいでしょう．
1. プロジェクトフォルダの整理

コマンドプロンプトで，このフォルダに移動(`cd foo`)したあと，

```{.sh}
> poetry init
```

と打ちます．すると，いろいろ聞かれますが，適切に答えると，フォルダの中に`pyproject.toml`というファイルが作られます．
2. プロジェクトフォルダの仮想環境作成

続けて，

```{.sh}
> poetry shell
```

と打ちます．すると，コマンドプロンプトの先頭が`(.venv)`となるでしょう．

3. プロジェクトフォルダの仮想環境から抜ける

```{.sh}
> exit
```

と打つと，もとの状態に戻ります．

**なにかパッケージを入れたいとき**

例えば`numpy`を入れたいときは，**普通の状態で(.venv環境ではない）**

```{.sh}
> poetry add numpy`
```

などとします．そうすると，`(.venv)`環境で`import numpy`が可能になります．

**vscodeでコーディング**

vscodeでプロジェクトを開き，pythonソースコードを編集しようとすると，インタプリタを聞かれます．このときには，`./.venv/bin/python.exe`を選ぶようにします．


## 4. 早速やってみよう

python, vscode, poetryのインストールが終わったら, 「プログラミング演習Ⅱ」用の準備をします．

1. 「ドキュメント」の下に，`psp2`というフォルダを作ります．今後は，このフォルダの下にいろいろ課題に対するソースコードやいろいろを置いていきます．
2. その`psp2`というフォルダの下に移動します．

```{.sh}
> cd c:\Users\kotaro\Documents\psp2
```

3. そこで，pythonプログラミングの準備をします．

```{.sh}
> poetry config virtualenvs.in-project true
> poetry init
```

いろいろ聞かれます．よく読んで答えましょう．基本的にはすべて提示されたままでいいですが，Authorについては，`Kotaro Sonoda <aa83988848@ms.nagasaki-u.ac.jp>`などと，「`自分の名前 スペース 三角カッコ
 メールアドレス 三角カッコ閉じ`」にしましょう．

続けて，vscodeでのプログラミングを便利にするために，`ipykernel`というpythonモデュールをインストールします．

```{.sh}
> poetry add ipykernel
```

続けて，

```{.sh}
> poetry shell
```

と打つと，「仮想環境」という独立した環境が構成されます．`>`という「プロンプト」が`(.venv)>`に変わります．とりあえず今は仮想環境から脱出しておきます．

```{.sh}
(.venv)> exit
```

## 5. それでは今日の課題をやっていきましょう．

vscodeを起動します．

![起動直後](vscode01.png)

左端にあるアイコンは，メニューです．一番下にある帯には，現在開いているファイルに関する「状態」が表示されています．

ウィンドウのほとんどの部分は，エディタです．「ファイル名　x」という感じで，最近のウェブブラウザのように「タブ」が並びます．

初期起動時には，「Get Started」というタブが立ち上がっています．使わないので「x」を押して消してください．

一番上にあるアイコンを押してください．これは「エクスプローラ」と呼ばれています．

![エクスプローラ](vscode02.png)

`OPEN EDITORS`には，現在開いているエディタで編集しているファイル名が並びます．先ほどタブを閉じたので何もありません．

その下には`NO FOLDER OPENED`と表示され，何やら青いボタンが並んでいます．

説明したように，「ファイルを開く」のではなく，「フォルダを開く」というボタンです．ちなみに下のボタン「Clone Repository」は「レポジトリ」と呼ばれる特殊なフォルダを開くボタンです．

さきほど作った`psp2`フォルダを開きます．

![psp2フォルダを開いた](vscode03.png)

「`NO FOLDER OPENED`」の表示が「`psp2`」に変わり，

```{.sh}
v PSP2
  > .venv
  pyproject.toml
```

と表示されていると思います．

「`PSP2`」のあたりにマウスを移動させると，その帯の右側に4つのアイコンが並びます．それぞれのアイコンにマウスを移動させると説明が表示されますが，左から，「ファイルを追加」「フォルダを追加」「更新」「表示を縮める」です．

なにかプログラミングしてみましょう．

「ファイル追加」アイコンを押して，「`k00.py`」という名前のファイルを新しく作ってみます．

![ファイル追加](vscode04.png)

「OPENED EDITORS」に`k00.py`が列挙され，`k00.py`というタブが開きます．

そこに以下のようなコードを書きましょう．

```{.py}
# coding:utf-8

# %%
# 使うモジュールの指定
# turtleというモジュールを使う
import turtle

# %%
turtle.setup(width=300, height=300)

# %%
# kame1, kame2は，turtleモジュールに定義されているTurtle型
# kame1の形は矢印，kame2の形はカメ
kame1 = turtle.Turtle(shape='arrow')
kame2 = turtle.Turtle(shape='turtle')

# %%
kame1.pencolor('red')
kame2.pencolor('blue')

# %%
kame1.penup()
kame1.goto(50,50)

kame2.penup()
kame2.goto(-50,50)

kame1.pendown()
kame2.pendown()

# %%
kame1.left(60)
kame2.left(120)

# %%
kame1.forward(100)
kame2.backward(200)

# %%
turtle.exitonclick()

# %%
```

- 「`#`」記号のある行はいわゆるコメントアウトで，pythonの実行コードから無視されます．
- コメントアウト，文字列，など色分けされていますね．
- 最初の行のコメントアウト「`# coding:utf-8`」は，このソースコードの日本語が文字コード「`utf-8`」で書かれていることをIDEに教えています．Windowsの場合は文字コードが「`shift-jis`」かもしれません．

また，このソースコードをvscodeで書くと，
「`# %%`」と書かれた部分の上に，

```{.sh}
「Run Cell | Run Below | Debug Cell」
------------------------------------------
# %%
```

という表示が見えます．この部分は実際のソースコードを勝手にいじったわけではありません．vscodeがただ見せているだけです．
これについては，あとで説明します．

では，この`k00.py`を実行しましょう．

vscodeとは別に，コマンドプロンプトを立ち上げて，

```{.sh}
> cd c:\Users\kotaro\Documents\psp2
```

で`psp2`フォルダに移動し，

```{.sh}
> python k00.py
```

とすればプログラムが動きます．

これでもいいのですが，vscodeはウィンドウの中でコマンドプロンプトを起動できます．上部メニューに「ターミナル」があり，そこに「新しいターミナルを開く」というのがあります．

![ターミナル](vscode05.png)

「(.venv)」プロンプトのコマンドプロンプトがエディタの下の領域に立ち上がります．フォルダも現在作業中の場所に移動しています．ここで

```{.sh}
(.venv) > python k00.py
```

でよいでしょう．

**で，このソースコードは，どんなプログラムでしょうか？**

ざっくり言うと，新しくウインドウが立ち上がって，矢印とカメがそれぞれ線を描きながら動いて停止します．ちなみに，ウインドウが立ち上がったままですが，ウインドウ内のどこかでクリックすると，ウインドウが閉じます．

というわけで，今日の課題 k00
> このソースコードのそれぞれの行で行われていることを調べて，ソースコードを編集し，正六角形を描画せよ．ただし，左半分は矢印で赤，右半分はカメで青で描くこと．また，自分で編集したソースコードのそれぞれの行で行われていることをコメントアウトに追加せよ．

課題は，

- LACSの課題から，ソースコードと正六角形が描画されたウィンドウのスクリーンショットを提出してください．
- 初めての提出作業は4月20日正午までに必ず行ってください．**この期限以降は再提出以外は受け付けません．** 課題提出があると，TAや私がそれを採点し，改善点があればコメントを残します．
- コメントを踏まえて再度提出し，10点満点を目指し何度でも提出を受付ます．課題k00の最終期限は4月27日正午までとします．**この期限以降は再提出はできません．**
- 今後の課題も，基本的には，初めての提出の期限を1週間後，最終期限を2週間後とします．

## 6. 便利なvscode用コメントアウト　「`# %%`」

ソースコードは基本的には，`python k00.py`だと最初の行から最後の行まですべての工程を行います．

コードのそれぞれの行で何を行っているか調べるなら，もしくは新しく文を書いて，その動きを確かめたいのなら，pythonだとIPythonが有名です．IPythonは，JupyterやGoogle Colabを動かしているプログラムです．

ターミナルやコマンドプロンプトで，`ipython`と打つと，

```{.sh}
(.venv) kotaro@calvados psp2 % ARM❯ ipython                                [04/12 21:31]
Python 3.10.0 (default, Jan 13 2022, 14:22:16) [Clang 13.0.0 (clang-1300.0.29.30)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.2.0 -- An enhanced Interactive Python. Type '?' for help.
Unable to automatically import mitosheet

In [1]: 
```

のように，インタラクティブモードが立ち上がります．

```{.sh}
In [1]: x = 10

In [2]: print(x)
10
```

のように，JupyterやGoogle Colabと何ら変わりません．

ただ，問題なのは，このインタラクティブモードで書いたソースコードは保存されないということ．JupyterやGoogle Colabで書いたものも，基本的には「jupyter notebook」（拡張子は `.ipynb`）であり，pythonのソースコード(`.py`)ではないということです．

JupyterやGoogle Colabではメニューから，JupyterNotebook(`.ipynb`)からpythonソースコード(`.py`)に変換することは可能ですが，

僕らが今欲しいのは，書いているpythonソースコードをブロック毎に動きを確かめたい．そこで，vscodeの「`# %%`」です．

実は，

```{.sh}
「Run Cell | Run Below | Debug Cell」
------------------------------------------
# %%
```

は，vscode上で，pythonソースコードを簡単にインタラクティブモードで動かすコメントアウトになっているのです．凄い便利！！

「`# %%`」から次の「`# %%`」までが，IPythonの「セル」です．

- 「Run Cell」は，セルを実行する
- 「Run Below」は，以下のすべてのセルを実行する
- 「Debug Cell」は，セルをデバグする．（デバグについては後日）
