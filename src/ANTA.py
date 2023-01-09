#!/usr/bin/env python3

#---------------------------------------------------------------------
# Analyzing Numpy-files for Threshold of ALPIDE
#---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

import sys
import os


class Thrs:
    totalnpy = []
    __output = ''
    __mydose_list = []
    
    def SetOutput(self,myoutput): self.__output = myoutput
    
    ### load npy file 
    def load(self, path):
        self.totalnpy = np.load(path)
    
    ### load Dose file 
    def loaddose(self,target):
        f = open(target,'r')
        while True:
            line = f.readline()
            line = line.strip()
            if not line: break
            # print(line)
            self.__mydose_list.append(float(line))
        f.close()

    ### print shape of numpy
    def printshape(self,):
        print(np.shape(self.totalnpy))
    
    ### print all maps of threshold npy
    def allmaps(self,myhspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.totalnpy)[0]/2)+1,2,i+1)
            plt.imshow(self.totalnpy[i]*10,interpolation='none')#,vmin=0.1)
            # plt.xlabel('row')
            # plt.ylabel('column')
            plt.colorbar()
            # plt.clim(0,1)
            plt.clim(0,200)
        plt.subplots_adjust(hspace = myhspace)
        plt.savefig(self.__output,dpi=300)


    ### pring all histogram of threshold npy
    def allhist(self,output,myhspace=0.3,mywspace=0.1):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.totalnpy)[0]/2)+1,2,i+1)
            dvmax = 200
            thresholds_draw = self.totalnpy[i].ravel()*10
            plt.hist(thresholds_draw,bins=dvmax,range=(0,dvmax))
            plt.xlim(0,dvmax)
            # plt.title('Threshold: $\mu=%.2f,\ \sigma=%.2f$'%(np.nanmean(self.totalnpy[i]*10),np.nanstd(self.totalnpy[i]*10)))
            plt.xlabel('Threshold (DAC)')
            plt.ylabel('Pixels')

        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        plt.savefig(output,dpi=300)

    ### print mean of threshold
    def meanthrs(self,):
        for i in range(0,np.shape(self.totalnpy)[0]):
            thresholds = self.totalnpy[i]
            thresholds[thresholds==0]=np.nan
            print('Threshold: %.2f +/- %.2f DAC (based on %d pixels)'%(np.nanmean(thresholds),np.nanstd(thresholds),int(np.sum(~np.isnan(thresholds)))))

    ### Save means of thoreshold as text file
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

    ### Print theshold projection for Y
    def projectionY(self,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.totalnpy)[0]/2)+1,2,i+1)
            meanthrs = list()
            
            for j in range(0,512):
                print(np.nanmean(self.totalnpy[i][j]))
                meanthrs.append(np.nanmean(self.totalnpy[i][j])*10)
            print(i)
            plt.plot(range(0,512),meanthrs)
            plt.xticks([0,100,200,300,400,500])
            
            plt.xlim(0,512)
            plt.ylim(70,160)
            plt.xlabel('row')
            plt.ylabel('#')
            # break
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        plt.savefig(self.__output,dpi=300)
        
        
    ### Print theshold projection for X
    def projectionX(self,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.totalnpy)[0]/2)+1,2,i+1)
            meanthrs = list()
            
            for j in range(0,1024):
                print(np.nanmean(self.totalnpy[i,:,j]))
                meanthrs.append(np.nanmean(self.totalnpy[i,:,j])*10)
            print(i)
            plt.plot(range(0,512),meanthrs)
            plt.xticks([0,100,200,300,400,500])
            
            plt.xlim(0,1024)
            plt.ylim(70,160)
            plt.xlabel('row')
            plt.ylabel('#')
            # break
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        plt.savefig(self.__output,dpi=300)
        
    ### Make revision of origin npy file
    def recoverdosehisto(self,):
        plt.figure(1,figsize=(7,9),facecolor='white')
        
        recoverdose_list = []
        for x in range(0,512):
            for y in range(0,1024):
                originthrs = self.totalnpy[0][x][y]
                for i in range(1,np.shape(self.totalnpy)[0]):
                    val = self.totalnpy[i][x][y]
                    if val <= originthrs:
                        recoverdose_list.append(i)
                        break
        counts, bins, bars = plt.hist(recoverdose_list,range(np.shape(self.totalnpy)[0]))
        plt.grid(True)
        plt.title('Total Entry : {}({:.2f}%)'.format(round(sum(counts)),100*round(sum(counts))/(1024*512)))
        plt.savefig(self.__output,dpi=300)
    
    
    ### High and low threshold pixels(1 sigma)
    def highlowThrs(self,):
        plt.figure(1,figsize=(7,9),facecolor='white')
        
        highpixel = []
        lowpixel = []
        
        # print(np.shape(self.totalnpy[0]>np.nanmean(self.totalnpy[0])))
        # highpixel.append(self.totalnpy[self.totalnpy[0]>np.nanmean(self.totalnpy[0]),:])
        mymean = np.nanmean(self.totalnpy[0])
        mystd = np.nanstd(self.totalnpy[0])
        for x in range(0,512):
            for y in range(0,1024):
                originthrs = self.totalnpy[0][x][y]
                if originthrs > mymean + mystd*2:
                    highpixel.append(self.totalnpy[:,x,y].copy())
                if originthrs < mymean - mystd*2:
                    lowpixel.append(self.totalnpy[:,x,y].copy())
            print(x)
        # print(np.shape(highpixel))
        
        highpixel = np.array(highpixel).swapaxes(0,1)
        lowpixel = np.array(lowpixel).swapaxes(0,1)
        
        highthrs = []
        lowthrs = []
        for i in range(0,np.shape(self.totalnpy)[0]):
            highthrs.append(np.nanmean(highpixel[i])*10)
            lowthrs.append(np.nanmean(lowpixel[i])*10)
            
        print(highthrs)
        print(lowthrs)
        plt.plot(highthrs)
        plt.plot(lowthrs)
        sub = np.subtract(highthrs,lowthrs)
        plt.plot(sub)

        plt.savefig('hl.png')
    
    ### Pring number of null pixels
    def numNull(self,mytitle=""):
        plt.figure(1,figsize=(7,4),facecolor='white')
        total_null_list = []
        for ithr in range(0,np.shape(self.totalnpy)[0]):
            numNull_total = 0
            for x in range(0,512):
                for y in range(0,1024):
                    # if self.totalnpy[ithr][x][y] == 0:
                    if np.isnan(self.totalnpy[ithr][x][y]):
                        numNull_total += 1
            
            print(numNull_total)
            total_null_list.append(numNull_total)
        plt.plot(self.__mydose_list,total_null_list,'o-')
        plt.xlabel("dose(krad)")
        plt.ylabel("# of Null Pixels")
        plt.title(mytitle)
        plt.savefig(self.__output)
        
    def testfunction(self,):
        print("Hello, It is testfunction from ANTA.py")