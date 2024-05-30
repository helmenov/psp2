- [day01: 開発環境](#day01-開発環境)
  - [1.Python](#1python)
    - [1.1. python コマンドの種類](#11-pythonコマンドの種類)
    - [1.2. python コマンドのインストール](#12-pythonコマンドのインストール)
      - [mac の人向けのお話](#macの人向けのお話)
      - [（ここは上級者向け）](#ここは上級者向け)
  - [2. vscode](#2-vscode)
    - [2.1. vscode の使い方](#21-vscodeの使い方)
    - [2.2. vscode の拡張機能](#22-vscodeの拡張機能)
  - [3. poetry](#3-poetry)
    - [3.1. poetry の使い方](#31-poetry-の使い方)
    - [3.2. **プロジェクトを始めるときには，**](#32-プロジェクトを始めるときには)
      - [0. プロジェクトの親ディレクトリを作ります．](#0-プロジェクトの親ディレクトリを作ります)
      - [1. プロジェクトの親ディレクトリに移動](#1-プロジェクトの親ディレクトリに移動)
      - [2. プロジェクトを作る．](#2-プロジェクトを作る)
      - [3. プロジェクトに必要な外部パッケージのインストール](#3-プロジェクトに必要な外部パッケージのインストール)
    - [3.3. 自作パッケージの配布](#33-自作パッケージの配布)
  - [4. **vscode でコーディング**](#4-vscodeでコーディング)
  - [5. jupyterhub の利用](#5-jupyterhubの利用)

# day01: 開発環境

プログラミングの一番の基盤は，IDE（開発環境）．IDE とは

    1. Code Editor
        - ソースコードを書くソフトウェア
    2. Debugger(Linter, Formatter, Tester)
        - ソースコードのバグを発見するソフトウェア
        - Linter(リンター): ソースコードの文法チェック
        - Formatter(フォーマッター): 文法に沿ったソースコードの整然化
        - Tester(テスター): プログラムの動きを確認するためのテスト（仮のデータ入力と想定される出力）を走らせるしくみ
    3. Interpreter(Compiler,Builder)
        - ソースコードを実行するソフトウェア

の 3 種のソフトウェアです．

## 1.Python

「Python」（パイソン）には 2 つの意味があります．（蛇の種類の意味以外に）

1. プログラミング言語
2. インタプリタ・コマンド（実行ファイル）

本来は上記 1 のプログラミング言語である Python 語のことですが，この Python 語で書かれたソースコードを読んでアプリケーション化するコマンドもまた python と読んでいます．

Python コマンドもまたアプリケーションで，元はソースコードがあり，そのソースコードをビルドすることで python コマンドが生成されています．そのソースコードは，さまざまなプログラミング言語で書かれたバージョンがあり，もっとも有名なものは CPython，C 言語というプログラミング言語で書かれたものです．その他には Java 言語で書かれた JPython などもあります．

ともあれ，自分の PC に python コマンドをインストールしましょう．

...とその前に，すでにインストールしているかも．でも，本当に今もそのままですか？

- あとで anaconda とかインストールしたりしていませんか？
- 環境変数 PATH とかをいじったりしていませんか？

今後のプログラミング演習 Ⅱ の進行のために，全員の開発環境を同じものにしたく，まず，現在インストールしてあるすべての python コマンドをアンインストールしたいと思います．

### 1.1. python コマンドの種類

windows で，`python`　とコマンドラインで打ったときに呼び出される`python.exe`は，典型的には次の 4 つです．

0. MS Python（ダミー）: Windows に最初から入っているもの
1. MS python : Microsoft Store から入手したもの
2. Anaconda python : Anaconda に付属してきたもの
3. 素 python : 公式サイト python.org から入手したもの

これらは，インストール先をいじっていなければ，デフォルトのインストール先が決まっています．

> **0. MS Pyton（ダミー）**
>
> - exe ファイルの場所は
>
> > %LOCALAPPDATA%\Microsoft\WindowsApps\python.exe
>
> - これはアプリケーション本体ではありません．ただのショートカットです．この`python`を呼ぶと，Microsoft Store の Python のページが立ち上がります．「入手」を押すと，1 の MS Python を入手することになります．
> - 1 の MS Python をインストールしたあとは，このショートカットの先は「Microsoft Store の Python ページ」から「1 の MS Python」に変わります．

> **1. MS Python 本体**
>
> - exe ファイルの場所は
>
> > %LOCALAPPDATA%\Microsoft\WindowsApps\PythonSoftwareFoundation.Python(Version)\*\*\*\python.exe
>
> - MicosoftStore 版 python （↓ の C の不完全版）
> - 端末で何の気なしに `python` と打つと連れていかれる MicrosoftStore の Python 売り場で手に入れる Python 本体

> **2 の Anaconda python**
>
> - exe ファイルの場所は
>
> > %USERPROFILE%\anaconda3\Scripts\python.exe

> **3 の素 Python**
>
> - exe ファイルの場所は
>
> > %LOCALAPPDATA%\Programs\Python\Python(Version)\python.exe

コマンドプロンプトで，それぞれの場所，

```{.sh}
> %LOCALAPPDATA%\Microsoft\WindowsApp\python.exe
```

などと打ってみてください．

ここで出てきた種類だけの Python があなたの PC にはインストールされているということです．

では，この python たちをアンインストールします．

1. 上記の確認作業で，Anaconda python の存在が確認された人は，最初に anaconda をアンインストールします．Anaconda をインストールした覚えのない人も念の為に次のコマンドをどこかで動かしてください．

   ```{.sh}
   > conda install -c anaconda anaconda-clean
   > anaconda-clean
   ```

2. 一般的に Windows でインストールしたものはギアアイコンの「設定」から「アプリと機能」，「python」を検索すると出てきます．ここでアンインストールを選びます．複数見つかることもあります．

3. 環境変数の PATH に python に関する記述があれば，その部分を削除します．

### 1.2. python コマンドのインストール

ぶっちゃけ何でも構いませんが，皆と同じ環境にしたいなら，演習 Ⅱ では「素 python」をおすすめします．すなわち[公式サイト](https://www.python.org/) からインストールしてください．

**その際に PATH の設定を加えるか聞かれるかもしれませんが，「いいえ」です．また，インストール後に手動で PATH の設定を加える必要もありません．**

**windows の人は，今後，python コマンドは`python`ではなく，`py`を使います．**

- `python foo.py`ではなく， `py foo.py` です．
- `python -m mod` ではなく，`py -m mod`　です．
- `python -VV`ではなく，`py -VV`です．

#### mac の人向けのお話

mac の人は，最初から python が入っています．

#### （ここは上級者向け）

- システム Python（管理者権限を持つ人しかインストールやアンインストールをできない）
- ユーザー Python をインストールする or システム Python をユーザー Python としても使う
  - ユーザー Python（ユーザが自由にインストール/アンインストールできる）
  - いろいろ入れて取り散らかりがちなので，管理ソフトで管理（どの Python を使うかを設定）すると良い．
    - [mise][mise]（MEEZ,ミーズ） がおすすめ
- 新しくモジュールを作るときは，仮想環境 Python を使う．
  - 仮想環境 Python（ユーザー Python の site-packages を使わない）

## 2. vscode

[Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)

Microsoft Windows には昔々から，Visual Studio という IDE（頭で紹介したエディタ・デバッガ・インタプリタ）すべての入ったソフトウェアがあります[Visual Studio](https://azure.microsoft.com/ja-jp/products/visual-studio/)．ただし，WindowsOS 専用です．また，とても大きなソフトウェアであり，手軽に扱えるものではありません．

Visual Studio Code (以下，`vscode`や`code`)は，そのエディタに特化したものとなります．
ただし，拡張機能を多く備えることができ，エディタでありながら，デバッグ，ビルドも可能なものとなっています．さらに，WindowsOS だけでなく，MacOS，LinuxOS でも同じように使用できます．

### 2.1. vscode の使い方

vscode はエディタですが，プログラミングに特化したエディタです．

プログラミングでは，あるアプリケーションを作ろうとなった場合に，
「プロジェクト」と呼ぶフォルダを作り，その中にソースコードやらリソースファイル（アイコンや画像や音楽ファイルなど），説明書(Readme)，ライセンス(License)を入れます．

**vscode では，ファイルを一つ一つ開くのではなく，この「プロジェクト」のフォルダを開きます．**

フォルダを開いたあと，そのフォルダルート（根っこ）を起点として，その下にあるソースコードを編集したり，ファイルを加えたり削除したりの整理をしたりします．

### 2.2. vscode の拡張機能

以下の拡張機能をインストールしてください．

[日本語パック拡張機能](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)

[Python 用拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 3. poetry

演習 Ⅰ や Web 上のいろんなサイトで，numpy その他のパッケージをインストールする際に`pip`や`conda`を使っているかもしれませんが，この演習 Ⅱ では[`poetry`][poetry] を使います．

まず，poetry をインストールしましょう．

```{powershell}
PS > (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
PS > [System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\AppData\Roaming\Python\Scripts;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

mac や linux の人は，

```{.sh}
> curl -sSL https://install.python-poetry.org | python3 -
```

### 3.1. poetry の使い方

poetry は単なるパッケージインストーラではなく，むしろ「プロジェクト」フォルダのマネージャです．

何はともあれ，最初に次のようにしてください．どのフォルダでもいいです．

```{.sh}
> poetry config virtualenvs.in-project true
> poetry config virtualenvs.options.no-pip true
> poetry config virtualenvs.options.no-setuptools true
```

（上記は，プロジェクトのライブラリ置き場を，プロジェクト内の `.venv` というフォルダに置く，という設定です．この設定をしない場合は，デフォルトで，ユーザの`Virtualenvs`というフォルダの下にプロジェクトごとの env が置かれます）

### 3.2. **プロジェクトを始めるときには，**

プロジェクトとは，パッケージとほぼ同じ意味と考えても結構です．配布（提出）するモジュールが梱包されたディレクトリです．

#### 0. プロジェクトの親ディレクトリを作ります．

これから，さまざまなプロジェクトを作るので，それらを置くための親となるディレクトリを作ります．エクスプローラで作ってもいいでしょう．ディレクトリの名前は何でもいいです．例えば `psp2` とか．

#### 1. プロジェクトの親ディレクトリに移動

たとえばディレクトリの場所が `C:\Users\helmenov\Documents\psp2` ならば，

```{.sh}
> cd C:\Users\helmenov\Documents\psp2
```

#### 2. プロジェクトを作る．

新しくプロジェクトを作ります．たとえば課題１用に， `kadai01` なら，

```{.sh}
> poetry new kadai01
```

と打ちます．すると，いろいろ聞かれますが，適切に答えると，`kadai01` というディレクトリが作られます．

そのディレクトリに入ると，いろいろなものができています．

```{.sh}
kadai01
├── README.md
├── kadai01
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py
```

`kadai01`ディレクトリの中にさらに `kadai01` というディレクトリができています．この深い位置の方の `kadai01` が配布されるパッケージです．このディレクトリの中にあなたがモジュールを作成します．すでに`__init__.py` というものがありますが，とりあえず今は気にせずそのままに．

`pyproject.toml`というファイルがあります．これが「あなたの作ったパッケージを使うためにあらかじめインストールしていなければならないパッケージのリスト」です．さらに，このファイルにはパッケージのバージョンを書きます．

他に， `README.md`というファイルがありますが，これはあなたの作ったパッケージの説明書です．

`tests`というディレクトリは，あなたの作ったパッケージをテストするためのモジュールを置きます．

#### 3. プロジェクトに必要な外部パッケージのインストール

**実は，上記で作ったプロジェクトですが，他のプロジェクトでインストールした外部パッケージを使えません．**

外部パッケージはプロジェクト毎に入れ直してください．

外部パッケージのインストールは，

```{.sh}
> poetry add 外部パッケージ名
```

でおこないます．(`pip install`ではありません)

ちなみに，厳密には「プロジェクトに必要な外部パッケージ」には２種類あり，

- 自作モジュール(.py)の中で import しているパッケージ
- 自作モジュールを import するテストモジュールが他に import しているパッケージ

どちらもインストールは，`poetry add` でインストールしてもいいのですが，後者は自作パッケージ配布のときには不要なパッケージです．

なので`poetry add --group=dev`でインストールしておくと，配布物から取り除かれます．

ちなみに，不要になった外部パッケージは，

```{.sh}
> poetry remove 外部パッケージ
```

で削除できます．

### 3.3. 自作パッケージの配布

作った自作モジュールを詰め込んだ自作パッケージを配布（提出）したいときは，まず`pyproject.toml`の`[tool.poetry]`の`version`の数値を大きくします．

そのあと，

```{.sh}
> poetry build
```

すると，`dist/kadai01-0.1.0-py3-none-any.whl`みたいのができます．これを配布（提出）します．

## 4. **vscode でコーディング**

まず，それぞれのプロジェクトで，

```{.sh}
> poetry add ipykernel --group=dev
```

してください．

その後，vscode でプロジェクトを開き，python ソースコードを編集します．

インタプリタを聞かれます．このときには，`./.venv/bin/python`を選ぶようにします．
（たいていは，自動的にインタプリタが選ばれます）

## 5. jupyterhub の利用

[演習室の JupyterHub][JupyterHub@演習室] を使うこともできます．ただし，学外からは使えません．

学内であれば，まず[Eteks][Eteks@演習室] で使う演習室 PC を決めます．使う PC が起動していない場合は新たに起動してください．

- 起動している場合は色が変わっています．また，その PC に現ログインしている人数が右上に表示されています．
  - JupyterHub のログインは演習室 PC へのログインと同等なので，JupyterHub にログインすると，Eteks のログイン人数に反映されます．
- 電源を切ることもできますが，Eteks のログイン人数が`00`人のときのみ電源を切ってもよいです．（心配なら電源つけっぱでもよいです）
  - **くれぐれも「現ログインしている人がいるのに電源を切る」ことはしないように**

起動していることが確認できたら，[つなぐ演習室 PC の JupyterHub][JupyterHub@演習室]に WebBrowser でアクセスします．

- 左側のディレクトリアイコンがエクスプローラです．
- 右側に Launcher というタブが表示されています．（無ければ`+`ボタンで Launcher が表示されます）

ディレクトリの移動は，エクスプローラでおこないます．

ファイルリストの上に `■ / … / k00 / tests /` のような表示があると思いますが，その`■`が所謂ホームディレクトリで，演習室 PC のあなたのディレクトリの根っこです．`■`をクリックすると，その根っこに移動します．

ファイルリストから移動したいディレクトリをクリックすれば，そのディレクトリに移動します．

移動先のディレクトリの下のファイルリストが表示されている状態で，右側の Launcher で操作します．

- Notebook の python3 を選べば，そのディレクトリに，python3 をカーネルとする notebook が作成されます．
- Other の Terminal は，そのディレクトリに移動した状態で，コマンドプロンプトのような端末操作(CUI 操作)
- Other の Python File は，そのディレクトリに，新しいモジュールを作ります．

poetry をインストールしてみましょう．現在開いているディレクトリがどこでも構いません．

Launcher の Other の Terminal を開きます．

```{.sh}
[sonoda@bes-ex01 ~] $ □
```

のようになっています．ここで，

```{.sh}
[sonoda@bes-ex01 ~] $ python -m pip install poetry
```

と打って実行すると，ズラーとインストール処理が行われ，最後に

```{.sh}
Successfully installed poetry-1.8.2
[sonoda@bes-ex01 ~] $ □
```

となってインストール終了です．試しに

```{.sh}
[sonoda@bes-ex01 ~] $ poetry help
```

で poetry のヘルプが表示されます．

あとはほぼ上記の自分 PC での操作と同じ(`poetry config`を忘れずに)ですが，

> vscode のときにインタプリタを聞かれたら `.venv/bin/python`を選べ

に対応するインタプリタ設定が必要です．

1. Other/Terminal で Python を起動する場合

   1. まず，

      ```{.sh}
      [sonoda@bes-ex01 k00] $ poetry shell
      ```

      と打つと

      ```{.sh}
      (k00-py3.8) [sonoda@bes-ex01 k00]$
      ```

      のようになるかと思います．

   2. この状況で python を動かせば，自分で入れた site-packages が反映されます．

2. Notebook を使いたい場合

   1. 初めから用意されている`python3`というカーネルには，自分で入れた site-packages が反映されません．よって新たにカーネルを作ります．
   2. Other/Terminal にて

      ```{.sh}
      [sonoda@bes-ex01 k00] $ poetry add ipykernel --group=Dev
      ```

      で カーネル作成パッケージをインストールし，それを使ってカーネルを作ります．カーネル名を指定します．たとえば`k00`なら

      ```{.sh}
      [sonoda@bes-ex01 k00]$ poetry run ipython kernel install --user --name=k00
      ```

   3. Launcher を開くと，Notebook に自分で作ったカーネルが追加されています．そのカーネルで Notebook を作れば，そこでは自分の入れた site-packages が使えます．
   4. ちなみに自分の作ったカーネルのリストは

      ```{.sh}
      [sonoda@bes-ex01 k00] $ jupyter kernelspec list
      ```

   5. ちなみに自分の作ったカーネルを削除するときは，

      ```{.sh}
      [sonoda@bes-ex01 k00] $ jupyter kenelspec uninstall k00
      ```

[JupyterHub@演習室]: https://bes-ex{}.cis.nagasaki-u.ac.jp:8080
[Eteks@演習室]: http://bes-master.cis.nagasaki-u.ac.jp/~matsuo/eteks/
[poetry]: https://python-poetry.org
[mise]: https://mise.jdx.dev/
