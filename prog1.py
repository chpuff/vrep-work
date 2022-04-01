# Make sure to have the server side running in CoppeliaSim:
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

try:
    import sim
    import simConst
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time
# import vrep
import pypot
from pypot.vrep import *

print('Program started')
# sim.simxFinish(-1) # just in case, close all opened connections

close_all_connections()

print('Closed')

# floor = VrepIO(vrep_host='127.0.0.1', vrep_port=19999, scene="simple_scene.ttt", start=False)

floor = VrepIO(scene="simple_scene.ttt")

print('Opened')

floor.start_simulation()

print("Started")

print("position - ", floor.get_object_position('Sphere'))


floor.add_cube("myCube", [0,0,0], [0.1,0.1,0.1], 10)

floor.change_object_name("Cuboid", "myCube")

print('Name changed')

print('Program ended')

print("time - ", floor.get_simulation_current_time())

# floor.stop_simulation()

print("Stopped")


