import os
from myhdl import *

mod_path = "/home/zzlee/verilog-dev/share/myhdl/cosimulation/icarus"
cmd = "iverilog -o bin2gray.o -Dwidth=%s " + \
  "bin2gray.v " + \
  "dut_bin2gray.v "

def tb(B, G):
  width = len(B)
  os.system(cmd % width)
  return Cosimulation("vvp -M %s -m myhdl bin2gray.o" % (mod_path,), B=B, G=G)

B = Signal(intbv(0)[4:]);
G = Signal(intbv(0)[4:]);
tb(
  B=B,
  G=G)