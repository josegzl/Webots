import math
from controller import Robot


robot = Robot()

timestep = int(robot.getBasicTimeStep())  
timestep_sec = timestep / 1000.0  


gyro = robot.getDevice('gyro')  
gyro.enable(timestep)

LM = robot.getDevice('LWM')   
RM = robot.getDevice('RWM')    

LM.setPosition(float('inf'))
RM.setPosition(float('inf'))


theta = 0.0    
target_angle = 90.0  


LM.setVelocity(1)
RM.setVelocity(-1)

# Bucle principal
while robot.step(timestep) != -1:
    
    gyro_values = gyro.getValues()
    angular_velocity = gyro_values[2]  
    
    
    theta += angular_velocity * timestep_sec  
    
    
    theta_deg = math.degrees(theta)

    print(f"Ángulo girado: {theta_deg:.2f}°")

    
    if abs(theta_deg) >= target_angle:
        LM.setVelocity(0.0)
        RM.setVelocity(0.0)
        break