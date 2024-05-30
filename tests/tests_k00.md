# 提出されたパッケージをインストール

パッケージの wheel の名前を書いて，コメントアウトを外してください．

```python
# !pip install k00-***.whl
```

## (1)

> `k00_turtle.py` のそれぞれの行で行われていることを調べて，ソースコードにそれぞれの行で行われていることをコメントアウトに追記せよ．

```python
# importするだけで動きます．
from k00 import k00_turtle
```

ソースコードを読みます．

```python
!more ~/.local/lib/python3.8/site-packages/k00/k00_turtle.py
```

## (2)

> 正六角形を描画するモジュール`k00_hexagon.py`を作成せよ．ただし，左半分は矢印で赤，右半分はカメで青で描くこと．`for文`もしくは`while文`などの繰り返し処理を用いること．自分で編集したソースコードのそれぞれの行で行われていることをコメントアウトに追加せよ．

```python
# import するだけで動きます．
from k00 import k00_hexagon
```

ソースコードを読みます．

```python
!more ~/.local/lib/python3.8/site-packages/k00/k00_hexagon.py
```

## (3)

> `k00_pentagon.py`に正 N 角形を描画する関数`NsidePolygon(n)`を作成し，`NsidePolygon`関数を利用して正五角形を描け．ただし，関数`NsidePolygon(n)`は`n`匹のカメを発生させ，それぞれのカメがそれぞれ各頂点に移動して一つの辺のみを描画することとする．繰り返し処理を利用してできるだけ行数を短くせよ．

```python
# importするだけで動くかも
from k00 import k00_pentagon

```

```python
# 関数定義がきちんとされているかチェック
n = 5

k00_pentagon.NsidePolygon(n=n)
```

ソースコードを読む

```python
!more ~/.local/lib/python3.8/site-packages/k00/k00_pentagon.py
```

## (4)

> (4)`k00_pentagon.py`を`k00_invalid.py`にコピーし，`NsidePolygon`関数に描く線の色名を引数`color`として指定してできるようにせよ．その上で正五角形を描け．`pencolor('yellow')`で黄色に，`pencolor('blue')`で青色の線を指定できる．ただし，適当な文字列を色名とするとエラーが出てプログラムが止まるであろう．適当な色名が指定されたときには`pencolor('black')`で線を黒色に指定しなおすように，例外処理を加えよ．

```python
# import するだけで動くかも
from k00 import k00_invalid

```

```python
# 関数定義されていれば，こちらも動く
n = 5

```

```python

color = 'blue'

k00_invalid.NsidePolygon(n=n, color=color)

```

```python
color = 'pink'
k00_invalid.NsidePolygon(n=n, color=color)
```

ソースコードを読む

```python
!more ~/.local/lib/python3.8/site-packages/k00/k00_invalid.py
```

## (5)

> パッケージ`k00`の下にさらにディレクトリ`k00funcs`を作り，その下に`k00_func.py`を作成せよ．(4)の関数`NsidePolygon`関数を`k00_func.py`に書き，`k00_octagon.py`で`from k00.k00funcs import k00_func`として読み込んだ上で，`k00_func.NsidePolygon`関数を利用して，正八角形を描け．

```python
# import するだけで動くはず．
from k00 import k00_octagon
```

ソースコードのチェック

```python
!more ~/.local/lib/python3.8/site-packages/k00/k00_octagon.py
```

```python
!more ~/.local/lib/python3.8/site-packages/k00/k00funcs/k00_func.py
```

# 最後に提出パッケージをアンインストール

```python
!pip uninstall k00
```
