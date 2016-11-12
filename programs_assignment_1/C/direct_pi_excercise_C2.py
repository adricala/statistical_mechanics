'''
Statistical Mechanics Course
Lecture 1 - Excercise C2

Created on Nov 12, 2016

@author: Adrian Garcia
'''
import random, math
n_trials = 400000
n_hits = 0
var = 0.0
Obs = 0.0
Obs_2 = 0.0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)    
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs += 4.0
        Obs_2 += 16.0    

Obs_mean = Obs / n_trials
Obs_2_mean = Obs_2 / n_trials
Obs_var_mean = Obs_2_mean - Obs_mean**2
Obs_std_dev = math.sqrt(Obs_var_mean)  

print "pi \t Obs \t Obs_2 \t Obs_2 - Obs^2 \t sqrt(Obs_2 - Obs^2) " 
print str(4.0 * n_hits / float(n_trials)) + "\t" + str(Obs_mean) + "\t" + str(Obs_2_mean) + "\t" + str(Obs_var_mean)  + "\t" +  str(Obs_std_dev) 
