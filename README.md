# 長崎大学　情報データ科学部　 2 年次　プログラミング演習 Ⅱ

## お品書き

- [1 日目](d01) Python 開発環境
- [2 日目](d02) Turtle Graphics による Python Programing の基礎演習
- [3 日目](d03) 〃（補足）例外処理
- [4 日目](d04) クラス：　自作の型（有理数），自作型における組み込みメソッドのオーバーライド
- [5 日目](d05) dataframe, 表計算パッケージ `Pandas`
- [6〜8 日目](d06) 〃
- [9〜12 日目](d09) 数値計算パッケージ `NumPy`, グラフ描画パッケージ `matplotlib`
- [13 日目](d13) 色当てゲーム支援プログラム

## 演習の進め方

[GitHub 上の演習ページ][psp2@github] にある課題に対して，

- レポート（実行画面のスクリーンショットを含む） word(.docx)でも pdf(.pdf)でもよい
- ソースパッケージ (.whl)

の 2 点を[LACS の課題ページ][psp2@LACS]に提出する．院生 TA と薗田が採点し，10 点満点未満であれば再提出対象となる．何度でも再提出可能．

- 初めての提出は，課題が提示されてから 2 週間後の正午までとする．
- この期限を過ぎたあとには，原則的に再提出以外は受け付けない．
- この期限までに提出物があった場合，この課題に関わる授業日を「出席」として扱う．逆に何の提出物も無かった場合に「欠席」として扱う．授業日に実際に在席していたかどうかは問わない．
- 最終期限は，原則的には課題が提示されてから 4 週間後の正午までとする．
- この期限を過ぎたあとには，原則的にはあらゆる提出を受け付けない．

提出は，演習の時間以外でも受け付ける．

### 教室

<!--
- 多目的ホール（DSコース）
- ２０９講義室（ISコース）
-->

- 多目的ホール

### レポートの書き方

```{.sh}
aa83988848 薗田光太郎

1. 課題
1.1 ......を出力するプログラムを作成せよ．
1.2 ......を出力するプログラムを作成せよ

2. プログラム実行例

- 課題小問ごとに，プログラム実行例のスクリーンショット画像を貼る
- どんな入力を行ったのか，を明確に

```

### ソースパッケージ（または提出する wheel）の作り方

#### パッケージとは

演習 Ⅱ では， *部品となるソースファイル「モジュール」*をコーディングし， _実行のためのソースファイル_ （なかで必要なモジュールを `import`する）はこちらで指定します．

_実行のためのソース・ファイル_ は，提出の必要がありません．モジュールのみを提出してもらいます．

一般的にモジュールは，それが梱包されたディレクトリ「パッケージ」で，人々に配布されています．（numpy, pandas, matplotlib, ...etc.）

#### パッケージの配布

ディレクトリを配布する際は，皆さんよく知っているように， `zip` などの圧縮ファイルが使われます．python のパッケージは `wheel` （拡張子は `.whl`） というもので配布されます．

```{.sh}
> pip install numpy
```

とコマンドを打ってパッケージをインストールすると思いますが， このコマンドは，インターネット上にある PyPI というサイトにある `numpy_***.whl` というものをダウンロードして，適切な場所に解凍されたディレクトリを配置するものです．

そこで， **演習 Ⅱ でも，この「パッケージ配布」で，パッケージ提出してもらいます．**

ただし，PyPI というサイトで全世界に公開するのではなく，LACS で wheel を提出してもらいます．

#### wheel の作り方

パッケージはモジュールを梱包したディレクトリですが，他人がこのモジュールを `import` して使うには，前もってインストールしておかなければならない別のパッケージがあります．

たとえば，あなたの作ったモジュールの中で， `import numpy` して NumPy の関数を使っているのであれば，そのモジュールを使う側ではあらかじめ `pip install numpy` していなければいけません．

したがって，パッケージ配布のときには，「あらかじめインストールしていなければいけないパッケージのリスト」を定型文で書いたファイル( `PKG-INFO` )も wheel に同封します． `PKG-INFO` は，必要なパッケージのリスト以外にも，様々な情報を書かなければいけません．

実際は面倒なので，wheel を作るためのツールを使うことが多いです．演習 Ⅱ では，  を使います．

poetry は

- ディレクトリを作る， `poetry new`
- モジュールを動かすためのパッケージをインストールする `poetry add`
- wheel を作る `poetry build`

のすべてを行えます．（PyPI へのアップロードもできるが今回はしない）

poetry の詳細は，初日のページ[d01](d01)で

ともかく，教員側では，提出された wheel を `pip install *.whl` し， 先の _実行のためのソースファイル_ を動かします．別に提出された実行結果スクリーンショットと合致し，課題を解けていればよいです．

### Teaching Assistants (TA)

演習当日のプログラミング相談，環境構築のヘルプ，提出物の採点をしてくれるのは，学生ティーチング・アシスタントである．

- 大学院工学研究科情報工学コースの 1 年生（いわゆる「M1」）を 8 人

他に，技術職員が参加してくれる．

### プログラミング相談

私のメールアドレスは，

> [kotaro@nagasaki-u.ac.jp](mailto:kotaro@nagasaki-u.ac.jp?subject='プログラミング演習Ⅱ')

です．LACS の「メッセージ（E メール）」からもメールできます．

メールなどでは伝わりにくい部分もあるので，対面での相談も受け付けます．その場合もあらかじめメールでアポイントをとってください．

## シラバス

[シラバス][psp2@NuWEB]

[psp2@LACS]: https://lacs.nagasaki-u.ac.jp/webapps/blackboard/content/launchLink.jsp?course_id=_56014_1&toc_id=_1089844_1&mode=cpview&mode=reset
[psp2@NuWEB]: https://nuweb.nagasaki-u.ac.jp/campusweb/campussquare.do?_flowId=SYW3201400-flow&jikanwaricd=20243802005501&locale=ja_JP
[psp2@github]: https://github.com/helmenov/psp2
[poetry]: https://python-poetry.org/
