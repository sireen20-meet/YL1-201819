import turtle
import time
from personal_project_ball import *
import random
import math
go = turtle.clone()
#again = turtle.Turtle()
go.hideturtle()

turtle.colormode(1)

turtle.tracer(0)
turtle.hideturtle() 

running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

#turtle.register_shape("again.gif")
#again.shape("again.gif")
number_of_balls = 4

my_ball = Ball(0, 0,3, 1, "blue", 70)


number_of_balls = 3
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5


BALLS = []

for i in range (number_of_balls) :
	x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	r = random.randint(minimum_ball_radius, maximum_ball_radius)
	color = (random.random(), random.random(), random.random())

	new_balls = Ball(x, y, dx, dy, color, r)
	BALLS.append(new_balls)

def move_all_balls():
	for b in BALLS:
		b.move(screen_width, screen_height)

def collide(ball_a, ball_b):
	if (ball_a == ball_b):
		return False

	distance = math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(), 2) + math.pow(ball_a.ycor() - ball_b.ycor(), 2))
	if ball_a.r + ball_b.r >= distance:
		return True

	else:
		return False


#distance_ab = math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(), 2) + math.pow(ball_a.ycor() - ball_b.ycor(), 2))

def check_all_balls_collision():
	global running
	all_balls = []
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)

	for ball_a in all_balls :
		for ball_b in all_balls :
			if (collide(ball_a, ball_b)):
				r1 = ball_a.r
				r2 = ball_b.r

				x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
				y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
				dx = random.randint(minimum_ball_dx, maximum_ball_dx)
				dy = random.randint(minimum_ball_dy, maximum_ball_dy)
				while (dx == 0 and dy ==0):
					dx = random.randint(minimum_ball_dx, maximum_ball_dx)
					dy = random.randint(minimum_ball_dy, maximum_ball_dy)
				r = random.randint(minimum_ball_radius, maximum_ball_radius)
				color = (random.random(), random.random(), random.random())

				if 	(r1<r2):
					ball_a.new_Ball(x, y, dx, dy, color, r)
					ball_b.r = ball_b.r + 1
					ball_b.shapesize(ball_b.r/ 10)
				else:
					ball_b.new_Ball(x, y, dx, dy, color, r)
					ball_a.r = ball_a.r + 1
					ball_a.shapesize(ball_a.r/ 10)
				if (my_ball == ball_a and r1<r2 or my_ball == ball_b and r1>r2):
					running = False
					go.write( "Game Over!",move=False, align="center", font=("Comic Sans MS", 40, "normal"))



def movearound():
	x=turtle.getcanvas().winfo_pointerx() - screen_width*2

	y = screen_height*1.5 - turtle.getcanvas().winfo_pointery()

	my_ball.goto(x, y)

				
running = True 
while running:
	
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2


	movearound()
	move_all_balls()
	# turtle.update()
	# time.sleep(2)
	check_all_balls_collision()

	time.sleep(.1)

	turtle.update()
	



turtle.mainloop()