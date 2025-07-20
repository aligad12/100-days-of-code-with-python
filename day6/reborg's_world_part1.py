def turn_right():  # this is for when the robot is facing you
    turn_left()
    turn_left()
    turn_left()


def turn_around():  # for when the robot is facing the right wall
    turn_left()
    turn_left()


def move_in_square():
    move()
    move()
    turn_left()
    move()
    move()

    move()
    move()
    turn_left()
    move()
    move()


def moveInSquare():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


def jump_hurdles(number_of_hurdles):
    for i in range(number_of_hurdles):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()


def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


jump_hurdles(6)

