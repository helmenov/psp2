# coding:utf-8

# 使うモジュールの指定
# turtleというモジュールを使う
import turtle
#from ColabTurtlePlus import Turtle as turtle

def main()-> None:
    """
    (このmain関数が何をするのかを書く．)
    """
    # 上の"""〜"""は，help(関数名)で表示される．

    #
    turtle.setup(width=300, height=300)

    #
    # kame1, kame2は，turtleモジュールに定義されているTurtle型
    kame1 = turtle.Turtle()
    kame2 = turtle.Turtle()

    #
    kame1.pencolor('red')
    kame2.pencolor('blue')

    #
    kame1.penup()
    kame1.goto(50,50)

    kame2.penup()
    kame2.goto(-50,50)

    kame1.pendown()
    kame2.pendown()

    #
    kame1.left(60)
    kame2.left(120)

    #
    kame1.forward(100)
    kame2.backward(200)

    #
    turtle.exitonclick()

if __name__ == '__main__':
    main()
