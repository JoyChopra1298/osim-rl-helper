from osim.env import ProstheticsEnv
import time

env = ProstheticsEnv(visualize=True,integrator_accuracy=3e-3)
observation = env.reset()

print("MUSCLE SET")
muscleSet = env.osim_model.muscleSet
for i in range(muscleSet.getSize()):
            print(i,muscleSet.get(i).getName())

# med - medial(towards the middle), lat - lateral(away from the middle)
muscle_dict = {"add_brev_r.excitation":1,"bifemsh_r.excitation":3,"glut_max1_r.excitation":4,"psoas_r.excitation":5
,"rect_fem_r.excitation":6,"vas_lat_r.excitation":7,"add_brev_l.excitation":9,"bifemsh_l.excitation":11,"glut_max1_l.excitation":12,
"psoas_l.excitation":13,"rect_fem_l.excitation":14,"vas_lat_l.excitation":15,"med_gas_l.excitation":16,"soleus_l.excitation":17,
"tib_ant_l.excitation":18}

header_indices = [10,13,20,24,28,31,53,56,63,67,71,74,75,77,81]

with open("subject02_running_CMC_controls.sto") as f:
	headers = f.readline().split()
	count = 0
	for line in f.readlines():
		if(count%5==0):
			values = [float(x) for x in line.split()]
			action = env.action_space.sample() * 0 
			for header_index in header_indices:
				action[muscle_dict[headers[header_index]]] = values[header_index]
			print(action)
			env.step(action)
		count+=1