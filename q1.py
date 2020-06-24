### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# A multiplexer (or MUX) is a combinational circuit that allows binary information 
# from several input lines to be routed onto a single output line based on the
# provided "select" signals.

# For example, an 1-bit 2:1 MUX has two 1-bit data inputs: {a, b}, one 1-bit data output: o, 
# and one 1-bit input select signal: s. When s=0, input a should be routed to the MUX's 
# output line. When s=1, input b should be routed to the MUX's output line. 

# An implementation of such an 1-bit 2:1 MUX based on PyRTL's conditional assignments follows.

# Declare two 1-bit data inputs: a, b
a = pyrtl.Input(bitwidth=1, name='a')
b = pyrtl.Input(bitwidth=1, name='b') 

# Declare one 1-bit control input: s
s = pyrtl.Input(bitwidth=1, name='s')

# Declare one 1-bit output: o
o = pyrtl.Output(bitwidth=1, name='o')

# 2:1 MUX implementation using PyRTL's conditional assignment
with pyrtl.conditional_assignment:
    with s==0: # alternarively, "with ~s:"  
        o |= a
    with s==1: # alternarively, "with s:"
        o |= b 


# Print the current working block to see that in fact the generated design looks like
# the hardware we described above
print('--- 1-bit 2:1 MUX Implementation ---')
print(pyrtl.working_block())
print()

# Simulate and test the design for 8 clock cycles using random inputs
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
for cycle in range(8):
    # Call "sim.step" to simulate each clock cycle of the design
    sim.step({
        'a': random.choice([0, 1]),
        'b': random.choice([0, 1]),
        's': random.choice([0, 1])
        })

# Print the trace results to the screen.
print('--- 1-bit 2:1 MUX Simulation -- Built using PyRTL\'s conditional statement---')
sim_trace.render_trace()
