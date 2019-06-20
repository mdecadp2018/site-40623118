import vrep
import keyboard
import sys, math
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV =360   

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
errorCode,RR_handle=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_oneshot_wait)


if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()

def speed(handle,speed):
    errorCode = vrep.simxSetJointTargetVelocity(clientID,handle,speed,vrep.simx_opmode_oneshot_wait)
def start():
    errorCode =vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

start()

while True:
    try:
        if keyboard.is_pressed('a'):
            speed(LR_handle,L_KickBallVel)
        else:
            speed(LR_handle,R_KickBallVel)
        if keyboard.is_pressed('l'):
            speed(RR_handle,R_KickBallVel)
        else:
            speed(RR_handle,L_KickBallVel)
        if keyboard.is_pressed('UP'): 
            speed(PL_handle,10)
        else:
            speed(PL_handle,-10)
    except:
        break 
    










