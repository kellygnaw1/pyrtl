import pyrtl 

rf = pyrtl.MemBlock(bitwidth=32, addrwidth=5, name='rf')
instr = pyrtl.Input(bitwidth=32, name='instr')

#fields for R-type
op = pyrtl.WireVector(bitwidth=6, name='op')
rs = pyrtl.WireVector(bitwidth=5, name='rs')
rt = pyrtl.WireVector(bitwidth=5, name='rt')
rd = pyrtl.WireVector(bitwidth=5, name='rd')
sh = pyrtl.WireVector(bitwidth=5, name='sh')
func = pyrtl.WireVector(bitwidth=6, name='func')

op <<= instr[26:32]
rs <<= instr[21:26]
rt <<= instr[16:21]
rd <<= instr[11:16]
sh <<= instr[6:11]
func <<= instr[0:6]

alu_out = pyrtl.WireVector(bitwidth=32, name='alu_out')
data0 = pyrtl.WireVector(bitwidth=32, name='data0')
data1 = pyrtl.WireVector(bitwidth=32, name='data1')

data0 <<= rf[rs]
data1 <<= rf[rt]

with pyrtl.conditional_assignment:
	#ADD, SUB, AND, OR, XOR, SLL, SRL, SRA, SLT (respectively)
	with func == 0x20:		
		alu_out |= data0 + data1

	with func == 0x22: 		
		alu_out |= data0 - data1

	with func == 0x24:		
		alu_out |= data0 & data1

	with func == 0x25:	
		alu_out |= data0 | data1

	with func == 0x26:		
		alu_out |= data0 ^ data1

	with func == 0x00: 		
		alu_out |= pyrtl.corecircuits.shift_left_logical(data1, sh)

	with func == 0x02: 		
		alu_out |= pyrtl.corecircuits.shift_right_logical(data1, sh)

	with func == 0x03: 		
		alu_out |= pyrtl.corecircuits.shift_right_arithmetic(data1, sh)

	with func == 0x2A: 		
		alu_out |= ((data0 - data1) > 0)

rf[rd] <<= alu_out