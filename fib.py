# Let’s test your PyRTL knowledge! Create a file called “fib.py”. Inside it:

# Design a circuit that has 2 inputs and 1 output. The names and bitwidths should match exactly.
# Input “A”, 32 bits
# Input “B”, 32 bits
# Output “result”, 32 bits

# The inputs A and B are the 2 starting terms of the fibonacci sequence respectively.

# The output is the nth fibonacci number, where n is the current cycle number.

# So, if A is 0 and B is 1, then:
# Cycle 0: result = 0
# Cycle 1: result = 1
# Cycle 2: result = 1
# Cycle 3: result = 2
# etc

import pyrtl

val_a = pyrtl.Input(bitwidth = 32, name = 'A') #input a
val_b = pyrtl.Input(bitwidth = 32, name = 'B') #input b
result = pyrtl.Output(bitwidth = 32, name = 'result') 

fib1 = pyrtl.Register(bitwidth = 32, name = 'fib n-1')
fib2 = pyrtl.Register(bitwidth = 32, name = 'fib n-2')

sum_res = pyrtl.WireVector(bitwidth = 32, name = 'A + B')
sum_res <<= fib1 + fib2

with pyrtl.conditional_assignment:
	with fib1 == 0:
		fib1.next |= val_b
		fib2.next |= val_a
		result |= val_a

	with pyrtl.otherwise:
		fib2.next |= fib1
		fib1.next |= sum_res
		result |= fib1
#result <<= fib1

#Simulation 
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer = sim_trace)

for cycle in range(9):
	sim.step({
		'A':1,
		'B':1
	})
	print(sim_trace.trace['result'][cycle])
	#print(sim_trace.trace['fib n-1'][cycle])
	#print(sim_trace.trace['fib n-2'][cycle])
sim_trace.render_trace()

