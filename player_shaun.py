import turtle

class PlayerShaun(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        turtle.register_shape("Resources\\ShaunAnimation\\Shaun_Start.gif")




        self.x_cor=0
        self.y_cor=0
        self.shape("Resources\\ShaunAnimation\\Shaun_Start.gif")
        self.penup()
        self.speed(0)
        self.direction="go_down"
        self.goto(self.x_cor,self.y_cor)


    #Define Player Movement
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\Shaun.gif")
        self.direction="go_up"


    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\Shaun.gif")
        self.direction="go_down"


    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\Left_Facing_Shaun.gif")
        self.direction="go_left"

    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\Right_Facing_Shaun.gif")
        self.direction="go_right"



