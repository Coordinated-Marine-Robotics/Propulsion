## N = Global North = 0deg , angles increase clockwise
## GDM = required global direction of motion
## n = local north = 0deg , angles increase clockwise
## LDM = required local direction of motion
## Heading = CGDF = current global direction it's facing = angle of n from N
## (CLDF always = 0 by definition)

## 3 thrusters:
## T1 at n (0) facing e (90)
## T2 at se (120) facing nne (210)
## T3 at sw (240) facing ssw (330)

ESC_Fwd_Max = 2500 ## = value assigned to ESC for max forward speed
ESC_Fwd_Min = 1501 #? ## = value assigned to ESC for min forward speed
ESC_Rev_Max = 1499 #? ## = value assigned to ESC for max reverse speed
ESC_Rev_Min = 500 ## = value assigned to ESC for min reverse speed

T_cut_off = 0.1 #? ## value range around 0 that don't bother turning on at all as close to 0

import numpy as np

x1 = 69.49				## distance of T1 from centre of foam
x2 = x3 = 103.21		## distance of T2 & T3 from centre of foam
theta = np.radians(30)	## angle of T2 & T3 from n

#T1S = 0  ## ESC value to be assigned to each thruster
#T2S = 0  # Won't need these in actual code as should be previously defined
#T3S = 0  # Actually might need them at the very very top (outside the run code)

def Thruster_Values(GDM, Heading, Speed_PC): ## Speed_PC = percentage of max speed required in direction of motion (value from 0 to 1)
    global T1S , T2S , T3S, LDM
    LDM = GDM - Heading
    if LDM < 0:
        LDM = 360+LDM
    LDM = np.radians(LDM)
    a = np.array([[np.sin(LDM),-np.cos(theta-LDM),np.cos(theta+LDM)] , [np.cos(LDM),-np.sin(theta-LDM),-np.sin(theta+LDM)] , [x1,x2,x3]])
    b = np.array([1,0,0])
    T = np.linalg.solve(a, b)
    TiS = []
    for Ti in T:
        if -T_cut_off < Ti < T_cut_off:	## Check likely values close to 0
            TiS.append(0)
        if Ti > T_cut_off:
            TiS.append(ESC_Fwd_Min + ((ESC_Fwd_Max - ESC_Fwd_Min)*Speed_PC) * Ti / max(abs(T))) # check this
        if Ti < -T_cut_off:
            TiS.append(ESC_Rev_Min + ((ESC_Rev_Max - ESC_Rev_Min)*Speed_PC) * -Ti / max(abs(T)))
    [T1S, T2S, T3S] = TiS

def turnLeft(Turn_Speed_PC):
	global T1S , T2S , T3S
	T1S = T2S = T3S = ESC_Fwd_Min + ((ESC_Fwd_Max - ESC_Fwd_Min)*Turn_Speed_PC)

def turnRight(Turn_Speed_PC):
	global T1S , T2S , T3S
	T1S = T2S = T3S = ESC_Rev_Min + ((ESC_Rev_Max - ESC_Rev_Min)*Turn_Speed_PC)

#Thruster_Values(51,66,0.5)
#print('LDM = ', np.degrees(LDM))
turnRight(0.7)
print('T1S =', T1S)
print('T2S =', T2S)
print('T3S =', T3S)