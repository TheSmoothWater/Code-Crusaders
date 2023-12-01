from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
drone.takeoff()

drone.set_throttle(30)
drone.move(2)
drone.set_throttle(0)
drone.hover(1)

time_start = time.time()
time_limit = 60 #seconds
drone_speed = 25

def fly_drone():
    time_elapsed = 0
    while time_elapsed < time_limit:
        time_elapsed = time.time() - time_start
        drone.set_pitch(drone_speed)
        drone.move()
        time.sleep(0.01)

        if is_object_detected(100):
            avoid_object(100)


def is_object_detected(distance):
    if drone.get_front_range("cm") <= distance:
        return True
    else:
        return False


def avoid_object(d_distance):
    drone.set_pitch(0)
    time.sleep(0.01)
    distance = d_distance

    drone.turn_left()
    left_result = is_object_detected(distance)
    drone.turn_right(180)
    right_result = is_object_detected(distance)

    if (left_result is False and right_result is False) or (left_result is True and right_result is False):
        return True
    elif right_result is True and left_result is False:
        drone.turn_left(180)
        time.sleep(0.01)
        return True
    else:
        drone.turn_right()
        time.sleep(0.01)
        return True


fly_drone()

drone.land()
drone.close()
