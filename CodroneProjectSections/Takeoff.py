from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()

distance = 120
if drone.detect_wall(distance): # In millimeters with a max of 1500 mm
    print("Takeoff area is not clear. Shutting Down.")
    drone.close()
else:
    drone.takeoff()


def lift(duration):
    drone.set_throttle(20)
    drone.move(duration)
    time.sleep(0.01)
