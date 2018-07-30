with open("joint-angles.txt") as f:
	f1 = open("joint-angles.csv","w+")
	for line in f.readlines():
		f1.write(",".join(line.split()))
		f1.write("\n")	
