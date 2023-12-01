from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
drone.takeoff()

time_elapsed = 0
time_start = time.time()

distance = 150


def fly_drone():
    while time_elapsed < 20:
        time_elapsed = time.time() - time_start
        drone.set_pitch(20)
        drone.move()
        time.sleep(0.01)

        if is_object_detected(150):
            avoid_object()


def is_object_detected(distance):
    if drone.get_front_range("cm") <= distance:
        return True
    else:
        return False


def avoid_object():
    drone.set_pitch(0)
    time.sleep(0.01)

    drone.turn_left()
    left_result = is_object_detected(distance)
    drone.turn_right(180)
    right_result = is_object_detected(distance)

    if (left_result == False and right_result == False) or (left_result == True and right_result == False):
        return True
    elif right_result == True and left_result == False:
        drone.turn_left(180)
        time.sleep(0.01)
        return True
    else:
        drone.turn_right()
        time.sleep(0.01)
        return True

    """
    if (left_result == False and right_result == False) or (left_result == True and right_result == False):
        return True
    elif right_result == True and left_result == False:
        drone.turn_left(180)
        return True
    else:
        drone.turn_right()
        return True
        """


fly_drone()

drone.land()
drone.close()