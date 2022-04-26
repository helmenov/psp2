# d03

## N匹のカメを発生させて，各カメを半径1００の円周を等分した点に移動させる

3匹などと少数で，かつ何匹か決まっている場合は，繰り返し処理をおこなわず，

```{.py}
import turtle

kame1 = turtle.Turtle()
kame1.shape('turtle')
kame1.left(0)
kame1.forward(100)

kame2 = turtle.Turtle()
kame2.shape('turtle')
kame2.left(120)
kame2.forward(100)

kame3 = turtle.Turtle()
kame3.shape('turtle')
kame3.left(240)
kame3.forward(100)

turtle.exitonclick()
```

...でもいいかもしれない．つまりkame1,kame2,kame3を命名して，各カメを動かす．

しかし，N匹などと一般性をもたせるとき，繰り返し処理が必要となり，
そのときは，角度をNを用いて求めたり，さらにはカメの名前をN匹分つくる必要がある．


```{.py}
import turtle

N = 5
R = 100
kame = [0] * N
for i in range(N):
    kame[i] = turtle.Turtle()
    kame[i].shape('turtle')
    kame[i].left(i*360/N)
    kame[i].forward(R)
turtle.exitonclick()
```

関数にする

```{.py}
import turtle

def kamefunc(N,R):
    kame = [0] * N
    for i in range(N):
        kame[i] = turtle.Turtle()
        kame[i].shape('turtle')
        kame[i].left(i*360/N)
        kame[i].forward(R)

N = 5
R = 100
kamefunc(N,R)
turtle.exitonclick()
```

## k00(4)の例外処理課題　

すいません，課題が不備でした．n=２以下でもエラーやワーニングは起きません．

よって，(4)はキャンセルします．

もし最終期限(5/11)までに余力がある人は，次のように読み替えてください．

> (4改)`k00_pentagon.py`を`k00_invalid.py`にコピーし，描く線の色名を指定して正五角形を描け．`pencolor('yellow')`で黄色に，`pencolor('blue')`で青色の線を指定できる．ただし，適当な文字列を色名とするとエラーが出てプログラムが止まるであろう．適当な色名が指定されたときには`pencolor('black')`で線を黒色に指定しなおすように，例外処理を加えよ．

例外処理の加え方

例えば，`shape('turtle')`はペンの形を「カメ」にするメソッドだが，`shape('kame')`ではNGで，その関数部分でエラーが起き，その後の処理が行われない．次のソースコードを動かしてみよ．

```{.py}
# coding:utf-8

# %%
# 使うモジュールの指定
# turtleというモジュールを使う
import turtle

# %%
SHAPE = 'turtle'
COLOR = 'blue'

# %%
kame = turtle.Turtle()

# %%
SHAPE = 'kame' #'turtle'なら問題ない

# %%
kame.shape(SHAPE)

# %%
kame.pencolor(COLOR)

# %%
kame.penup()
kame.goto(50,50)

kame.pendown()

# %%
kame.left(60)

# %%
kame.forward(100)

# %%
turtle.exitonclick()

# %%
```

```{.sh}
(.venv) kotaro@calvados d03 % ARM❯ python sample_invalid.py
Traceback (most recent call last):
  File "/Users/kotaro/MyRepository/2022psp2/d03/sample_invalid.py", line 19, in <module>
    kame.shape(SHAPE)
  File "/Users/kotaro/.pyenv/versions/3.10.0/lib/python3.10/turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named kame
```

エラーの内容は，`Traceback`と`〜Error`にあらわれる．`〜Error`はエラーの識別名であり，`Traceback`はそのエラーが発生した箇所である．
すなわち，上の場合は，
> `sample_invalid.py`の19行目 `kame.shape(SHAPE)`でエラーが発生し，`tutle.py`の2777行目がエラーを報告した
と読む．エラー識別名は，`turtle.TurtleGraphicsError`である．

そこで，このエラーを捕まえて(catch)して，例外処理を加える．

```{.py}
try:
    エラーが起きるかもしれない処理
except エラー識別名:
    エラーが起きる場合の代用処理
```

例外処理を加えたソースコードは次のようになる．

```{.py}
# coding:utf-8

# %%
# 使うモジュールの指定
# turtleというモジュールを使う
import turtle

# %%
SHAPE = 'turtle'
COLOR = 'blue'

# %%
kame = turtle.Turtle()

# %%
SHAPE = 'kame' #'turtle'なら問題ない

# %%
try:
    kame.shape(SHAPE)
except turtle.TurtleGraphicsError:
    kame.shape('turtle')


# %%
kame.pencolor(COLOR)

# %%
kame.penup()
kame.goto(50,50)

kame.pendown()

# %%
kame.left(60)

# %%
kame.forward(100)

# %%
turtle.exitonclick()
```
