# XYZ envm
from vrep_commucation.vrepper import vrepper
import numpy as np
import os
import math
from invers_kinematic import armrobot

class ArmVREPEnv():
    dt = .1    # refresh rate time = 0.1 for one step
    action_bound = [-1, 1] # 轉動角度範圍
    
    #goal = {'x': 300.0, 'y': -161.96, 'z':18.0 ,'l': 0.05} # 藍色目標的座標及長度
    
    # can get the information by the envirement
    state_dim = 10
    
    # two links can input degrees control
    action_dim = 3
    
    
    def __init__(self):
        
        self.arm_info = np.zeros(3, dtype=[('l',np.float32), ('r', np.float32),('pos', np.float32), ('deg', np.float32)] )
        self.arm_info['l'] = 10        # 2 arms length
        self.arm_info['r'] = np.pi/6    # 2 arms angles information
        self.on_goal = 0
        self.actjoint = [0.0, 0.0, -90.0, 0.0, -90.0, 0.0]
        self.goal = {'l':10}
        self.armrobot = armrobot()
     
    def step(self, action):
        
        done = False
        # [a,b,c,d]
        
        action = np.clip(action, *self.action_bound) #*self.action_bound
        
        self.arm_info['pos'] += action * 0.1# 0.5   #self.dt
        #self.arm_info['pos'] %= np.pi * 2  #  normalize

        (X, Y, Z) = self.arm_info['pos']  # radian, angle
        
        print(X, Y, Z)
        
        # joint degree inverse
        (a1r, a2r, a3r, a4r, a5r, a6r), check = self.armrobot.Inverse_Kinematic(self.arm_info['pos'], [0, 180, 0], self.actjoint)
        # block position joint
        (blocka1r, blocka2r, blocka3r, blocka4r, blocka5r, blocka6r) , check= self.armrobot.Inverse_Kinematic([self.blockX, self.blockY, 0], [0, 180, 0], self.actjoint)
        
        a1 = a1r-blocka1r
        b1 = a2r-blocka2r
        c1 = a3r-blocka3r
        d1 = a4r-blocka4r
        e1 = a5r-blocka5r
        f1 = a6r-blocka6r
        
        a1 %= 360
        b1 %= 360
        c1 %= 360
        d1 %= 360
        e1 %= 360
        f1 %= 360
        
        
        # normalize features
        dist = [(self.blockX-X)/678, (self.blockY-Y)/678, (0-Z)/678]
        r = -np.sqrt(dist[0]**2+dist[1]**2+dist[2]**2)
        
        if self.blockX - self.goal['l']/2 < X < self.blockX + self.goal['l']/2:
            if self.blockY - self.goal['l']/2 < Y < self.blockY + self.goal['l']/2:
                if self.blockZ - self.goal['l']/2 < Z < self.blockZ + self.goal['l']/2:
                    r += 1.
                    self.on_goal += 1
                    if self.on_goal > 50:
                        done = True
        else:
            self.on_goal = 0
            
        s = np.concatenate(([a1/360., b1/360.,c1/360.,d1/360.,e1/360.,f1/360.], dist, [1. if self.on_goal else 0.]))
        
        #print(s, r, done)
        return s, r, done, check
        
    def test_reset(self):
        # act joint 
       # actjoint = []  # TODO: need to add position in this 
        
        #self.arm_info['r'] = 2 * np.pi * np.random.rand(4)
        #self.arm_info['r'] %= np.pi * 2
        
        self.on_goal = 0
        
        # this is random block position
        blockrtheta = np.random.uniform(-45.0,45.0, 1)
        blockranR = np.random.uniform(200, 678, 1)
        blockrtheta %= 360
        self.blockX =   300.0     #blockranR*math.cos(np.deg2rad(blockrtheta))
        self.blockY =   -162.0         #blockranR*math.sin(np.deg2rad(blockrtheta))
        self.blockZ = 10
        
        # this is random arm robot position
        rantehta = np.random.uniform(-45.0,45.0, 1)
        ranR = np.random.uniform(200, 678, 1)
        rantehta %= 360
        
        ranX = ranR*math.cos(np.deg2rad(rantehta))
        ranY = ranR*math.sin(np.deg2rad(rantehta))
        ranZ = np.random.uniform(0, 200, 1)

        self.arm_info['pos'] = [ranX, ranY, ranZ]
        
        # joint degree inverse
        (a1r, a2r, a3r, a4r, a5r, a6r), check = self.armrobot.Inverse_Kinematic(self.arm_info['pos'], [0, 180, 0], self.actjoint)
        
        # block position joint
        (blocka1r, blocka2r, blocka3r, blocka4r, blocka5r, blocka6r), check = self.armrobot.Inverse_Kinematic([self.blockX, self.blockY, 10], [0, 180, 0], self.actjoint)
        
        a1 = a1r-blocka1r
        b1 = a2r-blocka2r
        c1 = a3r-blocka3r
        d1 = a4r-blocka4r
        e1 = a5r-blocka5r
        f1 = a6r-blocka6r
        
        a1 %= 360
        b1 %= 360
        c1 %= 360
        d1 %= 360
        e1 %= 360
        f1 %= 360
        
        # normalize features
        dist = [(self.blockX-ranX)[0]/20, (self.blockY-ranY)[0]/20, (self.blockZ-ranZ)[0]/20]
        
        s = np.concatenate(([a1/360., b1/360.,c1/360.,d1/360.,e1/360.,f1/360.], dist, [1. if self.on_goal else 0.]))
        return s
        
    def getposition(self):
        
        self.venv.start_blocking_simulation()
        #a2xy_ = np.array([self.motor2.get_joint_angle()])
        #a3xy_ = np.array([self.motor3.get_joint_angle()])
        #a4xy_ = np.array([self.motor4.get_joint_angle()])
        #finger = np.array([self.gripperCenter.get_position()])
        #print(a2xy_, a3xy_, a4xy_, finger)
        a1r = np.random.uniform(np.deg2rad(-170), np.deg2rad(340), 1) # a1  -170~340
        a2r = np.random.uniform(np.deg2rad(-135), np.deg2rad(270), 1)  #  a2 -135~ 270
        a3r = np.random.uniform(np.deg2rad(-135), np.deg2rad(270), 1)  #  a3 -135~ 270
        a4r = np.random.uniform(np.deg2rad(-90), np.deg2rad(180), 1)  #  a4 -90~ 180
        
        self.motor1.set_position_target(np.rad2deg(a1r))
        self.motor2.set_position_target(np.rad2deg(a2r))
        self.motor3.set_position_target(np.rad2deg(a3r))
        self.motor4.set_position_target(np.rad2deg(a4r))
        
        self.venv.step_blocking_simulation()
        
        print(np.rad2deg(a1r), np.rad2deg(a2r), np.rad2deg(a3r), np.rad2deg(a4r))
        
        while True:
            self.motor1.set_position_target(np.rad2deg(a1r))
            self.motor2.set_position_target(np.rad2deg(a2r))
            self.motor3.set_position_target(np.rad2deg(a3r))
            self.motor4.set_position_target(np.rad2deg(a4r))
            
            ra = self.motor1.get_joint_angle()
            rb = self.motor2.get_joint_angle()
            rc = self.motor3.get_joint_angle()
            rd = self.motor4.get_joint_angle()
            
            self.venv.step_blocking_simulation()
            #print(ra, rb, rc, rd)
            if abs(np.rad2deg(a1r)-ra) <5.0:
                if abs(np.rad2deg(a2r)-rb) <5.0:
                    if abs(np.rad2deg(a3r)-rc) <5.0:
                        if abs(np.rad2deg(a4r)-rd) <5.0:
                            break
                
        
        print(np.rad2deg(a1r), np.rad2deg(a2r), np.rad2deg(a3r), np.rad2deg(a4r))
        print(ra, rb, rc, rd)
        
        #return finger
        
if __name__ == '__main__':
    env = ArmVREPEnv()
    a = env.test_reset()
    print(a)
