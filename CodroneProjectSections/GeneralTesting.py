from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
drone.takeoff()

time_start = time.time()

drone.set_throttle(30)
drone.move(2)
drone.set_throttle(0)
time.sleep(0.01)



def fly_drone():
    time_elapsed = 0
    while time_elapsed < 20:
        time_elapsed = time.time() - time_start
        drone.set_pitch(40)
        drone.move()
        time.sleep(0.01)

        if is_object_detected(100):
            avoid_object()

        print(drone.get_pos_x("cm"), drone.get_pos_y("cm"), drone.get_pos_z("cm"))


def is_object_detected(distance):
    if drone.get_front_range("cm") <= distance:
        return True
    else:
        return False


def avoid_object():
    drone.set_pitch(0)
    time.sleep(0.01)
    distance = 150

    drone.turn_left()
    left_result = is_object_detected(distance)
    drone.turn_right(180)
    right_result = is_object_detected(distance)

    if (not left_result and not right_result) or (left_result and not right_result):
        return True
    elif right_result and not left_result:
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

