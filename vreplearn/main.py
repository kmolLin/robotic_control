"""
Make it more robust.
Stop episode once the finger stop at the final position for 50 steps.
Feature & reward engineering.
"""
from xyz_path import ArmVREPEnv
from rl import DDPG

#設置全局變量
MAX_EPISODES = 500
MAX_EP_STEPS = 200  # 200
ON_TRAIN = True

# vrep gui mode
guimode = False

# 設置環境
env = ArmVREPEnv()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

# set RL method (continuous) # 設置學習方法 (DDPG)
rl = DDPG(a_dim, s_dim, a_bound)

# output log dir 
OUTPUT_GRAPH = True



steps = []
# 開始訓練
def train():
    # start training
    for i in range(MAX_EPISODES):
        #初始化回合設置
        #s = env.reset()
        s = env.reset()
        ep_r = 0.
        for j in range(MAX_EP_STEPS):
            # 環境渲染 
            #env.render()
            
            # RL 選擇 action
            if s is False:
                print("error point")
                break
            else:
                a = rl.choose_action(s)
            #print(a)
            #if a == False:
            #   print("error point")
            #    break
                
            #else :
                

            # 在環境中施加動作 由 a 決定的 得到新的state (s_) 以及 reward 以及判斷是否完成動作
            s_, r, done, check = env.step(a)
            
            if check == False:
                print("move to error point")
                break
            
            # DDPG 需要將經驗存取到記憶庫
            rl.store_transition(s, a, r, s_)
        
            ep_r += r
            if rl.memory_full:
                # start to learn once has fulfilled the memory
                rl.learn()
            # translate new state to old state
            s = s_
            if done or j == MAX_EP_STEPS-1 or check:
                #print(env.getposition())
                print('Ep: %i | %s | ep_r: %.1f | step: %i' % (i, '---' if not done else 'done', ep_r, j))
                break
    rl.save()
    rl.savelog(OUTPUT_GRAPH)


def eval():
    rl.restore()
    #env.render()
    #env.viewer.set_vsync(True)
    for i in range(3):
        s = env.reset()
        for _ in range(200):
            a = rl.choose_action(s)
            s, r, done, check = env.step(a)
            if done:
                break


if ON_TRAIN:
    train()
else:
    eval()



