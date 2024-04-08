# day01: 開発環境

プログラミングの一番の基盤は，IDE（開発環境）．IDEとは

1. Code Editor
    - ソースコードを書くソフトウェア
2. Debugger(Linter, Formatter, Tester)
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
- `python -VV`ではなく，`py -VV`です．

#### macの人向けのお話

macの人は，最初からpythonが入っています．

#### （ここは上級者向け）

- システムPython（管理者権限を持つ人しかインストールやアンインストールをできない）
- ユーザーPythonをインストールする or システムPythonをユーザーPythonとしても使う
  - ユーザーPython（ユーザが自由にインストール/アンインストールできる）
  - いろいろ入れて取り散らかりがちなので，管理ソフトで管理（どのPythonを使うかを設定）すると良い．
    - [mise][mise]（MEEZ,ミーズ） がおすすめ
- 新しくモジュールを作るときは，仮想環境Pythonを使う．
  - 仮想環境Python（ユーザーPythonのsite-packagesを使わない）

## 2. vscode

[Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)

Microsoft Windowsには昔々から，Visual StudioというIDE（頭で紹介したエディタ・デバッガ・インタプリタ）すべての入ったソフトウェアがあります[Visual Studio](https://azure.microsoft.com/ja-jp/products/visual-studio/)．ただし，WindowsOS専用です．また，とても大きなソフトウェアであり，手軽に扱えるものではありません．

Visual Studio Code (以下，`vscode`や`code`)は，そのエディタに特化したものとなります．
ただし，拡張機能を多く備えることができ，エディタでありながら，デバッグ，ビルドも可能なものとなっています．さらに，WindowsOSだけでなく，MacOS，LinuxOSでも同じように使用できます．

### 2.1. vscodeの使い方

vscodeはエディタですが，プログラミングに特化したエディタです．

プログラミングでは，あるアプリケーションを作ろうとなった場合に，
「プロジェクト」と呼ぶフォルダを作り，その中にソースコードやらリソースファイル（アイコンや画像や音楽ファイルなど），説明書(Readme)，ライセンス(License)を入れます．

**vscodeでは，ファイルを一つ一つ開くのではなく，この「プロジェクト」のフォルダを開きます．**

フォルダを開いたあと，そのフォルダルート（根っこ）を起点として，その下にあるソースコードを編集したり，ファイルを加えたり削除したりの整理をしたりします．

### 2.2. vscodeの拡張機能

以下の拡張機能をインストールしてください．

[日本語パック拡張機能](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)

[Python用拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 3. poetry

演習ⅠやWeb上のいろんなサイトで，numpyその他のパッケージをインストールする際に`pip`や`conda`を使っているかもしれませんが，この演習Ⅱでは[`poetry`][poetry] を使います．

まず，poetry をインストールしましょう．

> `py -m pip install poetry`

macやlinuxの人は，`python -m pip install poetry`

インストール後に，PATHにpoetryの実行ファイルを加えます．

「虫眼鏡」アイコンから「環境変数」を検索し，「環境変数を編集」からユーザのPathについて「編集」　→　「新規」で下記のpathを追加してください．

```{.sh}
C:\Users\kotaro\AppData\Local\Programs\Python\Python310\Scripts\
```

（上記の `kotaro` はwindowsのサインインアカウント名, `Python310`は`py -V`で表示されるバージョンに合わせてください． 3.10.＊なら`310`）

### 3.1. poetry の使い方

poetryは単なるパッケージインストーラではなく，むしろ「プロジェクト」フォルダのマネージャです．

何はともあれ，最初に次のようにしてください．どのフォルダでもいいです．

```{.sh}
> poetry config virtualenvs.in-project true
> poetry config virtualenvs.options.no-pip true
> poetry config virtualenvs.options.no-setuptools true
```


（上記は，プロジェクトのライブラリ置き場を，プロジェクト内の `.venv` というフォルダに置く，という設定です．この設定をしない場合は，デフォルトで，ユーザの`Virtualenvs`というフォルダの下にプロジェクトごとのenvが置かれます）

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

- 自作モジュール(.py)の中でimportしているパッケージ
- 自作モジュールをimportするテストモジュールが他にimportしているパッケージ

どちらもインストールは，`poetry add` でインストールしてもいいのですが，後者は自作パッケージ配布のときには不要なパッケージです．

なので`poetry add --group=dev`でインストールしておくと，配布物から取り除かれます．

ちなみに，不要になった外部パッケージは，

```{.sh}
> poetry remove 外部パッケージ
```

で削除できます．

#### 4. 自作パッケージの配布

作った自作モジュールを詰め込んだ自作パッケージを配布（提出）したいときは，まず`pyproject.toml`の`[tool.poetry]`の`version`の数値を大きくします．

そのあと，

```{.sh}
> poetry build
```

すると，`dist/kadai01-0.1.0-py3-none-any.whl`みたいのができます．これを配布（提出）します．

## **vscodeでコーディング**

まず，それぞれのプロジェクトで，

```{.sh}
> poetry add ipykernel --group=dev
```

してください．

その後，vscodeでプロジェクトを開き，pythonソースコードを編集します．

インタプリタを聞かれます．このときには，`./.venv/bin/python.exe`を選ぶようにします．
（たいていは，自動的にインタプリタが選ばれます）

[poetry]:https://python-poetry.org
[mise]:https://mise.jdx.dev/
