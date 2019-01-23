from turtle import  *
class Ball(Turtle):
	def __init__(self, x, y ,dx ,dy, color, r):
		Turtle.__init__(self)
		self.penup()
		self.x = self.xcor()
		self.y = self.ycor()
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.goto(x,y)

	def move(self,screen_width, screen_height):
		self.screen_width = screen_width
		self.screen_height = screen_height
		current_x = self.xcor()
		new_x = current_x +  self.dx
		current_y = self.ycor()
		new_y = current_y +  self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r
		self.goto(new_x, new_y)
		if (right_side_ball >= screen_width):
			self.dx = -self.dx

		if (left_side_ball <= -screen_width):
			self.dx = -self.dx

		if (up_side_ball >= screen_height):
			self.dy = -self.dy

		if (bottom_side_ball <= -screen_height):
			self.dy = -self.dy

	def new_Ball(self, x, y ,dx ,dy, color, r):
		self.penup()
		self.x = self.xcor()
		self.y = self.ycor()
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.goto(x,y)

