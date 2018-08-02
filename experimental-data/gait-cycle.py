from osim.env import ProstheticsEnv

env = ProstheticsEnv(visualize=True,integrator_accuracy=5e-2)

observation = env.reset()

for i in range(20):
	print(i)
	print(str(env.osim_model.state))
	print(str(env.osim_model.get_state_desc()))
	print(str(env.osim_model.get_activations()))
	observation, reward, done, info = env.step(env.action_space.sample())
