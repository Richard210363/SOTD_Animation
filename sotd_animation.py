'''Application entry module'''

import turtle

import player_shaun

QUIT_GAME=False

#spritelistmanager = sprite_list_manager.SpriteListManager()
player = player_shaun.PlayerShaun()
player.initialise()


#Define the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shaun of the Dead")
wn.setup(700,700)

def quit_game():
    '''Stop the application'''
    global QUIT_GAME
    QUIT_GAME = True


#Listen to keyboard input
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,'d')
turtle.onkey(player.go_up,'w')
turtle.onkey(player.go_down,'s')
#turtle.onkey(self.fire_bullet,'f')
turtle.onkey(quit_game,'q')

#main loop
while not QUIT_GAME:
    wn.update()

wn.bye()