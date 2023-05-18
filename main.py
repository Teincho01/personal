import turtle as tr
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from ui import UI
from scoreboard import Scoreboard
import time

screen = tr.Screen()
screen.setup = (1200, 600)
screen.bgcolor("black")
screen.title("Breakout")

ui = UI()
ui.header()

score = Scoreboard(lives = 5)
paddle = Paddle()
bricks = Bricks()

ball = Ball()

game_paused = False
playing_game = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True

screen.listen()
screen.onkey(key = "Left", fun = paddle.move_left)
screen.onkey(key = "Right", fun = paddle.move_right)
screen.onkey(key = "space", fun = pause_game)

def check_collision_with_walls():
    if ball.xcor() > 570 or ball.xcor() < -580:
        ball.bounce(x_bounce = True, y_bounce = False)
        return
    if ball.ycor() > 270:
        ball.bounce(x_bounce = False, y_bounce = True)
        return
    if ball.ycor() < -280:
        ball.reset_position()
        return

def check_collision_with_paddle():
    global ball, paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()
    
    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce = True, y_bounce = True)
                return
            else:
                ball.bounce(x_bounce = False, y_bounce = True)
                return

        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce = True, y_bounce = True)
                return
            else:
                ball.bounce(x_bounce = False, y_bounce = True)
                return

        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce = True, y_bounce = True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce = True, y_bounce = True)
                return
            else:
                ball.bounce(x_bounce = False, y_bounce = True)
                return

def check_collision_with_bricks():
    global ball, score, bricks

    for Brick in Brick.bricks:
        if ball.distance(Brick) < 40:
            score.increase_score()
            Brick.quantity -= 1
            if Brick.quantity == 0:
                Brick.clear()
                Brick.goto(3000, 3000)
                Brick.bricks.remove(Brick)
            
            if ball.xcor() < Brick.left_wall:
                ball.bounce(x_bounce = True, y_bounce = False)
                
            elif ball.xcor() > Brick.right_wall:
                ball.bounce(x_bounce = True, y_bounce = False)
            
            elif ball.ycor() > Brick.top_wall:
                ball.bounce(x_bounce = False, y_bounce = True)

            elif ball.ycor() < Brick.bottom_wall:
                ball.bounce(x_bounce = False, y_bounce = True)
            
while playing_game:
    if not game_paused:
        screen.update()
        time.sleep(0.01)
        ball.move()
        check_collision_with_bricks()
        check_collision_with_walls()
        check_collision_with_paddle()
        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break
        else:
            ui.paused_status()

screen.update()
tr.mainloop()