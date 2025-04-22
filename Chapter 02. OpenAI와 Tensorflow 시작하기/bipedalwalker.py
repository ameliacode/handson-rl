import gym

env = gym.make('BipedalWalker-v2')
env.reset()

for episode in range(100):
    observation = env.render()
    for t in range(10000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print(f"{t+1} timesteps taken for the episode")
            break 
