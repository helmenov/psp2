



```python
import pandas as pd

# アジア語の文字幅をきれいに表示するおまじない
pd.set_option('display.unicode.east_asian_width', True) 
```


```python
df = pd.read_csv('mydata1.csv',skipinitialspace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th># mydata1.csv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>名前</th>
      <th>性別</th>
      <th>好きな数</th>
      <th>誕生月</th>
      <th>セロリ好き度</th>
      <td>身長</td>
    </tr>
    <tr>
      <th>薗田</th>
      <th>男</th>
      <th>7</th>
      <th>5</th>
      <th>とても嫌い</th>
      <td>172</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <th>女</th>
      <th>3</th>
      <th>12</th>
      <th>好き</th>
      <td>165</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <th>男</th>
      <th>4</th>
      <th>10</th>
      <th>嫌い</th>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



`skip-initial-space`はアジア語で余計な空白が入るのを防ぐので，いつもつけておくとよい．


```python
type(df)
```




    pandas.core.frame.DataFrame



`df`は`DataFrame`というクラスに割当てられています．

```{.py}
class DataFrame():
    def __str__(self):
```

のように`__str__`メソッドがあるので，文字列にすることができ，


```python
df.__str__()
```




    '                                       # mydata1.csv\n名前 性別 好きな数 誕生月 セロリ好き度          身長\n薗田 男   7        5      とても嫌い             172\n鈴木 女   3        12     好き                   165\n斎藤 男   4        10     嫌い                   180'



文字列を表示すれば


```python
print(df.__str__())
```

                                           # mydata1.csv
    名前 性別 好きな数 誕生月 セロリ好き度          身長
    薗田 男   7        5      とても嫌い             172
    鈴木 女   3        12     好き                   165
    斎藤 男   4        10     嫌い                   180


のように表示されます．jupyterだともっときれいに出力できて


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th># mydata1.csv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>名前</th>
      <th>性別</th>
      <th>好きな数</th>
      <th>誕生月</th>
      <th>セロリ好き度</th>
      <td>身長</td>
    </tr>
    <tr>
      <th>薗田</th>
      <th>男</th>
      <th>7</th>
      <th>5</th>
      <th>とても嫌い</th>
      <td>172</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <th>女</th>
      <th>3</th>
      <th>12</th>
      <th>好き</th>
      <td>165</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <th>男</th>
      <th>4</th>
      <th>10</th>
      <th>嫌い</th>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



```{.py}
class DataFrame():
    def __init__(self, ...):
        self.shape = ...
```

のようなクラス変数`shape`があり，データフレームの行数（観測数）と列数（変数数）をタプルで表示します．


```python
print(df.shape)
```

    (4, 1)


4つの観測，1つの変数となりました．

あれれ，それは違います．今回のデータは3観測(薗田と鈴木と斎藤)，6変数（名前,..., 身長）のはずなので`(3,6)`であるはずです．

ファイルを直接見ると，1行目に`# mydata1.csv`とあり，これはメモですね．読み飛ばす行番号をリストにして`skiprows`オプションに渡します．



