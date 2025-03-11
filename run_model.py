
from tmnf_env import TmnfEnv
from agent import Agent

env = TmnfEnv()
obs = env.reset()

model = Agent.load_model()  #addd checkpoint

while True:
    action, _states = model.predict(obs, deterministic=False)
    obs, reward, dones, info = env.step(action)