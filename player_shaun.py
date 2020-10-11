'''Player Module'''

import turtle
import sprite_list_manager

class PlayerShaun(turtle.Turtle):
    '''Turtle of Player'''
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
        self.go_right_list = []

    def get_go_right_list(self):
        self.go_right_list = sprite_list_manager.load_images_to_list("Resources\\ShaunAnimation\\Shaun_Right")
        pass

    def initialise(self):
        self.get_go_right_list()

    #Define Player Movement
    def go_up(self):
        '''Move Player Turtle up in the game area'''
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\Shaun.gif")
        self.direction="go_up"


    def go_down(self):
        '''Move Player Turtle down in the game area'''
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\Shaun.gif")
        self.direction="go_down"


    def go_left(self):
        '''Move Player Turtle left in the game area'''
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\Left_Facing_Shaun.gif")
        self.direction="go_left"

    def go_right(self):
        '''Move Player Turtle right in the game area'''
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        self.goto(move_to_x,move_to_y)
        self.shape("Resources\\ShaunAnimation\\Shaun_Right\\Shaun_Right_05.gif")
        self.direction="go_right"
