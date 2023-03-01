from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="GAMBLE YOUR TURTLE COINS", prompt="Which color turtle will win?: ")
colors = ["red", "orange", "yellow", "chartreuse", "blue", "purple"]
is_racing = False
# value=0
ydiv = round(screen.window_height() / len(colors))
newy = -230 + ydiv
all_turts = []

# for color in colors:
#     turt = Turtle(shape="turtle")
#     turt.color(colors[value])
#     turt.pu()
#     turt.goto(x=-240, y=newy)
#     value += 1
#     newy += ydiv

for turtle_index in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.color(colors[turtle_index])
    turt.pu()
    turt.goto(x=-240, y=newy)
    newy += ydiv
    all_turts.append(turt)

if user_bet:
    is_racing = True

while is_racing:
    for turty in all_turts:
        if turty.xcor() > 230:
            is_racing = False
            winner = turty.pencolor()
            if winner == user_bet:
                print(f"You win! {winner} is the winner")
            else:
                print(f"You lose! {winner} is the winner")
        rand_dis = random.randint(0,10)
        turty.fd(rand_dis)


screen.exitonclick()



