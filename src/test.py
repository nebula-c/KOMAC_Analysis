import numpy as np

def Run(self,):
    print(int(9/2))

txtfile = open('/home/suchoi/KOMAC/analysis/processed/flux/Apr_flux.txt', 'r')

while True:
    line = txtfile.readline()
    if not line: break
    
    hello = int(line)
    print(hello)
