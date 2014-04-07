from random import *
import math
import numpy 

# part a
totalU = 0
us = []
NUM_RUNS = 3000
for i in range(NUM_RUNS):
	value = 1.0
	for j in range(20):
		u = random()
		if u < 0.5:
			value = value * 2
		else:
			value = value * 0.5
	totalU += value
	us.append(value)

array = numpy.array([us])
u_std = numpy.std(array) * math.sqrt(1/ (NUM_RUNS-1))
u_mean = numpy.mean(array)

print "Expected U value is " + str(u_mean)
print "95 percent confidence interval: " + str(u_mean - 1.96 * u_std) + " to " + str(u_mean + 1.96 * u_std)

totalV = 0
NUM_RUNS = 3000
vs = []
for i in range(NUM_RUNS):
	value = 1.0
	for j in range(20):
		stock = value * 0.5
		cash = value * 0.5
		u = random()
		if u < 0.5:
			stock = stock * 2
		else:
			stock = stock * 0.5
		value = stock + cash
	totalV += value
	vs.append(value)
array = numpy.array([vs])
v_std = numpy.std(array) * math.sqrt(1/ (NUM_RUNS-1))
v_mean = numpy.mean(array)
print "Expected V value is " + str(v_mean)

print "95 percent confidence interval: " + str(v_mean - 1.96 * v_std) + " to " + str(v_mean + 1.96 * v_std)


#part b 
difference_mean = v_mean - u_mean
difference_std = math.sqrt(u_std ** 2 + v_std **2)
print "The mean is : " + str(difference_mean)
print "The 95 percent confidence interval is : " + str(difference_mean - 1.96 * difference_std) + " to " + str(difference_mean + 1.96 * difference_std)

#part c 
v_u_array = []
for i in range(NUM_RUNS):
	u_value = 1.0 
	v_value = 1.0 
	for j in range(20):
		stock = v_value /2
		cash = v_value /2
		u = random()
		if u < 0.5:
			stock = stock * 2
			u_value = u_value * 2
		else:
			stock = stock * 0.5
			u_value = u_value * 0.5
		v_value = cash + stock
		difference = v_value - u_value
	v_u_array.append(difference)
array = numpy.array([v_u_array])
sync_difference_mean = numpy.mean(array)
sync_difference_std = numpy.std(array)/math.sqrt(NUM_RUNS-1)
print "The mean is : " + str(sync_difference_mean)
print "The 95 percent confidence interval is : "+ str(sync_difference_mean - 1.96 * sync_difference_std) + " to " + str(sync_difference_mean + 1.96 * sync_difference_std)

#part d 


