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