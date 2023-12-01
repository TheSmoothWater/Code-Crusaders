from codrone_edu.drone import *
drone = Drone()
drone.pair()

drone.takeoff()
drone.set_throttle(30)
drone.move(1)
drone.set_throttle(0)
while not drone.detect_wall(50):
    drone.hover()
drone.land()
drone.close()