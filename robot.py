#TODO: allow multiwheel, wheel spacing, OR non-static wheels, also allow better motor PWM voltage+battery -> torque output calcm 

class Robot:
    def __init__(self, x, y, head, battery, uk, width, mass, wheelRadius, motorStallTorque, motorMaxRPM, motorGearing, maxV, maxA, maxJ, kR):
        #Instantaeous Robot Properties 
        self.x = x
        self.y = y
        self.veloL = 0

        self.veloR = 0
        self.accelR = 0
        self.
        self.head = head
        self.battery = battery
        
        #Static Robot Characteristics 
        self.uk = uk
        self.width = width
        self.mass = mass
        self.wheelRadius = wheelRadius
        self.motorStallTorque = motorStallTorque
        self.motorMaxRPM = motorMaxRPM
        self.motorGearing = motorGearing
        self.maxV = maxV
        self.maxA = maxA
        self.maxJ = maxJ
        self.kR = kR #coeficient of randomness in applied speed/velo and friction
        
        #rate limiters
        self.prevVeloL = 0
        self.prevVeloR = 0
        self.prevAccelL = 0
        self.prevAccelR = 0
        
        
    def update(deltaT, battery, speedL, speedR):
        TorqueL = (-motorStallTorque/motorMaxRPM * )
         

    def getPos():
        return [self.x, self.y, self.head]
       
