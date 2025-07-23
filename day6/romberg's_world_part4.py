def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    counter = 0
    while wall_on_right():
        counter += 1
        move()
    turn_right()
    move()
    turn_right()
    for count in range(counter + 1):
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()