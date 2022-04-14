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


