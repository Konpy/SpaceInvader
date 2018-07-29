#Space Invader Game 

import turtle
import os
import math
import random


#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space.gif")
#Register the Shapes
turtle.register_shape("invader.gif")


#Draw a border

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-250,-250)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()

#Set score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-230,230)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 12, "normal"))
score_pen.hideturtle()


#Choose number of enemies
number_of_enemies = 5
#Create a empty list
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
        #Create enemy turtle 
        enemies.append(turtle.Turtle())
        
for enemy in enemies:       
    enemy.color("blue")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(0,200)
    enemy.setposition(x,y)

enemyspeed = 2

    


#Create player turtle
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-200)
player.setheading(90)

#Player Movement
playerspeed = 10

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -230:
        x = -230
    player.setx(x)
     
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 230:
        x = 230
    player.setx(x)
    
#Player Weapons
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bullet.speed = 15  

#Define bullet state
bulletstate = "ready"  



def fire_bullet():
    #DEclare bulletstate as a global if it needs changed
    global bulletstate
    
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move bullet to player position
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()
        

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")    
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:
    
    
    
    
    for enemy in enemies:
    #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        #Move the enemy back and down
        if enemy.xcor() > 230:
            #Move all enemies down
            for e in enemies:
                y =e.ycor()
                y -= 20
                e.sety(y)
            #Changes enemy direction
            enemyspeed *= -1
            
            
            
        if enemy.xcor() < -230:
            for e in enemies:
                #Move all enemies down
                y = e.ycor()
                y -= 20
                e.sety(y)
            #Changes enemy direction
            enemyspeed *= -1    
            
            #Check if bullet hit a enemy
        if isCollision(bullet,enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #Reset enemy
            x = random.randint(-200,200)
            y = random.randint(0,200)
            enemy.setposition(x,y)
            #Update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font = ("Arial", 12, "normal"))
            
        #Check if playe has been hit
        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break
            
        #Move the Bullet 
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bullet.speed
        bullet.sety(y)
        
        # Check if bullet has hit the border
    if bullet.ycor() > 230:
        bullet.hideturtle()
        bulletstate = "ready"
            
        
    
    
    


#Tell computer that the window is done
turtle.done()