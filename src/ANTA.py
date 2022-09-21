#!/usr/bin/env python3

#---------------------------------------------------------------------
# Analyzing Numpy-files for Threshold of ALPIDE
#---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

import sys
import os


class Thrs:
    __totalnpy = []
    
    def load(self, path):
        self.__totalnpy = np.load(path)
    
    def printshape(self,):
        print(np.shape(self.__totalnpy))
    
    def testshow(self,):
        plt.figure(1,figsize=(10,8),facecolor='white')
    
        for i in range(0,np.shape(self.__totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.__totalnpy)[0]/2)+1,2,i+1)
            plt.imshow(self.__totalnpy[i],interpolation='none')#,vmin=0.1)
            plt.xlabel('row')
            plt.ylabel('column')
        plt.subplots_adjust(hspace = 0.3)
        plt.colorbar()
        plt.savefig("./temp.png",dpi=300)