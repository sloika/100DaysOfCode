# reeborg's world Hurdles & Maze

def turn_right():
    # noinspection PyUnresolvedReferences
    turn_left()
    # noinspection PyUnresolvedReferences
    turn_left()
    # noinspection PyUnresolvedReferences
    turn_left()


def follow_right_wall():
    # noinspection PyUnresolvedReferences
    if right_is_clear():
        turn_right()
        # noinspection PyUnresolvedReferences
        move()
    elif front_is_clear():
        # noinspection PyUnresolvedReferences
        move()
    else:
        # noinspection PyUnresolvedReferences
        turn_left()


# noinspection PyUnresolvedReferences
think(0)
# noinspection PyUnresolvedReferences
while not at_goal():
    follow_right_wall()
