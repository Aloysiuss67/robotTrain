
# motorRight =


def adjust_with_error(motor, error):
    motor.forward(0.5 + error)  # value between 0-1
    # motor2.forward(0.5 - error)
