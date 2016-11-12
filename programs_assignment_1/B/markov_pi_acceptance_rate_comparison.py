import random
import math

x, y = 1.0, 1.0
n_trials = 2**12
n_hits = 0
acceptance_list = []
delta_list = [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]

for delta in delta_list:
    n_hits = 0;
    n_accepted_moves = 0
    for i in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            n_accepted_moves += 1
        if x**2 + y**2 < 1.0: 
            n_hits += 1
    acceptance_list.append(n_accepted_moves / float(n_trials))
    
print ("delta | acceptance rate")
for i in range(len(delta_list)):
    print "%f | %f" %(delta_list[i],acceptance_list[i]) 
    

