from codrone_edu.drone import *
drone = Drone()
drone.pair()

drone.takeoff()

while True:
    drone.hover()


    end = input("Input anything to end program\n")
    if len(end) > 0:
        break


drone.land()
drone.close()