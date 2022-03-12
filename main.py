import time
from turtle import  Screen #se llaman turtle y screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#Creacion del tablero
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake game")
#Quitamos la animacion de turtle
screen.tracer(0)
#INstancia objeto serpiento


game_is_on = True
food = Food()
snake = Snake()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on: 
    #Actualizar nosotros la animación
    screen.update()
    #velocidad de la animación
    time.sleep(0.05)
    snake.move()
    #Colision con comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Colision con pared
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    #Colision segmento serpiente - usar slicespara descartar el if
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()