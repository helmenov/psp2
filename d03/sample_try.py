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
except turtle.TurtleGraphicsError as e: # 変数`e`にはエラーの説明文が代入される．
    print(f'例外処理：{e}, turtleに変えます') # `f`をつけると，`{変数}`の部分を変数に入っている値が文字列に直されます．
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