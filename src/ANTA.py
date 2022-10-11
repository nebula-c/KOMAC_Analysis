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
    __output = ''
    
    def SetOutput(self,myoutput): self.__output = myoutput
    
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
            plt.clim(0,1)
            # plt.clim(0,200)
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

    def savemeanastxt(self,filepath):
        txtfile = open(filepath, 'r')
        filename = filepath.split('/')[len(filepath.split('/'))-1]
        
        os.system("mkdir datainfo")
        newfile = open("./datainfo/{}".format(filename), 'w')
        newfile.write('mean,noise\n')


        while True:
            line = txtfile.readline()
            if not line: break
            
            word = line.split(' ')
            newfile.write('{},{}\n'.format(word[1],word[3]))


        txtfile.close()
        newfile.close()

    def projectionY(self,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.__totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.__totalnpy)[0]/2)+1,2,i+1)
            meanthrs = list()
            
            for j in range(0,512):
                meanthrs.append(np.sum(self.__totalnpy[i][j]))
            
            plt.plot(range(0,512),meanthrs)
            
            
            plt.xlim(0,512)
            plt.ylim(0.1024)
            plt.xlabel('row')
            plt.ylabel('#')
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        plt.savefig(self.__output,dpi=300)
        
    def recoverdosehisto(self,):
        plt.figure(1,figsize=(7,9),facecolor='white')
        
        recoverdose_list = []
        for x in range(0,512):
            for y in range(0,1024):
                originthrs = self.__totalnpy[0][x][y]
                for i in range(1,np.shape(self.__totalnpy)[0]):
                    val = self.__totalnpy[i][x][y]
                    if val <= originthrs:
                        recoverdose_list.append(i)
                        break
        counts, bins, bars = plt.hist(recoverdose_list,range(np.shape(self.__totalnpy)[0]))
        plt.grid(True)
        plt.title('Total Entry : {}({:.2f}%)'.format(round(sum(counts)),100*round(sum(counts))/(1024*512)))
        plt.savefig(self.__output,dpi=300)
    
    def highlowThrs(self,):
        plt.figure(1,figsize=(7,9),facecolor='white')
        
        highpixel = []
        lowpixel = []
        
        # print(np.shape(self.__totalnpy[0]>np.nanmean(self.__totalnpy[0])))
        # highpixel.append(self.__totalnpy[self.__totalnpy[0]>np.nanmean(self.__totalnpy[0]),:])
        mymean = np.nanmean(self.__totalnpy[0])
        mystd = np.nanstd(self.__totalnpy[0])
        for x in range(0,512):
            for y in range(0,1024):
                originthrs = self.__totalnpy[0][x][y]
                if originthrs > mymean + mystd*2:
                    highpixel.append(self.__totalnpy[:,x,y].copy())
                if originthrs < mymean - mystd*2:
                    lowpixel.append(self.__totalnpy[:,x,y].copy())
            print(x)
        # print(np.shape(highpixel))
        
        highpixel = np.array(highpixel).swapaxes(0,1)
        lowpixel = np.array(lowpixel).swapaxes(0,1)
        
        highthrs = []
        lowthrs = []
        for i in range(0,np.shape(self.__totalnpy)[0]):
            highthrs.append(np.nanmean(highpixel[i])*10)
            lowthrs.append(np.nanmean(lowpixel[i])*10)
            
        print(highthrs)
        print(lowthrs)
        plt.plot(highthrs)
        plt.plot(lowthrs)
        sub = np.subtract(highthrs,lowthrs)
        plt.plot(sub)

        plt.savefig('hl.png')

class Rowhits:
    __totalrowhits = []
    __output = ''
    
    def SetOutput(self,myoutput): self.__output = myoutput
    
    def load(self, path):
        self.__totalrowhits = np.load(path)
        
                    