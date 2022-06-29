#reeborg's world Hurdles & Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def follow_right_wall():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
think(0)
while not at_goal():
    follow_right_wall()

