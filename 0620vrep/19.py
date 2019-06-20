import vrep
import keyboard
import time
import sys, math     
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
   
vrep.simxFinish(-1)
 
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV = 360
n=1
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
     
errorCode,B_handle=vrep.simxGetObjectHandle(clientID,'B',vrep.simx_opmode_oneshot_wait)
errorCode,LR_handle=vrep.simxGetObjectHandle(clientID,'LR',vrep.simx_opmode_oneshot_wait)
errorCode,RR_handle=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_oneshot_wait)
errorCode,PR_handle=vrep.simxGetObjectHandle(clientID,'PR',vrep.simx_opmode_oneshot_wait)
 
 
vrep.simxSetJointTargetVelocity(clientID,RR_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,LR_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,PR_handle,0,vrep.simx_opmode_oneshot_wait)
 
 
def con(): 
      errorCode = vrep.simxSetJointTargetVelocity(clientID,RR_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
def clo():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,RR_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait) 
def right():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,PR_handle,2,vrep.simx_opmode_oneshot_wait)
def left():
      errorCode =  vrep.simxSetJointTargetVelocity(clientID,PR_handle,-200,vrep.simx_opmode_oneshot_wait)
def con1():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,LR_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
def clo1():
      errorCode = vrep.simxSetJointTargetVelocity(clientID,LR_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait) 

 
 
vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
while True:
    try:
            if keyboard.is_pressed('a'): 
                con()
            else:  
                clo()
            if keyboard.is_pressed('Up Arrow'):  
                right()
            else:  
                left()

            if keyboard.is_pressed('l'): 
                clo1()
            else:  
                con1()
    except:
            break