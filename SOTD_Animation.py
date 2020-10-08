import turtle

quit=False

#Define the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shaun of the Dead")
wn.setup(700,700)

def quit_game():
    global quit
    quit = True


#Listen to keyboard input
turtle.listen()
#turtle.onkey(self.player.go_left,"a")
#turtle.onkey(self.player.go_right,'d')
#turtle.onkey(self.player.go_up,'w')
#turtle.onkey(self.player.go_down,'s')
#turtle.onkey(self.fire_bullet,'f')
turtle.onkey(quit_game,'q')


#main loop
while not quit:
    wn.update()

wn.bye()
