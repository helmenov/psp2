# editor

vscode

# python

## pythonは1人いればよい（python開発環境事始め）

プログラミングの一番の基盤は，IDE（開発環境）である．IDEとは

1. Code Editor
    - ソースコードを書くソフトウェア
2. Debugger(Linter, Fromatter, Tester)
    - ソースコードのバグを発見するソフトウェア
3. Interpreter(Compiler,Builder)
    - ソースコードを実行するソフトウェア
の3種のソフトウェアである．

では，皆さん，自分が現在使っているIDEソフトウェアが何かは知っているでしょうが，それがどこにあるか把握していますか？

例えば，コードエディタである`emacs`，どこにありますか．

windowsでもmac/Linuxでも`where`コマンドで調べることができます．

```
$ where emacs
```

複数表示された人は，そのソフトウェアが複数インストールされていることを意味しています．また，最初の行のものが実際に使われているソフトウェアで，2行目以降は「パス付きでないと実行されない」ものです．基本的には同名のソフトウェアは1個で十分です．複数あった場合，トラブルのもとになるので消したほうが身のためです．

さて，インタプリタである`python`が，どこにあるか`where python`で試してみてください．

複数表示された人は，どれか1つを使うことにして，他のものは消しましょう．

## じゃぁ，どのPythonを使おうか？

Pythonがユーザに配られるパターンは大きく下の3パターンです．おそらく`where python`で3つ表示された場合，それぞれが以下のものです．

1. Microsoft Store（Windows）や，HomeBrew(Mac)や，Apt/Yum(Linux)など，OSのパッケージ管理ソフトでインストール
2. Anaconda/Minicondaでインストール
3. Python公式ページから直接にインストーラーをダウンロード

最も推奨されるのは**1**です．なぜか？ｰ>OSが直接ソフトウェアを管理しているので，インストールやアンインストールがしやすいからです．でも，安定はしているものの，最新ではありません．また変な使い方もできません．

2のAnaconda/Minicondaは**独自の**Python開発環境を提供しています．というか，とりあえず必要なもの全てをまるごとインストールします．とりあえず始めるのにはいいのですが，くせが強く，抜けるのが困難です．

3は無難です．安定版か開発版かなど自分で選びます．どこに入れるかも自分で選びます．きちんと管理しないとごちゃごちゃします．一番困るのはPATHの設定が必要なことです．

## 残念ですがPythonを全部アンインストール

プログラミング演習2を始めるにあたり，
最初に，python環境を統一したいと思います．

まず，pythonをすべてアンインストールします．
`where python`で見つかるPythonは，環境変数PATHの下にあるpythonです．おそらく，PATHの下にないpythonもあるでしょう．それも削除します．

1. Windowsの設定から，アプリケーションの管理，pythonやanacondaを選んで，アンインストール
2. エクスプローラで，Cドライブに対して`python.exe`を検索して，見つかった場所の「ディレクトリ」を削除

## pyenv（python公式を使うがきちんと管理する．）

### windows版 pyenv 

[pyenv-win](https://github.com/pyenv-win/pyenv-win/releases)

最新のzipをダウンロードして，展開すると
`pyenv-win`というフォルダができる．
そのフォルダを
`％USER%\.pyenv_win`
に移す．
`mv pyenv-win %USER%\.pyenv_win`

ユーザー環境変数のPathの先頭に
`%USER%\.pyenv_win\pyenv-win\bin`
と
`%USER%\.pyenv_win\pyenv-win\shims`
を加える．

この時点で，
`pyenv versions`
を実行できればOK

### Mac, Linux版 pyenv

brewやyumやaptなどのパッケージインストーラで入れることができる

### pythonをインストール

`pyenv install --list`
してみて好みのものを
`pyenv install 3.10.1`
などとしてインストールする．

最後に
`pyenv global 3.10.1`
などとしておく


## poetry

windowsなら
```{pwsh}
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```
をPowerShellで打ち込むことでインストールされる

Mac,Linuxならば，
```
curl -sSL https://install.python-poetry.org | python3 -
```

仮想環境をプロジェクトの下に置くために，
```
poetry config virtualenvs.in-project true
```
を打っておく（なんのことかわからなくとも）

