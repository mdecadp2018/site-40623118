import vrep
import keyboard
from time import sleep
import sys, math
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV =360   
Move_Minus =-0.1         
Move_Plus =0.1
n=1
R_KickBallVel = (math.pi/180)*KickBallV
L_KickBallVel = -(math.pi/180)*KickBallV
P_KickBallVel = -KickBallV
B_KickBallVel = KickBallV/50
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode,B_handle=vrep.simxGetObjectHandle(clientID,'B',vrep.simx_opmode_oneshot_wait)
errorCode,PL_handle=vrep.simxGetObjectHandle(clientID,'PL',vrep.simx_opmode_oneshot_wait)
errorCode,LR_handle=vrep.simxGetObjectHandle(clientID,'LR',vrep.simx_opmode_oneshot_wait)
errorCode,RL_handle=vrep.simxGetObjectHandle(clientID,'RL',vrep.simx_opmode_oneshot_wait)


if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
    

    
def start():
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)



while True:
    try:
        if keyboard.is_pressed('a'):
            vrep.simxSetJointTargetVelocity(clientID,LR_handle,L_KickBallVel,vrep.simx_opmode_oneshot_wait)
        else:
            vrep.simxSetJointTargetVelocity(clientID,LR_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
        
        if keyboard.is_pressed('l'):
            vrep.simxSetJointTargetVelocity(clientID,RR_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
        else:
            vrep.simxSetJointTargetVelocity(clientID,RR_handle,L_KickBallVel,vrep.simx_opmode_oneshot_wait)
        if keyboard.is_pressed('UP'): 
            vrep.simxSetJointTargetVelocity(clientID,PL_handle,100,vrep.simx_opmode_oneshot_wait)
        else:
            vrep.simxSetJointTargetVelocity(clientID,PL_handle,-10,vrep.simx_opmode_oneshot_wait)
    except:
        break 
    
start()