from tmnf_env import TmnfEnv
from agent import Agent

if __name__ == "__main__":
    env = TmnfEnv()
    model = Agent(env)
    model.learn(total_timesteps=10000)