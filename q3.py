### Implementing and simulating multiplexers in PyRTL ###

import pyrtl
import random

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
# < add your code here >
a = pyrtl.Input(bitwidth=3, name='a')
b = pyrtl.Input(bitwidth=3, name='b') 
c = pyrtl.Input(bitwidth=3, name='c') 
d = pyrtl.Input(bitwidth=3, name='d')
e = pyrtl.Input(bitwidth=3, name='e') 

# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
# < add your code here >
o = pyrtl.Output(bitwidth=3, name='o')

# Describe your 5:1 MUX implementation
# < add your code here >
with pyrtl.conditional_assignment:
	with s == 0:
		o |= a
	with s == 1:
		o |= b
	with s == 2:
		o |= c
	with s == 3:
		o |= d
	with s == 4:
		o |= e

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer = sim_trace)
for cycle in range(16):
	sim.step({
		'a': random.randint(0, 7), 
		'b': random.randint(0, 7), 
		'c': random.randint(0, 7), 
		'd': random.randint(0, 7), 
		'e': random.randint(0, 7), 
		's': random.randint(0, 4)
		})


print('--- 3-bit 3:1 MUX Simulation -- Built using PyRTL\'s conditional assignments ---')
sim_trace.render_trace()