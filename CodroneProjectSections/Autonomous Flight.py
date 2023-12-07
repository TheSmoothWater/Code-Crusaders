#Official and Final Code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
drone.set_initial_pressure()
pressure = 70

time_start = time.time()
#Should be battery life time but I forgot (sorry)
time_limit = 480 #seconds

drone_speed = 30
sensor_d = 25 #cm

#Lab 8 
def set_altitude(alt):
    d_height = drone.height_from_pressure()
    sign = 1
    if alt <= d_height:
        sign = -1
    drone.set_throttle(sign * 20)
    drone.move()
    while sign * alt > sign * d_height:
        print(d_height, "centimeters")
        d_height = drone.height_from_pressure()
        drone.set_throttle(0)


def fly_drone():
    #Take off
    if drone.detect_wall(5):  # In millimeters with a max of 1500 mm
        print("Takeoff area is not clear. Shutting Down.")
        drone.close()
    else:
        drone.takeoff()
    time_elapsed = 0

    set_altitude(pressure) #This sets the drone to the wanted height
    
    while time_elapsed < time_limit: #How long the drone will fly for 
        time_elapsed = time.time() - time_start
        drone.set_pitch(drone_speed)
        drone.move()
        time.sleep(0.01)

        if is_object_detected(sensor_d):
            avoid_object(sensor_d)


def is_object_detected(distance):
    if drone.get_front_range("cm") <= distance:
        return True  #Path is not clear
    else:
        return False #Path is clear

#In easy terms, the drone will turn left if it can and if not then right and if not then back
def avoid_object(d_distance):
    drone.set_pitch(0)
    drone.turn_left()
    left_result = is_object_detected(d_distance)
    if left_result is False:
        print(left_result)
        return True
    drone.turn_right(180)
    right_result = is_object_detected(d_distance)
    if right_result is False:
        print(right_result)
        return True
    drone.turn_right()

    # if (left_result is False and right_result is False) or (left_result is True and right_result is False):
    #     return True
    # elif right_result is True and left_result is False:
    #     drone.turn_left(180)
    #     return True
    # else:
    #     drone.turn_right()
    #     return True


fly_drone()

drone.land()
drone.close()

