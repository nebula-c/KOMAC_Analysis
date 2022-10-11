import numpy as np
import matplotlib.pyplot as plt

def Run():
    # print("Hello")
    a = [1,2,2,2,2,2,4,5,6,7,8,3,3,3,3]
    plt.hist(a)
    plt.grid(True)
    plt.savefig("hereis.png")
# # txtfile = open('/home/suchoi/KOMAC/analysis/processed/flux/Apr_flux.txt', 'r')

# while True:
#     line = txtfile.readline()
#     if not line: break
    
#     hello = int(line)
#     print(hello)
