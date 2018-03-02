# test script for DDPG learning (RL learning)

from vrep_commucation.vrepper import vrepper
import numpy as np
import os


class ArmVREPEnv():
    dt = .1    # refresh rate time = 0.1 for one step
    action_bound = [-1, 1] # 轉動角度範圍
    goal = {'x': 0.0, 'y': 0.2, 'z':0.205 ,'l': 0.05} # 藍色目標的座標及長度
    
    # can get the information by the envirement
    state_dim = 25
    
    # two links can input degrees control
    action_dim = 4
    
    def __init__(self,headless=True):
        
        self.arm_info = np.zeros(4, dtype=[('l',np.float32), ('r', np.float32)])  # make (2,2) martix
        self.arm_info['l'] = 100        # 2 arms length
        self.arm_info['r'] = np.pi/6    # 2 arms angles information
        self.on_goal = 0
        
        self.venv = venv = vrepper(headless=False)
        venv.start()
        venv.load_scene(
            os.getcwd() + '/armtest.ttt')

        self.motor1 = venv.get_object_by_name('A_joint')
        self.motor2 = venv.get_object_by_name('B_joint')
        self.motor3 = venv.get_object_by_name('C_joint')
        #self.motor4 = venv.get_object_by_name('PhantomXPincher_joint4')

        self.gripperCenter = venv.get_object_by_name('gettingpoint')

        print('(armVREP) initialized')
        
     
    def step(self, action):
        
        done = False
        # [a,b,c,d]
        cc = action
        print(action)
        
        action[0] = np.clip(action[0], *[np.deg2rad(255), np.deg2rad(-75)])  #*self.action_bound
        action[1] = np.clip(action[1],  *[np.deg2rad(175), np.deg2rad(-25)])
        action[2] = np.clip(action[2],  *[np.deg2rad(185), np.deg2rad(-55)])
        #action[3] = np.clip(action[3],  *[np.deg2rad(-90), np.deg2rad(180)])
        
        self.arm_info['r'] += action * 0.1   #self.dt
        print(self.arm_info['r'])
        self.arm_info['r'] %= np.pi * 2  #  normalize
        
        (a1l, a2l , a3l, a4l) = self.arm_info['l']  # radius, arm length
        (a1r, a2r, a3r, a4r) = self.arm_info['r']  # radian, angle
        
        # move angle
        
        self.motor1.set_position_target(np.rad2deg(a1r))
        self.motor2.set_position_target(np.rad2deg(a2r))
        self.motor3.set_position_target(np.rad2deg(a3r))
        #self.motor4.set_position_target(np.rad2deg(a4r))
        
        a2xy_ = np.array(self.motor2.get_position())
        a3xy_ = np.array(self.motor3.get_position())
        a4xy_ = np.array(self.motor4.get_position())
        finger = np.array(self.gripperCenter.get_position())
        
        self.venv.step_blocking_simulation()
        
        # normalize features
        dist1 = [(self.goal['x'] - a2xy_[0]) / 0.8, (self.goal['y'] - a2xy_[1]) / 0.8, (self.goal['z'] - a2xy_[2]) / 0.8]
        dist2 = [(self.goal['x'] - a3xy_[0]) / 0.8, (self.goal['y'] - a3xy_[1]) / 0.8, (self.goal['z'] - a3xy_[2]) / 0.8]
        dist3 = [(self.goal['x'] - a4xy_[0]) / 0.8, (self.goal['y'] - a4xy_[1]) / 0.8, (self.goal['z'] - a4xy_[2]) / 0.8]
        dist4 = [(self.goal['x'] - finger[0]) / 0.8, (self.goal['y'] - finger[1]) / 0.8, (self.goal['z'] - finger[2]) / 0.8]
        
        r = -np.sqrt(dist4[0]**2+dist4[1]**2+dist4[2]**2)
        
        if self.goal['x'] - self.goal['l']/2 < finger[0] < self.goal['x'] + self.goal['l']/2:
            if self.goal['y'] - self.goal['l']/2 < finger[1] < self.goal['y'] + self.goal['l']/2:
                if self.goal['z'] - self.goal['l']/2 < finger[1] < self.goal['z'] + self.goal['l']/2:
                    r += 1.
                    self.on_goal += 1
                    if self.on_goal > 50:
                        done = True
        else:
            self.on_goal = 0
            
        s = np.concatenate((a2xy_/0.8, a3xy_/0.8, a4xy_/0.8, finger/0.9, dist1 + dist2 + dist3+ dist4 
                                        , [1. if self.on_goal else 0.]))
                                        
        
        
        #print(s, r, done)
        return s, r, done
        
    def compute_reward(self):
        # TODO : need to add new method to calc the reward
        pass
        
    def sample_action(self):
        return np.random.rand(4)-0.5    # two radians
        
    def stopsim(self):
        self.venv.stop_simulation()
        
        
    def goal_distance(self, goal_a, goal_b):
        return np.linalg.norm(goal_a - goal_b, axis=-1)
        
    def test_rest(self):
        #self.venv.stop_blocking_simulation()
        self.venv.start_blocking_simulation()
        
        #self.arm_info['r'] = 2 * np.pi * np.random.rand(4)
        #self.arm_info['r'] %= np.pi * 2
        
        self.on_goal = 0
        
        a1r = np.random.uniform(np.deg2rad(-170), np.deg2rad(340), 1) # a1  -170~340
        a2r = np.random.uniform(np.deg2rad(-135), np.deg2rad(270), 1)  #  a2 -135~ 270
        a3r = np.random.uniform(np.deg2rad(-135), np.deg2rad(270), 1)  #  a3 -135~ 270
        a4r = np.random.uniform(np.deg2rad(-90), np.deg2rad(180), 1)  #  a4 -90~ 180
        
        self.arm_info['r'] = a1r, a2r, a3r, a4r
        (a1r, a2r, a3r, a4r) = self.arm_info['r']  # radian, angle
        
        #a1r, a2r, a3r, a4r = [0, 0, 0, 0]
    
        count = 0
        while count<20:
            self.motor1.set_position_target(np.rad2deg(a1r))
            self.motor2.set_position_target(np.rad2deg(a2r))
            self.motor3.set_position_target(np.rad2deg(a3r))
            self.motor4.set_position_target(np.rad2deg(a4r))
            
            ra = self.motor1.get_joint_angle()
            rb = self.motor2.get_joint_angle()
            rc = self.motor3.get_joint_angle()
            rd = self.motor4.get_joint_angle()
            
            self.venv.step_blocking_simulation()
            #time.sleep(100)
            count = count+1
            
            #print(ra, rb, rc, rd)
            #if abs(np.rad2deg(a1r)-ra) <10.0:
              #  if abs(np.rad2deg(a2r)-rb) <10.0:
                #    if abs(np.rad2deg(a3r)-rc) <10.0:
                  #      if abs(np.rad2deg(a4r)-rd) <10.0:
            
        a2xy_ = np.array(self.motor2.get_position())
        a3xy_ = np.array(self.motor3.get_position())
        a4xy_ = np.array(self.motor4.get_position())
        finger = np.array(self.gripperCenter.get_position())
                            
        
        print(np.rad2deg(a1r), np.rad2deg(a2r), np.rad2deg(a3r), np.rad2deg(a4r))
        print(ra, rb, rc, rd)
        
        # normalize features
        dist1 = [(self.goal['x'] - a2xy_[0]) / 0.8, (self.goal['y'] - a2xy_[1]) / 0.8, (self.goal['z'] - a2xy_[2]) / 0.8]
        dist2 = [(self.goal['x'] - a3xy_[0]) / 0.8, (self.goal['y'] - a3xy_[1]) / 0.8, (self.goal['z'] - a3xy_[2]) / 0.8]
        dist3 = [(self.goal['x'] - a4xy_[0]) / 0.8, (self.goal['y'] - a4xy_[1]) / 0.8, (self.goal['z'] - a4xy_[2]) / 0.8]
        dist4 = [(self.goal['x'] - finger[0]) / 0.8, (self.goal['y'] - finger[1]) / 0.8, (self.goal['z'] - finger[2]) / 0.8]
        
        s = np.concatenate((a2xy_/0.8, a3xy_/0.8, a4xy_/0.8, finger/0.9, dist1 + dist2 + dist3+ dist4 
                                        , [1. if self.on_goal else 0.]))
        
        return s
        
        
    
    def reset(self):
        self.venv.stop_blocking_simulation()
        self.venv.start_blocking_simulation()
        
        
        self.arm_info['r'] = 2 * np.pi * np.random.rand(4)
        self.arm_info['r'] %= np.pi * 2
        self.on_goal = 0
        
        #(a1l, a2l) = self.arm_info['l']   radius, arm length
        
        (a1r, a2r, a3r, a4r) = self.arm_info['r']  # radian, angle
        
        self.motor1.set_position_target(np.rad2deg(a1r))
        self.motor2.set_position_target(np.rad2deg(a2r))
        self.motor3.set_position_target(np.rad2deg(a3r))
        self.motor4.set_position_target(np.rad2deg(a4r))
        
        self.venv.step_blocking_simulation()
        
        a2xy_ = np.array(self.motor2.get_position())
        a3xy_ = np.array(self.motor3.get_position())
        a4xy_ = np.array(self.motor4.get_position())
        finger = np.array(self.gripperCenter.get_position())
        
        # normalize features
        dist1 = [(self.goal['x'] - a2xy_[0]) / 0.8, (self.goal['y'] - a2xy_[1]) / 0.8, (self.goal['z'] - a2xy_[2]) / 0.8]
        dist2 = [(self.goal['x'] - a3xy_[0]) / 0.8, (self.goal['y'] - a3xy_[1]) / 0.8, (self.goal['z'] - a3xy_[2]) / 0.8]
        dist3 = [(self.goal['x'] - a4xy_[0]) / 0.8, (self.goal['y'] - a4xy_[1]) / 0.8, (self.goal['z'] - a4xy_[2]) / 0.8]
        dist4 = [(self.goal['x'] - finger[0]) / 0.8, (self.goal['y'] - finger[1]) / 0.8, (self.goal['z'] - finger[2]) / 0.8]
        
        s = np.concatenate((a2xy_/0.8, a3xy_/0.8, a4xy_/0.8, finger/0.9, dist1 + dist2 + dist3+ dist4 
                                        , [1. if self.on_goal else 0.]))
        
        return s
        
    def getposition(self):
        
        self.venv.start_blocking_simulation()
        #a2xy_ = np.array([self.motor2.get_joint_angle()])
        #a3xy_ = np.array([self.motor3.get_joint_angle()])
        #a4xy_ = np.array([self.motor4.get_joint_angle()])
        finger = np.array([self.gripperCenter.get_position()])
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
    env.getposition()
    #print(s)
    #print("*"*10)
    #print(env.sample_action())
        #for k in range(5):
            #env.step(env.sample_action())
    #env.getposition()
