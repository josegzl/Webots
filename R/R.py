import math
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())  
timestep_sec = timestep / 1000.0  

# Parámetros del robot
radius = 0.05 
rad = 2 * math.pi * radius
conv = rad / (2 * math.pi)

# Dispositivos
RM = robot.getDevice('RWM')  
LM = robot.getDevice('LWM')
RS = robot.getDevice('RS')
LS = robot.getDevice('LS')
gyro = robot.getDevice('gyro') 
cam= robot.getDevice('camera') 
dis= robot.getDevice('distance sensor')
dis.enable(timestep)
cam.enable(timestep)
gyro.enable(timestep)
RS.enable(timestep)
LS.enable(timestep)

LM.setPosition(float('inf'))
RM.setPosition(float('inf'))


sensor = [0, 0]
linear = 0
delta_theta = 0.0



def delay(time_ms):
    steps = int(time_ms / timestep)
    for _ in range(steps):
        robot.step(timestep)


def avanzar(distancia):
    global linear
    linear = 0  
    while linear < distancia:
        sen = dis.getValue()
        print(sen)
        LM.setVelocity(1)
        RM.setVelocity(1)
        robot.step(timestep)
        sensor[0] = LS.getValue()
        sensor[1] = RS.getValue()
        señal = [x * conv for x in sensor]
        linear = (señal[0] + señal[1]) / 2
    LM.setVelocity(0)
    RM.setVelocity(0)
    delay(500)  

def girar(grados):
    global delta_theta
    delta_theta = 0.0  
    while abs(math.degrees(delta_theta)) < grados:
        sen = dis.getValue()
        print(sen)
        LM.setVelocity(-1)
        RM.setVelocity(1)
        robot.step(timestep)
        gyro_data = gyro.getValues()
        w = gyro_data[2]  
        delta_theta += w * timestep_sec
        
    LM.setVelocity(0)
    RM.setVelocity(0)
    delay(500)  

while robot.step(timestep) != -1:

    angle= 75
    avanzar(0.25)
    girar(angle)
    avanzar(0.5)
    girar(angle)
    avanzar(0.75)
    girar(angle)
    avanzar(1.0)
    girar(angle)
    avanzar(1.25)
    
    break
    

