'''Player Module'''

import turtle
import sprite_list_manager
import constant

class PlayerShaun(turtle.Turtle):
    '''Turtle of Player'''
    def __init__(self):
        turtle.Turtle.__init__(self)

        turtle.register_shape(constant.shaun_animation_start)

        self.x_cor=0
        self.y_cor=0
        self.shape(constant.shaun_animation_start)
        self.penup()
        self.speed(0)
        self.direction="go_down"
        self.goto(self.x_cor,self.y_cor)
        self.go_right_list = []
        self.go_left_list = []
        self.go_up_list = []
        self.go_down_list = []
        self.current_frame = 0

    def get_go_right_list(self):
        '''Preparing list for animation'''
        self.go_right_list = sprite_list_manager.load_images(constant.shaun_animation_right)

    def get_go_left_list(self):
        '''Preparing list for animation'''
        self.go_left_list = sprite_list_manager.load_images(constant.shaun_animation_left)

    def get_go_up_list(self):
        '''Preparing list for animation'''
        self.go_up_list = sprite_list_manager.load_images(constant.shaun_animation_up)

    def get_go_down_list(self):
        '''Preparing list for animation'''
        self.go_down_list = sprite_list_manager.load_images(constant.shaun_animation_down)

    def initialise(self):
        '''Prepares player for use'''
        self.get_go_right_list()
        self.get_go_left_list()
        self.get_go_up_list()
        self.get_go_down_list()

    #Define Player Movement
    def go_up(self):
        '''Move Player Turtle up in the game area'''
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        self.goto(move_to_x,move_to_y)
        filename = self.go_up_list[self.current_frame]
        if self.current_frame == len(self.go_up_list) - 1:
            self.current_frame = 0
        else:
            self.current_frame = self.current_frame + 1
        self.shape(constant.shaun_animation_up + "\\" + filename)
        self.direction="go_up"


    def go_down(self):
        '''Move Player Turtle down in the game area'''
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        self.goto(move_to_x,move_to_y)
        filename = self.go_down_list[self.current_frame]
        if self.current_frame == len(self.go_down_list) - 1:
            self.current_frame = 0
        else:
            self.current_frame = self.current_frame + 1
        self.shape(constant.shaun_animation_down + "\\" + filename)
        self.direction="go_down"


    def go_left(self):
        '''Move Player Turtle left in the game area'''
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.goto(move_to_x,move_to_y)
        filename = self.go_left_list[self.current_frame]
        if self.current_frame == len(self.go_left_list) - 1:
            self.current_frame = 0
        else:
            self.current_frame = self.current_frame + 1
        self.shape(constant.shaun_animation_left + "\\" + filename)
        self.direction="go_left"

    def go_right(self):
        '''Move Player Turtle right in the game area'''
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        self.goto(move_to_x,move_to_y)
        filename = self.go_right_list[self.current_frame]
        if self.current_frame == len(self.go_right_list) - 1:
            self.current_frame = 0
        else:
            self.current_frame = self.current_frame + 1
        self.shape(constant.shaun_animation_right + "\\" + filename)
        self.direction="go_right"