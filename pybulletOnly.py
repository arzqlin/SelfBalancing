import pybullet as p
import pybullet_data
import gym
from time import sleep

client = p.connect(p.GUI)
p.setGravity(0, 0, -9.8, physicsClientId=client)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
carId = p.loadURDF("cart.urdf")

angle = p.addUserDebugParameter("Steering", -0.5, 0.5, 0)
throttle = p.addUserDebugParameter("Throttle", 0, 20, 0)

while p.isConnected():
    p.stepSimulation()
