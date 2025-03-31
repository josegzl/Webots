from controller import Robot

def run_robot(robot):
    timestep = timestep = int(robot.getBasicTimeStep()) 
    maxVel = 6.28 
    porcentage= 0.28 

    LW = robot.getDevice('LW')  
    RW = robot.getDevice('RW')  
    RS = robot.getDevice('RS')
    LS = robot.getDevice('LS') 
    LS.enable(timestep)
    RS.enable(timestep)

    LW.setPosition(float('inf'))
    RW.setPosition(float('inf'))
    LW.setVelocity(0.0)
    RW.setVelocity(0.0)
    
    while robot.step(timestep) != -1:
        RSValue = RS.getValue()
        LSValue = LS.getValue()
        #print(f'Right: {RSValue}  Left: {LSValue}')
        leftS = maxVel * porcentage
        rightS = maxVel * porcentage

        
        if LSValue >= 1000 and RSValue < 1000:  
            leftS = -maxVel * porcentage 
            rightS = maxVel * porcentage 
            print("RIGHT")

        elif RSValue >= 1000 and LSValue < 1000:
            rightS = -maxVel * porcentage  
            leftS = maxVel * porcentage 
            print("LEFT")

        
        LW.setVelocity(leftS)
        RW.setVelocity(rightS)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
