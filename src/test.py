import numpy as np

def Run(self,):
    mypath = '/home/suchoi/KOMAC/analysis/eachdata/Apr/rowhits_origin_20220417_172913.npy'
    a = np.load(mypath)
    print(np.shape(a))