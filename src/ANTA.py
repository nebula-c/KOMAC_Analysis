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
    
    def allmaps(self,output,myhspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.__totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.__totalnpy)[0]/2)+1,2,i+1)
            plt.imshow(self.__totalnpy[i]*10,interpolation='none')#,vmin=0.1)
            # plt.xlabel('row')
            # plt.ylabel('column')
            plt.colorbar()
            plt.clim(0,200)
        plt.subplots_adjust(hspace = myhspace)
        plt.savefig(output,dpi=300)

    def allhist(self,output,myhspace=0.3,mywspace=0.1):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.__totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.__totalnpy)[0]/2)+1,2,i+1)
            dvmax = 200
            thresholds_draw = self.__totalnpy[i].ravel()*10
            plt.hist(thresholds_draw,bins=dvmax,range=(0,dvmax))
            plt.xlim(0,dvmax)
            # plt.title('Threshold: $\mu=%.2f,\ \sigma=%.2f$'%(np.nanmean(self.__totalnpy[i]*10),np.nanstd(self.__totalnpy[i]*10)))
            plt.xlabel('Threshold (DAC)')
            plt.ylabel('Pixels')

        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        plt.savefig(output,dpi=300)

    def meanthrs(self,):
        for i in range(0,np.shape(self.__totalnpy)[0]):
            thresholds = self.__totalnpy[i]
            thresholds[thresholds==0]=np.nan
            print('Threshold: %.2f +/- %.2f DAC (based on %d pixels)'%(np.nanmean(thresholds),np.nanstd(thresholds),int(np.sum(~np.isnan(thresholds)))))

        