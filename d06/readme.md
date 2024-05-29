---
jupyter: python3
---
<!-- TOC -->

- [まず，](#%E3%81%BE%E3%81%9A)
    - [vscode で jupyter](#vscode-%E3%81%A7-jupyter)
- [Pandas](#pandas)
    - [標本の追加](#%E6%A8%99%E6%9C%AC%E3%81%AE%E8%BF%BD%E5%8A%A0)
    - [標本セットの読み込み](#%E6%A8%99%E6%9C%AC%E3%82%BB%E3%83%83%E3%83%88%E3%81%AE%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF)
    - [データを集めたら](#%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E9%9B%86%E3%82%81%E3%81%9F%E3%82%89)
    - [データフレーム上の値は以下のように参照できます．](#%E3%83%87%E3%83%BC%E3%82%BF%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E4%B8%8A%E3%81%AE%E5%80%A4%E3%81%AF%E4%BB%A5%E4%B8%8B%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E5%8F%82%E7%85%A7%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%EF%BC%8E)
    - [データの要約](#%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E8%A6%81%E7%B4%84)
    - [変数の尺度を正しく設定](#%E5%A4%89%E6%95%B0%E3%81%AE%E5%B0%BA%E5%BA%A6%E3%82%92%E6%AD%A3%E3%81%97%E3%81%8F%E8%A8%AD%E5%AE%9A)
- [課題k02](#%E8%AA%B2%E9%A1%8Ck02)

<!-- /TOC -->

## 0. まず，

`cmd`で

```{.sh}
> poetry new k02
> cd k02
> poetry env use py
> poetry install --sync
> poetry add ipykernel
```

により，いつものように，パッケージ開発用フォルダを作り，
その下に，仮想環境(`.venv`)，配布するフォルダ(`k02`)などを作る．

今回は，パッケージの中で，外部パッケージを使いたいので，

```{.sh}
> poetry add pandas
> poetry add openpyxl
> poetry add matplotlib
> poetry add numpy
```

というように，

- Pandas
- OpenPyXL
- MatplotLib
- NumPy

の4つの外部パッケージを仮想環境にインストールしておきます．

### 0.1. vscode で jupyter

vscodeで配布用フォルダ `k02` の下に，`k02_1.ipynb` という名前のファイルを作り，開きます．

## 1. Pandas

### 1.1 標本の追加

最初のセルに，

```{python}
import pandas as pd

# アジア語の文字幅をきれいに表示するおまじない
pd.set_option('display.unicode.east_asian_width', True)
```

と書いて，実行します．

次に，データフレームを作ります．データフレームには変数（項目名）が必要です．

```{python}
df = pd.DataFrame(columns=['名前','性別','好きな数','誕生月','セロリ好き度','身長'])
```

dfを表示するには，普通は`print(df)`としますが，jupyterでは，`display(df)`とすると，きれいに表示されます．

```{python}
display(df)
```

今はデータがありませんので，項目名のみが表示されます．

では，データを入れていきましょう．

というか，データが1つでもデータフレームです．

```{python}
sample_0 = {
    '名前':'鈴木', '性別':'女', '好きな数':3,
    '誕生月':12, 'セロリ好き度':'好き', '身長':165
    } # dictで作ります．
df_0 = pd.DataFrame(data=[sample_0])
display(df_0)
```

別の標本は，

```{python}
sample_1 = {
    '名前':'薗田', '性別':'男', '好きな数':7,
    '誕生月':5, 'セロリ好き度':'とても嫌い', '身長':172
    }
df_1 = pd.DataFrame(data=[sample_1])
display(df_1)
```

これら2つのデータフレームを合成して，新たなデータフレーム `df` を作ります．

```{python}
df = pd.concat([df_0, df_1], ignore_index=True, axis=1)
display(df)
```

`axis=1` は，合成の方向です．標本を追加するので縦方向に合成です．縦方向は`axis=1`です．（列方向，項目を追加する場合は，`axis=0`）

### 1.2. 標本セットの読み込み

CSVファイルの読み込みは，`read_csv`関数です．

```{python}
df = pd.read_csv('mydata1.csv',skipinitialspace=True)
display(df)
```

`skip-initial-space`はアジア語で余計な空白が入るのを防ぐので，いつもつけておくとよい．

```{python}
type(df)
```

`df`は`DataFrame`というクラスに割当てられていることがわかります．

`df.shape` データフレームの行数（観測数）と列数（変数数）をタプルで表示します．

```{python}
print(df.shape)
```

4つの観測，1つの変数となりました．

あれれ，それは違います．今回のデータは3観測(薗田と鈴木と斎藤)，6変数（名前,..., 身長）のはずなので`(3,6)`であるはずです．

ファイルを直接見ると，1行目に`# mydata1.csv`とあり，これはメモですね．読み飛ばす行番号をリストにして`skiprows`オプションに渡します．

```{python}
df = pd.read_csv('mydata1.csv',skipinitialspace=True, skiprows=[0])
df
```

```{python}
df.shape
```

きちんと，3観測6変数になりました．ちなみに読み飛ばした後の最初の行をヘッダ(header)，変数名リストとして読みます．
クラス変数columnsに変数名が保存されています．

ちなみに，ヘッダ行は観測ではないので，(4,6)ではなく(3,6)になっています．

```{python}
df.columns
```

変数名が並んだ行が無いCSVもあります．例えば`mydata2.csv`は`mydata1.csv`と同じ3観測6変数のデータですが，

```{python}
df = pd.read_csv('mydata2.csv',skipinitialspace=True)
df
```

```{python}
df.shape
```

のように，データの1観測目がヘッダと捉えられてしまいます．よって，
`header`が無いことを教えて read_csv　します．

```{python}
df = pd.read_csv('mydata2.csv',skipinitialspace=True,header=None)
df
```

ただし，ヘッダが無いので変数名が仮に0,....,5となっています．

```{python}
df.columns
```

きちんと変数名を決めるには
このクラス変数`columns`を正しいもので上書きします．

```{python}
df.columns=['Name','Sex','FavoriteNumber','BirthMonth','CeleryFavor','Height']
df
```

変数名を変えるにはrenameメソッドを使ってもよいです．

```{python}
df.rename(columns={'Sex':'Gender'})
```

ところで，データフレームを表示したときに，左端に毎回0から始まる数字が書かれています．
これは，CSVにおける観測の個体IDであり，「インデックス(index)」と読んでいます．データ本体には含まれません．

```{python}
print(df.index)
```

indexは0から始まって，1ずつ増えて，3の前までということみたいですね．

### 1.3. データを集めたら

そんなこんなで，`mydata1.csv`を読みます．

```{python}
df = pd.read_csv('mydata1.csv',skipinitialspace=True,header=1)
df
```

同じデータですが，場合によっては，次のような表でまとめているかもしれません．

```{python}
df2 = pd.read_csv('mydata3.csv',skipinitialspace=True,skiprows=[0])
df2
```

この場合，「名前」が同じ行は，1人に対する別々の変数と回答を表しています．つまり，回答者は「薗田」「鈴木」「斎藤」の3人です．よって，回答者をIDとします．

```{python}
df2 = df2.set_index('名前')
df2
```

このような縦長の表を先程のようなデータフレームに変換するには，pivot関数を使います．変数名が並ぶ列と，回答が並ぶ列を指定すると，変換できます．

```{python}
df3 = pd.pivot(df2,columns='変数名',values='回答')
df3
```


### 1.4. データフレーム上の値は以下のように参照できます．

- 変数「好きな数」だけを全サンプル参照してみます．

1. df[[変数名]]

```{python}
col1 = df3[['好きな数']]
col1
```

```{python}
print(type(col1), col1.shape)
```

2. df.変数名

```{python}
col2 = df3.好きな数
col2
```

```{python}
print(type(col2), col2.shape)
```

3. df[変数名]

```{python}
col3 = df3['好きな数']
col3
```

```{python}
print(type(col3),col3.shape)
```

4. df[[変数名]][範囲]

```{python}
col4 = df3[['好きな数']][1:3] #　スライスで行番号
col4
```

```{python}
print(type(col4),col4.shape)
```

5. df.loc[範囲,変数名]

```{python}
col5 = df.loc[:1, '好きな数'] # 行スライスが`:1`に注意
col5
```

```{python}
print(type(col5), col5.shape)
```

6. df.iloc[行範囲，列範囲]

```{python}
col6 = df3.iloc[:2, 1] # 変数の順番で指定
col6
```

以上から，
- `df[['var']]` : DataFrame 2階テンソル（行列）
- `df['var']` : Series 1階テンソル（ベクトル）
- `df.var` : Series 1階テンソル（ベクトル）

- `df[['var']][:2]` : DataFrame
- `df.loc[:1, 'var']` : Series
- `df.iloc[:2, 2]` : Series

### 1.5. データの要約

データの要約は describeメソッドで行います．

```{python}
df.describe(include='all')
```

全て，各項目ごとの代表値で，

- `count`はデータの個数(sample size，サンプルサイズ)
- `unique`は*データに現れた*水準の個数 (**本当の水準数ではない**)
- `top`はデータの最頻値，`freq`は最頻値の頻度
- `mean`は平均値，`std`は標準偏差(STandard Deviation)
- `min`は最小値，`max`は最大値，
- `25%`, `50%`, `75%`は四分位で，ヒストグラムを低い水準から並べたときに下位25％，50％，75％にあたる水準を答えるものです．下位50％はmedian（メディアン，メジアン）とも呼ばれます．
- `NaN` は *Not a Number* 値なし

この関数の中身は，以下のDataFrameのメソッドを使っても表示されます．

```{python}
# 各変数のサンプルサイズ
df['身長'].count()
```

```{python}
# 各変数の標本平均
df['身長'].mean()
```

```{python}
# 各変数の標本中央値
df['身長'].median()
```

```{python}
# 各変数の標本標準偏差
df['身長'].std(ddof=0)
```

```{python}
# 第1四分位
df['身長'].quantile(q=0.25)
```

```{python}
# 第2四分位（中央値）
df['身長'].quantile(q=0.5)
```

```{python}
# 第3四分位
df['身長'].quantile(q=0.75)
```

### 1.6. 変数の尺度を正しく設定

ところで，身長は平均や標準偏差に意味がありますが，「好きな数」や「誕生月」にとっての平均や標準偏差は意味不明ですね．

「好きな数」や「誕生月」って，いわば「性別」と同じように，どれが最初でどれが最後だとか無いですね．

ということで，各変数は，尺度（スケール，scale）というものがあります．

|尺度名|特徴|計算可能|
|---|---|---|
|名義尺度(nominal)|分類のための単なる文字・数字| `==`, `!=`, `is`, `not`|
|順序尺度(ordered)|順序関係のある文字・数字| `>`, `<`|
|間隔尺度(interval)|MKS単位系でない測定値| `+`,`-`|
|比尺度(ratio)| MKS単位系の測定値 | `*`,`/`|

間隔尺度と比尺度は見分けにくいが，MKS単位系（メートル，キログラム，秒）を基本単位とする測定値は原器に対する比で表されるので比尺度，それ以外の単位系（または単位無し）の測定値は間隔尺度と考えられる．

では，`mydata1.csv`の各変数の尺度は何でしょうか.

また，各変数は，とりうる値のリスト（「水準」といいます）がすでに決められています．各変数の具体的な水準はどうなっているでしょうか

|変数名|尺度|水準|
|---|---|---|
|名前|名義尺度|あらゆる人名|
|性別|名義尺度|集合{'男','女'}|
|好きな数|名義尺度|集合{'1','2','3','4','5','6','7','8','9','10','11','12'}|
|誕生月|名義尺度|集合{'1','2','3','4','5','6','7','8','9','10','11','12'}|
|セロリ好き度|順序尺度|リスト['とても嫌い'，'嫌い'，'普通'，'好き'，'とても好き']|
|身長|比尺度|あらゆる実数|


Pandasでは，それぞれの尺度に型（クラス）を割り当てています．
- 名義尺度は，`Categorical(categories=[...],ordered=False)`クラス
- 順序尺度は，`Categorical(categories=[...],ordered=True)`クラス
- 間隔尺度と比尺度は，`Float`クラス

というわけで，そのように直します．

[公式サイトの`class pandas.Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html)

- 「名前」

```{python}
df['名前']
```

```{python}
df['名前'] = pd.Categorical(df['名前'])
df['名前']
```

- 「性別」

```{python}
df['性別']
```

```{python}
GenderSet = {'男','女'}
df['性別'] = pd.Categorical(df['性別'], categories=GenderSet, ordered=False)
df['性別']
```

- 「好きな数」，「誕生月」

```{python}
df['好きな数']
```

```{python}
df['好きな数'] = df['好きな数'].astype('str')
df['好きな数']
```

```{python}
# MonthSet = {'1','2','3','4','5','6','7','8','9','10','11','12'} でもいいですが
MonthSet = set([str(n) for n in range(1,13)])
df['好きな数'] = pd.Categorical(df['好きな数'], categories=MonthSet, ordered=False)

df['好きな数']
```

```{python}
df['誕生月'] = df['誕生月'].astype('str')
df['誕生月'] = pd.Categorical(df['誕生月'], categories=MonthSet, ordered=False)
```

- 「セロリ好き度」

セロリ好き度は，強弱・大小があるので，順序尺度です．

```{python}
df['セロリ好き度']
```

```{python}
CerelyFavorLevel = ['とても嫌い','嫌い','ふつう','好き','とても好き']
df['セロリ好き度'] = pd.Categorical(df['セロリ好き度'],categories=CerelyFavorLevel,ordered=True)
df['セロリ好き度']
```

変数が文字列のものは，数字と対応付けすることができます．

性別に対して，

- 男: -1
- 女: +1

に対応付けしたいならば，まず対応を記した辞書を作り，それをマッピングします．

マッピングしたのちも，尺度は変わらず名義尺度(Categorical, ordered=False)となっています．

数字だからといって大小をつけられるわけではありません．

```{python}
SexMap = {'男':-1, '女':+1}
df['性別'] = df['性別'].map(SexMap)
df['性別']
```

同様に，「セロリ好き度」も数字にしましょうか．

とても嫌い(-2) - 嫌い(-1) - ふつう(0) - 好き(+1) - とても好き(+2)

```{python}
CerelyFavorMap = {'とても嫌い':-2, '嫌い':-1, 'ふつう':0, '好き':+1, 'とても好き':+2}
df['セロリ好き度'] = df['セロリ好き度'].map(CerelyFavorMap)
df['セロリ好き度']
```

```{python}
#df['セロリ好き度'].median()
```

セロリ好き度の5段階は，等間隔ですので，数字にしたからには間隔尺度になってほしいですが，そうなっていません．
間隔尺度にしてあげましょう．

```{python}
df['セロリ好き度'] = df['セロリ好き度'].cat.codes
df['セロリ好き度']
```

```{python}
df['セロリ好き度'] = df['セロリ好き度']-2
df['セロリ好き度']
```

```{python}
df['セロリ好き度'].median()
```

今回のデータでは，名前は単に各データのID（データを見分けるための符号）でしかありません．set_indexでIDとなる列を指定します．

```{python}
df = df.set_index('名前')
```

```{python}
df
```

本当は数値なのにCategoricalや文字列に認識されてしまっている列が合った場合や
本当は整数なのに，小数点付きに認識されてしまっている列については，

```
df['列名'].astype(float) # 列の値をすべてfloat型に
```

のような　astype(float) や astype(int)　などで型キャストができる


要約

```{python}
df.describe(include='all')
```

ある変数をグループ分けして，グループごとに要約することもできます．

```{python}
df.groupby(['性別']).describe(include='all')
```

クロス集計表を作ることもできます．クロスさせる2つの変数名を引数に並べます．

```{python}
pd.crosstab(df['性別'],df['好きな数'])
```

## 課題k02

[これ](heights14.csv)は，身近の14人（男7人，女7人）に性別と身長を尋ねたときの回答を集めた標本データである．

(1) pandasパッケージを用いて，csvファイルを読み込んでデータフレームを作成し，
この標本集団における男性と女性それぞれの「平均」と「標準偏差」を表示する関数を `k02_1.py` の中で `main()` として定義せよ．

開発手順は，

0. `k02/k02_1.ipynb` を作り，Jupyter形式で，入力セルと出力セルを確認しながらプログラミング
1. `k02/k02_1.ipynb` を `k02/k02_1.py` にエクスポートする．入力セルのみが .py にコピーされる．
    - jupyter形式ではないため `display()` は使えないので消す．
    - `poetry run python k02/k02_1.py`で確認．
2. `k02_1.py` をモジュールに書き換える．
    - import行のあとのすべての処理を `def main():` ブロックに入れる．
    - `k02_1.py` の末尾に，`if __name__ == '__main__': main()` という行を追加
3. 動作確認用に`tests/test_k02_1.py`を書いて，正しく動作することを確認

    ```{.py}
    from k02 import k02_1

    k02_1.main()
    ```

`k02_1.py`を以下のように，`def main()` に処理，`if __name__ == '__main__': main()` を末尾に設定，とすると，

```{.py'}
import pandas as pd

def main():
    # ここに処理を書く（インデントに気をつけよ）

if __name__ == '__main__': main()
```

```{.sh}
> poetry run python k02/k02_1.py
```

は，

```{.sh}
> poetry run python
>>> from k02 import k02_1
>>> k02_1.main()
```

実行結果は

```{.sh}
==男==
平均:173.90
標準偏差: 5.06

--女--
平均: ◯ cm
標準偏差：　◯ cm
```

と表示されるようにせよ．（男について表示される数値は上記になるのが正解）

ちなみに，標本分散は `var(ddof=0)`，標本標準偏差は， `std(ddof=0)` で計算される．（いくつかのサイトで誤っていることを確認しているので，注意すること）

```{.sh}
df_M = df[df['性別']=='男']
se_M_height = df_M['身長']
M_std = se_M_height.std(ddof=0) # 標準偏差
M_var = se_M_height.var(ddof=0) # 分散
```

(2) このデータはある特定の14人のデータなので，別な14人で回答を集めるたびに別の標本平均が求まる．
適当な男7人，女7人で回答を集めたときにその標本平均が収まる範囲「◯±△」を推定せよ．
`(1)`と同様に最終的には モジュール`k02/k02_2.py`を作り，`tests/test_k02_2.py`で動作確認せよ．

- 母集団の平均の最良推定値（「◯±△」の「◯」）は，標本平均と等しい．
- また，標本誤差（「◯±△」の「△」）は， $\sqrt{\frac{u^2}{N}}$ で求まる．
  - 母集団の分散 $u^2$ は標本の分散 $s^2$ と標本サイズ $N$ から「推定」できる．所謂，不偏分散と呼ばれる．

$$
u^2 = \frac{N}{N-1}s^2
$$

ちなみに，母集団の分散と標準偏差は，`var(ddof=1)`，`std(ddof=1)`で計算される．（いくつかのサイトで誤っていることを確認しているので，注意すること）

実行結果は，

```{.sh}
==男==
母集団平均:173.90± 1.91

--女--
母集団平均範囲： ◯ ± △ cm
```

と表示されるようにせよ．（男について表示される数値は上記になるのが正解）

(3) 男性全体，女性全体の母集団の標準偏差を求めよ．モジュール名は，`k02/k02_3.py`とする．
母集団の標準偏差は，(2)の母集団分散の二乗根である．

実行結果は，

```{.sh}
==男==
母集団標準偏差: 5.41

--女--
母集団標準偏差：　◯ cm
```

と表示されるようにせよ．（男について表示される数値は上記になるのが正解）
