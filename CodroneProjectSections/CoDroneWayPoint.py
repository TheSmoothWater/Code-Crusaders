# This is to keep the drone from flying off course
# Limit its height, z position, and x and y position
from codrone_edu.drone import *
drone = Drone()
drone.pair()

drone.takeoff()


def lift(duration):
    drone.set_throttle(30)
    drone.move(duration)
    drone.set_throttle(0)


lift(3)
drone.hover(1)
drone.set_waypoint()
drone.set_pitch(30)
drone.move(3)
drone.hover(1)

drone.goto_waypoint(drone.waypoint_data[0], 0.5)

drone.land()
drone.close()