```python
df = pd.read_csv('mydata1.csv',skipinitialspace=True, skiprows=[0])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名前</th>
      <th>性別</th>
      <th>好きな数</th>
      <th>誕生月</th>
      <th>セロリ好き度</th>
      <th>身長</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>薗田</td>
      <td>男</td>
      <td>7</td>
      <td>5</td>
      <td>とても嫌い</td>
      <td>172</td>
    </tr>
    <tr>
      <th>1</th>
      <td>鈴木</td>
      <td>女</td>
      <td>3</td>
      <td>12</td>
      <td>好き</td>
      <td>165</td>
    </tr>
    <tr>
      <th>2</th>
      <td>斎藤</td>
      <td>男</td>
      <td>4</td>
      <td>10</td>
      <td>嫌い</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (3, 6)



きちんと，3観測6変数になりました．ちなみに読み飛ばした後の最初の行をヘッダ(header)，変数名リストとして読みます．
クラス変数columnsに変数名が保存されています．

ちなみに，ヘッダ行は観測ではないので，(4,6)ではなく(3,6)になっています．


```python
df.columns
```




    Index(['名前', '性別', '好きな数', '誕生月', 'セロリ好き度', '身長'], dtype='object')



変数名が並んだ行が無いCSVもあります．例えば`mydata2.csv`は`mydata1.csv`と同じ3観測6変数のデータですが，


```python
df = pd.read_csv('mydata2.csv',skipinitialspace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>薗田</th>
      <th>男</th>
      <th>7</th>
      <th>5</th>
      <th>とても嫌い</th>
      <th>172</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>鈴木</td>
      <td>女</td>
      <td>3</td>
      <td>12</td>
      <td>好き</td>
      <td>165</td>
    </tr>
    <tr>
      <th>1</th>
      <td>斎藤</td>
      <td>男</td>
      <td>4</td>
      <td>10</td>
      <td>嫌い</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (2, 6)



のように，データの1観測目がヘッダと捉えられてしまいます．よって，
`header`が無いことを教えて read_csv　します．


```python
df = pd.read_csv('mydata2.csv',skipinitialspace=True,header=None)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>薗田</td>
      <td>男</td>
      <td>7</td>
      <td>5</td>
      <td>とても嫌い</td>
      <td>172</td>
    </tr>
    <tr>
      <th>1</th>
      <td>鈴木</td>
      <td>女</td>
      <td>3</td>
      <td>12</td>
      <td>好き</td>
      <td>165</td>
    </tr>
    <tr>
      <th>2</th>
      <td>斎藤</td>
      <td>男</td>
      <td>4</td>
      <td>10</td>
      <td>嫌い</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



ただし，ヘッダが無いので変数名が仮に0,....,5となっています．



```python
df.columns
```




    Int64Index([0, 1, 2, 3, 4, 5], dtype='int64')



きちんと変数名を決めるには
このクラス変数`columns`を正しいもので上書きします．


```python
df.columns=['Name','Sex','FavoriteNumber','BirthMonth','CeleryFavor','Height']
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>FavoriteNumber</th>
      <th>BirthMonth</th>
      <th>CeleryFavor</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>薗田</td>
      <td>男</td>
      <td>7</td>
      <td>5</td>
      <td>とても嫌い</td>
      <td>172</td>
    </tr>
    <tr>
      <th>1</th>
      <td>鈴木</td>
      <td>女</td>
      <td>3</td>
      <td>12</td>
      <td>好き</td>
      <td>165</td>
    </tr>
    <tr>
      <th>2</th>
      <td>斎藤</td>
      <td>男</td>
      <td>4</td>
      <td>10</td>
      <td>嫌い</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



変数名を変えるにはrenameメソッドを使ってもよいです．


```python
df.rename(columns={'Sex':'Gender'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Gender</th>
      <th>FavoriteNumber</th>
      <th>BirthMonth</th>
      <th>CeleryFavor</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>薗田</td>
      <td>男</td>
      <td>7</td>
      <td>5</td>
      <td>とても嫌い</td>
      <td>172</td>
    </tr>
    <tr>
      <th>1</th>
      <td>鈴木</td>
      <td>女</td>
      <td>3</td>
      <td>12</td>
      <td>好き</td>
      <td>165</td>
    </tr>
    <tr>
      <th>2</th>
      <td>斎藤</td>
      <td>男</td>
      <td>4</td>
      <td>10</td>
      <td>嫌い</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



ところで，データフレームを表示したときに，左端に毎回0から始まる数字が書かれています．
これは，CSVにおける観測の個体IDであり，「インデックス(index)」と読んでいます．データ本体には含まれません．


```python
print(df.index)
```

    RangeIndex(start=0, stop=3, step=1)


indexは0から始まって，1ずつ増えて，3の前までということみたいですね．

### データを集めたら

そんなこんなで，`mydata1.csv`を読みます．


```python
df = pd.read_csv('mydata1.csv',skipinitialspace=True,header=1)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名前</th>
      <th>性別</th>
      <th>好きな数</th>
      <th>誕生月</th>
      <th>セロリ好き度</th>
      <th>身長</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>薗田</td>
      <td>男</td>
      <td>7</td>
      <td>5</td>
      <td>とても嫌い</td>
      <td>172</td>
    </tr>
    <tr>
      <th>1</th>
      <td>鈴木</td>
      <td>女</td>
      <td>3</td>
      <td>12</td>
      <td>好き</td>
      <td>165</td>
    </tr>
    <tr>
      <th>2</th>
      <td>斎藤</td>
      <td>男</td>
      <td>4</td>
      <td>10</td>
      <td>嫌い</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



同じデータですが，場合によっては，次のような表でまとめているかもしれません．


```python
df2 = pd.read_csv('mydata3.csv',skipinitialspace=True,skiprows=[0])
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名前</th>
      <th>変数名</th>
      <th>回答</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>薗田</td>
      <td>性別</td>
      <td>男</td>
    </tr>
    <tr>
      <th>1</th>
      <td>薗田</td>
      <td>好きな数</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>薗田</td>
      <td>誕生月</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>薗田</td>
      <td>セロリ好き度</td>
      <td>とても嫌い</td>
    </tr>
    <tr>
      <th>4</th>
      <td>薗田</td>
      <td>身長</td>
      <td>172</td>
    </tr>
    <tr>
      <th>5</th>
      <td>鈴木</td>
      <td>性別</td>
      <td>女</td>
    </tr>
    <tr>
      <th>6</th>
      <td>鈴木</td>
      <td>好きな数</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>鈴木</td>
      <td>誕生月</td>
      <td>12</td>
    </tr>
    <tr>
      <th>8</th>
      <td>鈴木</td>
      <td>セロリ好き度</td>
      <td>好き</td>
    </tr>
    <tr>
      <th>9</th>
      <td>鈴木</td>
      <td>身長</td>
      <td>165</td>
    </tr>
    <tr>
      <th>10</th>
      <td>斎藤</td>
      <td>性別</td>
      <td>男</td>
    </tr>
    <tr>
      <th>11</th>
      <td>斎藤</td>
      <td>好きな数</td>
      <td>4</td>
    </tr>
    <tr>
      <th>12</th>
      <td>斎藤</td>
      <td>誕生月</td>
      <td>10</td>
    </tr>
    <tr>
      <th>13</th>
      <td>斎藤</td>
      <td>セロリ好き度</td>
      <td>嫌い</td>
    </tr>
    <tr>
      <th>14</th>
      <td>斎藤</td>
      <td>身長</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



この場合，「名前」が同じ行は，1人に対する別々の変数と回答を表しています．つまり，回答者は「薗田」「鈴木」「斎藤」の3人です．よって，回答者をIDとします．


```python
df2 = df2.set_index('名前')
df2

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>変数名</th>
      <th>回答</th>
    </tr>
    <tr>
      <th>名前</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>薗田</th>
      <td>性別</td>
      <td>男</td>
    </tr>
    <tr>
      <th>薗田</th>
      <td>好きな数</td>
      <td>7</td>
    </tr>
    <tr>
      <th>薗田</th>
      <td>誕生月</td>
      <td>5</td>
    </tr>
    <tr>
      <th>薗田</th>
      <td>セロリ好き度</td>
      <td>とても嫌い</td>
    </tr>
    <tr>
      <th>薗田</th>
      <td>身長</td>
      <td>172</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>性別</td>
      <td>女</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>好きな数</td>
      <td>3</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>誕生月</td>
      <td>12</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>セロリ好き度</td>
      <td>好き</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>身長</td>
      <td>165</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <td>性別</td>
      <td>男</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <td>好きな数</td>
      <td>4</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <td>誕生月</td>
      <td>10</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <td>セロリ好き度</td>
      <td>嫌い</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <td>身長</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



このような縦長の表を先程のようなデータフレームに変換するには，pivot関数を使います．変数名が並ぶ列と，回答が並ぶ列を指定すると，変換できます．


```python
df3 = pd.pivot(df2,columns='変数名',values='回答')
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>変数名</th>
      <th>セロリ好き度</th>
      <th>好きな数</th>
      <th>性別</th>
      <th>誕生月</th>
      <th>身長</th>
    </tr>
    <tr>
      <th>名前</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>斎藤</th>
      <td>嫌い</td>
      <td>4</td>
      <td>男</td>
      <td>10</td>
      <td>180</td>
    </tr>
    <tr>
      <th>薗田</th>
      <td>とても嫌い</td>
      <td>7</td>
      <td>男</td>
      <td>5</td>
      <td>172</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>好き</td>
      <td>3</td>
      <td>女</td>
      <td>12</td>
      <td>165</td>
    </tr>
  </tbody>
</table>
</div>




#### データフレーム上の値は以下のように参照できます．

- 変数「好きな数」だけを全サンプル参照してみます．

1. df[[変数名]]


```python
col1 = df3[['好きな数']]
col1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>変数名</th>
      <th>好きな数</th>
    </tr>
    <tr>
      <th>名前</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>斎藤</th>
      <td>4</td>
    </tr>
    <tr>
      <th>薗田</th>
      <td>7</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(type(col1), col1.shape)
```

    <class 'pandas.core.frame.DataFrame'> (3, 1)


2. df.変数名


```python
col2 = df3.好きな数
col2
```




    名前
    斎藤    4
    薗田    7
    鈴木    3
    Name: 好きな数, dtype: object




```python
print(type(col2), col2.shape)
```

    <class 'pandas.core.series.Series'> (3,)


3. df[変数名]


```python
col3 = df3['好きな数']
col3
```




    名前
    斎藤    4
    薗田    7
    鈴木    3
    Name: 好きな数, dtype: object




```python
print(type(col3),col3.shape)
```

    <class 'pandas.core.series.Series'> (3,)


4. df[[変数名]][範囲]


```python
col4 = df3[['好きな数']][1:3] #　スライスで行番号
col4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>変数名</th>
      <th>好きな数</th>
    </tr>
    <tr>
      <th>名前</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>薗田</th>
      <td>7</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(type(col4),col4.shape)
```

    <class 'pandas.core.frame.DataFrame'> (2, 1)


5. df.loc[範囲,変数名]


```python
col5 = df.loc[:1, '好きな数'] # 行スライスが`:1`に注意
col5
```




    0    7
    1    3
    Name: 好きな数, dtype: int64




```python
print(type(col5), col5.shape)
```

    <class 'pandas.core.series.Series'> (2,)


6. df.iloc[行範囲，列範囲]


```python
col6 = df3.iloc[:2, 1] # 変数の順番で指定
col6
```




    名前
    斎藤    4
    薗田    7
    Name: 好きな数, dtype: object



以上から，
- `df[['var']]` : DataFrame 2階テンソル（行列）
- `df['var']` : Series 1階テンソル（ベクトル）
- `df.var` : Series 1階テンソル（ベクトル）

- `df[['var']][:2]` : DataFrame
- `df.loc[:1, 'var']` : Series
- `df.iloc[:2, 2]` : Series 


### データの要約

データの要約は describeメソッドで行います．


```python
df.describe(include='all')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名前</th>
      <th>性別</th>
      <th>好きな数</th>
      <th>誕生月</th>
      <th>セロリ好き度</th>
      <th>身長</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3</td>
      <td>3</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>3</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>薗田</td>
      <td>男</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>とても嫌い</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.666667</td>
      <td>9.000000</td>
      <td>NaN</td>
      <td>172.333333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.081666</td>
      <td>3.605551</td>
      <td>NaN</td>
      <td>7.505553</td>
    </tr>
    <tr>
      <th>min</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.000000</td>
      <td>5.000000</td>
      <td>NaN</td>
      <td>165.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.500000</td>
      <td>7.500000</td>
      <td>NaN</td>
      <td>168.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.000000</td>
      <td>10.000000</td>
      <td>NaN</td>
      <td>172.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.500000</td>
      <td>11.000000</td>
      <td>NaN</td>
      <td>176.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.000000</td>
      <td>12.000000</td>
      <td>NaN</td>
      <td>180.000000</td>
    </tr>
  </tbody>
</table>
</div>



全て，各項目ごとの代表値で，

- `count`はデータの個数(sample size，サンプルサイズ)
- `unique`は*データに現れた*水準の個数 (**本当の水準数ではない**)
- `top`はデータの最頻値，`freq`は最頻値の頻度
- `mean`は平均値，`std`は標準偏差(STandard Deviation)
- `min`は最小値，`max`は最大値，
- `25%`, `50%`, `75%`は四分位で，ヒストグラムを低い水準から並べたときに下位25％，50％，75％にあたる水準を答えるものです．下位50％はmedian（メディアン，メジアン）とも呼ばれます．
- `NaN` は *Not a Number* 値なし

この関数の中身は，以下のDataFrameのメソッドを使っても表示されます．


```python
# 各変数のサンプルサイズ
df.count()
```




    名前            3
    性別            3
    好きな数        3
    誕生月          3
    セロリ好き度    3
    身長            3
    dtype: int64




```python
# 各変数の標本平均
df.mean()
```

    /var/folders/99/qkvnxd5x1zv5v058py9fckk80000gn/T/ipykernel_29916/2071310889.py:2: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      df.mean()





    好きな数      4.666667
    誕生月        9.000000
    身長        172.333333
    dtype: float64




```python
# 各変数の標本中央値
df.median()
```

    /var/folders/99/qkvnxd5x1zv5v058py9fckk80000gn/T/ipykernel_29916/3673436120.py:2: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      df.median()





    好きな数      4.0
    誕生月       10.0
    身長        172.0
    dtype: float64




```python
# 各変数の標本標準偏差
df.std()
```

    /var/folders/99/qkvnxd5x1zv5v058py9fckk80000gn/T/ipykernel_29916/3194488187.py:2: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      df.std()





    好きな数    2.081666
    誕生月      3.605551
    身長        7.505553
    dtype: float64




```python
# 第1四分位
df.quantile(q=0.25)
```




    好きな数      3.5
    誕生月        7.5
    身長        168.5
    Name: 0.25, dtype: float64




```python
# 第2四分位（中央値）
df.quantile(q=0.5)
```




    好きな数      4.0
    誕生月       10.0
    身長        172.0
    Name: 0.5, dtype: float64




```python
# 第3四分位
df.quantile(q=0.75)
```




    好きな数      5.5
    誕生月       11.0
    身長        176.0
    Name: 0.75, dtype: float64



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


```python
df['名前']
```




    0    薗田
    1    鈴木
    2    斎藤
    Name: 名前, dtype: object




```python
df['名前'] = pd.Categorical(df['名前'])
df['名前']
```




    0    薗田
    1    鈴木
    2    斎藤
    Name: 名前, dtype: category
    Categories (3, object): ['斎藤', '薗田', '鈴木']



- 「性別」


```python
df['性別']
```




    0    男
    1    女
    2    男
    Name: 性別, dtype: object




```python
GenderSet = {'男','女'}
df['性別'] = pd.Categorical(df['性別'], categories=GenderSet, ordered=False)
df['性別']
```




    0    男
    1    女
    2    男
    Name: 性別, dtype: category
    Categories (2, object): ['男', '女']



- 「好きな数」，「誕生月」


```python
df['好きな数']
```




    0    7
    1    3
    2    4
    Name: 好きな数, dtype: int64




```python
df['好きな数'] = df['好きな数'].astype('str') 
df['好きな数']
```




    0    7
    1    3
    2    4
    Name: 好きな数, dtype: object




```python
# MonthSet = {'1','2','3','4','5','6','7','8','9','10','11','12'} でもいいですが
MonthSet = set([str(n) for n in range(1,13)])
df['好きな数'] = pd.Categorical(df['好きな数'], categories=MonthSet, ordered=False)

df['好きな数']
```




    0    7
    1    3
    2    4
    Name: 好きな数, dtype: category
    Categories (12, object): ['1', '3', '9', '4', ..., '11', '10', '7', '8']




```python
df['誕生月'] = df['誕生月'].astype('str') 
df['誕生月'] = pd.Categorical(df['誕生月'], categories=MonthSet, ordered=False)
```

- 「セロリ好き度」

セロリ好き度は，強弱・大小があるので，順序尺度です．


```python
df['セロリ好き度']
```




    0    とても嫌い
    1          好き
    2          嫌い
    Name: セロリ好き度, dtype: object




```python
CerelyFavorLevel = ['とても嫌い','嫌い','ふつう','好き','とても好き']
df['セロリ好き度'] = pd.Categorical(df['セロリ好き度'],categories=CerelyFavorLevel,ordered=True)
df['セロリ好き度']
```




    0    とても嫌い
    1          好き
    2          嫌い
    Name: セロリ好き度, dtype: category
    Categories (5, object): ['とても嫌い' < '嫌い' < 'ふつう' < '好き' < 'とても好き']



変数が文字列のものは，数字と対応付けすることができます．

性別に対して，

- 男: -1
- 女: +1

に対応付けしたいならば，まず対応を記した辞書を作り，それをマッピングします．

マッピングしたのちも，尺度は変わらず名義尺度(Categorical, ordered=False)となっています．

数字だからといって大小をつけられるわけではありません．


```python
SexMap = {'男':-1, '女':+1}
df['性別'] = df['性別'].map(SexMap)
df['性別']
```




    0   -1
    1    1
    2   -1
    Name: 性別, dtype: category
    Categories (2, int64): [-1, 1]



同様に，「セロリ好き度」も数字にしましょうか．

とても嫌い(-2) - 嫌い(-1) - ふつう(0) - 好き(+1) - とても好き(+2)


```python
CerelyFavorMap = {'とても嫌い':-2, '嫌い':-1, 'ふつう':0, '好き':+1, 'とても好き':+2}
df['セロリ好き度'] = df['セロリ好き度'].map(CerelyFavorMap)
df['セロリ好き度'] 
```




    0   -2
    1    1
    2   -1
    Name: セロリ好き度, dtype: category
    Categories (5, int64): [-2 < -1 < 0 < 1 < 2]




```python
df['セロリ好き度'].median()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [53], in <cell line: 1>()
    ----> 1 df['セロリ好き度'].median()


    File ~/Dropbox/My Mac (sliwowica.local)/Documents/MyRepository/2022psp2/.venv/lib/python3.10/site-packages/pandas/core/generic.py:11187, in NDFrame._add_numeric_operations.<locals>.median(self, axis, skipna, level, numeric_only, **kwargs)
      11169 @doc(
      11170     _num_doc,
      11171     desc="Return the median of the values over the requested axis.",
       (...)
      11185     **kwargs,
      11186 ):
    > 11187     return NDFrame.median(self, axis, skipna, level, numeric_only, **kwargs)


    File ~/Dropbox/My Mac (sliwowica.local)/Documents/MyRepository/2022psp2/.venv/lib/python3.10/site-packages/pandas/core/generic.py:10699, in NDFrame.median(self, axis, skipna, level, numeric_only, **kwargs)
      10691 def median(
      10692     self,
      10693     axis: Axis | None | lib.NoDefault = lib.no_default,
       (...)
      10697     **kwargs,
      10698 ) -> Series | float:
    > 10699     return self._stat_function(
      10700         "median", nanops.nanmedian, axis, skipna, level, numeric_only, **kwargs
      10701     )


    File ~/Dropbox/My Mac (sliwowica.local)/Documents/MyRepository/2022psp2/.venv/lib/python3.10/site-packages/pandas/core/generic.py:10639, in NDFrame._stat_function(self, name, func, axis, skipna, level, numeric_only, **kwargs)
      10629     warnings.warn(
      10630         "Using the level keyword in DataFrame and Series aggregations is "
      10631         "deprecated and will be removed in a future version. Use groupby "
       (...)
      10634         stacklevel=find_stack_level(),
      10635     )
      10636     return self._agg_by_level(
      10637         name, axis=axis, level=level, skipna=skipna, numeric_only=numeric_only
      10638     )
    > 10639 return self._reduce(
      10640     func, name=name, axis=axis, skipna=skipna, numeric_only=numeric_only
      10641 )


    File ~/Dropbox/My Mac (sliwowica.local)/Documents/MyRepository/2022psp2/.venv/lib/python3.10/site-packages/pandas/core/series.py:4459, in Series._reduce(self, op, name, axis, skipna, numeric_only, filter_type, **kwds)
       4455     self._get_axis_number(axis)
       4457 if isinstance(delegate, ExtensionArray):
       4458     # dispatch to ExtensionArray interface
    -> 4459     return delegate._reduce(name, skipna=skipna, **kwds)
       4461 else:
       4462     # dispatch to numpy arrays
       4463     if numeric_only:


    File ~/Dropbox/My Mac (sliwowica.local)/Documents/MyRepository/2022psp2/.venv/lib/python3.10/site-packages/pandas/core/arrays/base.py:1369, in ExtensionArray._reduce(self, name, skipna, **kwargs)
       1367 meth = getattr(self, name, None)
       1368 if meth is None:
    -> 1369     raise TypeError(
       1370         f"'{type(self).__name__}' with dtype {self.dtype} "
       1371         f"does not support reduction '{name}'"
       1372     )
       1373 return meth(skipna=skipna, **kwargs)


    TypeError: 'Categorical' with dtype category does not support reduction 'median'


セロリ好き度の5段階は，等間隔ですので，数字にしたからには間隔尺度になってほしいですが，そうなっていません．
間隔尺度にしてあげましょう．


```python
df['セロリ好き度'] = df['セロリ好き度'].cat.codes
df['セロリ好き度']

```




    0    0
    1    3
    2    1
    Name: セロリ好き度, dtype: int8




```python
df['セロリ好き度'] = df['セロリ好き度']-2
df['セロリ好き度']
```




    0   -2
    1    1
    2   -1
    Name: セロリ好き度, dtype: int8




```python
df['セロリ好き度'].median()
```




    -1.0



今回のデータでは，名前は単に各データのID（データを見分けるための符号）でしかありません．set_indexでIDとなる列を指定します．


```python
df = df.set_index('名前')
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>性別</th>
      <th>好きな数</th>
      <th>誕生月</th>
      <th>セロリ好き度</th>
      <th>身長</th>
    </tr>
    <tr>
      <th>名前</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>薗田</th>
      <td>-1</td>
      <td>7</td>
      <td>5</td>
      <td>-2</td>
      <td>172</td>
    </tr>
    <tr>
      <th>鈴木</th>
      <td>1</td>
      <td>3</td>
      <td>12</td>
      <td>1</td>
      <td>165</td>
    </tr>
    <tr>
      <th>斎藤</th>
      <td>-1</td>
      <td>4</td>
      <td>10</td>
      <td>-1</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>



本当は数値なのにCategoricalや文字列に認識されてしまっている列が合った場合や
本当は整数なのに，小数点付きに認識されてしまっている列については，

```
df['列名'].astype(float) # 列の値をすべてfloat型に
```

のような　astype(float) や astype(int)　などで型キャストができる


```python

```

要約


```python
df.describe(include='all')

```

ある変数をグループ分けして，グループごとに要約することもできます．


```python
df.groupby(['性別']).describe(include='all')
```

クロス集計表を作ることもできます．クロスさせる2つの変数名を引数に並べます．


```python
pd.crosstab(df['性別'],df['好きな数'])
```

## 課題k02



[これ](heights14.csv)は，身近の14人（男7人，女7人）に性別と身長を尋ねたときの回答を集めた標本データである．

(1) pandasパッケージを用いて，データフレームを作成し，
この標本集団における男性と女性それぞれの平均と標準偏差を求めよ．

(2) このデータはある特定の14人のデータなので，別な14人で回答を集めるたびに別の標本平均が求まる．
適当な男7人，女7人で回答を集めたときにその標本平均が収まる範囲「◯±△」を推定せよ．
これはすなわち，男性全体，女性全体の母集団平均が収まる範囲に等しい．

(3) 男性全体，女性全体の母集団の標準偏差を求めよ．

母集団の分散$u^2$は標本の分散$s^2$と標本サイズ$N$から「推定」できる．所謂，不偏分散と呼ばれる．
$$ u^2 = \frac{N}{N-1}s^2 $$

母集団の平均の最良推定値（「◯±△」の「◯」）は，標本平均と等しい．また，標本誤差（「◯±△」の「△」）は，$\sqrt{\frac{u^2}{N}}$で求まる．

提出するファイル`k02.py`は，
```
python k02.py　
```
を実行すると，同じ階層にある`heights14.csv`を読み込み，

```
==男==
標本平均:173.90
標本標準偏差: 5.06
母集団平均:173.90± 1.91
母集団標準偏差: 5.41

--女--
標本平均: ◯ cm
標本標準偏差：　◯ cm
母集団平均範囲： ◯ ± △ cm
母集団標準偏差：　◯ cm
```

と表示されるようにせよ．（男について表示される数値は上記になるのが正解）


 
 







