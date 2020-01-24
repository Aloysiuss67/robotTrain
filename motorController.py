def adjust_left(motor, error, debug_mode):
    if debug_mode:
        print("Left motor speed = " + repr(0.5 + error))
    motor.forward(0.5 + error)  # value between 0-1


def adjust_right(motor, error, debug_mode):
    if debug_mode:
        print("Right motor speed = " + repr(0.5 - error))
    motor.forward(0.5 - error)  # value between 0-1
