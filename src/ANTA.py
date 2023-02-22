#!/usr/bin/env python3

#---------------------------------------------------------------------
# Analyzing Numpy-files for Threshold of ALPIDE
#---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size

import sys
import os
import itertools


class Thrs:
    totalnpy = []
    __output = ''
    __mydose_list = []
    
    def SetOutput(self,myoutput): self.__output = myoutput
    
    def pltshow(self,): plt.show()
    
    def pltsave(self, myname): 
        self.__output = myname
        plt.savefig(self.__output,dpi=300)
    
    def pltxlim(self,min,max):
        plt.xlim(min,max)
    
    def pltylim(self,min,max):
        plt.ylim(min,max)
    
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
        
    def resetdoselist(self,):
        self.__mydose_list = []

    ### print shape of numpy
    def printshape(self,):
        print(np.shape(self.totalnpy))
    
    ### Load All data @ 0krad
    def SetAllMonthsData(self,):
        exp_path=[
                  "processed/totalnpy/Apr_threshold_origin_total.npy",
                  "processed/totalnpy/Jun_threshold_origin_total.npy",
                  "processed/totalnpy/Jul_RPI_threshold_origin_total.npy",
                  "processed/totalnpy/Jul_RAS_threshold_origin_total.npy",
                  "processed/totalnpy/Sep_threshold_origin_total.npy",
                  "processed/totalnpy/Nov_threshold_origin_total.npy"
                    ]
        totaExpNum = np.shape(exp_path)[0]
        
        mine=[]
        for i in range(0,totaExpNum):
            tempnpy = np.load(exp_path[i])
            mine.append(tempnpy[0])
        self.totalnpy = np.array(mine)
    
    ### print all maps of threshold npy
    def allmaps(self,myhspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.totalnpy)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.totalnpy)[0]/2),2,i+1)
            plt.imshow(self.totalnpy[i]*10,interpolation='none')#,vmin=0.1)
            # plt.xlabel('row')
            # plt.ylabel('column')
            plt.colorbar()
            # plt.clim(0,1)
            plt.clim(0,200)
            print(1024*512 - np.count_nonzero(~np.isnan(self.totalnpy[i]*10)))
        plt.subplots_adjust(hspace = myhspace)
        # plt.savefig(self.__output,dpi=300)
    
    ### print all maps of threshold npy
    def OneMap(self,ith,myhspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
        ax = plt.axes()
        im = plt.imshow(self.totalnpy[ith]*10,interpolation='none')#,vmin=0.1)
        plt.xlabel('row')
        plt.ylabel('column')
        self.SetCbar(ax,im)
        # plt.colorbar()
        # plt.clim(0,1)
        plt.clim(0,200)
        print(1024*512 - np.count_nonzero(~np.isnan(self.totalnpy[ith]*10)))
        
    ### print all maps of threshold npy
    def OneMap_OneNpy(self,myhspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
        ax = plt.axes()
        im = plt.imshow(self.totalnpy*10,interpolation='none')#,vmin=0.1)
        plt.xlabel('row')
        plt.ylabel('column')
        self.SetCbar(ax,im)
        # plt.colorbar()
        # plt.clim(0,1)
        plt.clim(0,200)
        
    def SetCbar(self, myax, myim):
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(myax)
        width = axes_size.AxesY(myax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        plt.colorbar(myim,cax=cax)
        # plt.clim(-30,30)
        # plt.clim(0,30)


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
        # plt.savefig(output,dpi=300)

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
                meanthrs.append(np.nanmean(self.totalnpy[i][j])*10)
            
            plt.scatter(range(0,512),meanthrs,s=.1)
            meanthrs_chip = np.nanmean(meanthrs)
            
            plt.xlim(0,512)
            # self.ShowPadY()
            plt.ylim(meanthrs_chip-15,meanthrs_chip+15)
            plt.xticks([0,100,200,300,400,500])
            
            plt.xlabel('row')
            plt.ylabel('threshold')
            # break
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        # plt.savefig(self.__output,dpi=300)
        
        
    ### Print theshold projection for X
    def projectionX(self,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.totalnpy)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.totalnpy)[0]/2)+1,2,i+1)
            meanthrs = list()
            
            for j in range(0,1024):
                meanthrs.append(np.nanmean(self.totalnpy[i,:,j])*10)
                
            plt.scatter(range(0,1024),meanthrs,s=.1)
            meanthrs_chip = np.nanmean(meanthrs)
                
            plt.xlim(0,512)
            self.ShowPadX()
            plt.ylim(meanthrs_chip-15,meanthrs_chip+15)
            plt.xticks([0,256,512,768,1024])
            
            
            plt.xlabel('column')
            plt.ylabel('threshold')
            # break
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        # plt.savefig(self.__output,dpi=300)
        
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
        # plt.savefig(self.__output,dpi=300)
    
    
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

        # plt.savefig('hl.png')
    
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
        # plt.savefig(self.__output)
        
    def testfunction(self,):
        print("Hello, It is testfunction from ANTA.py")
        
    ### I made SetAllMonthsData function, so it is not need anymore
    def All0kradThrsProj(self,myaxis="X",myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
        # plt.figure(1,figsize=(5,7),facecolor='white')
        
        exp_path=[
                  "processed/totalnpy/Apr_threshold_origin_total.npy",
                  "processed/totalnpy/Jun_threshold_origin_total.npy",
                  "processed/totalnpy/Jul_RPI_threshold_origin_total.npy",
                  "processed/totalnpy/Jul_RAS_threshold_origin_total.npy",
                  "processed/totalnpy/Sep_threshold_origin_total.npy",
                  "processed/totalnpy/Nov_threshold_origin_total.npy"
                    ]
        totaExpNum = np.shape(exp_path)[0]
        
        for i in range(0,totaExpNum):
            plt.figure(1).add_subplot(totaExpNum/2,2,i+1)
            # i=5
            self.load(exp_path[i])
            
            meanthrs = list()

            if myaxis == "Y":
                for j in range(0,512):
                    meanthrs.append(np.nanmean(self.totalnpy[0][j])*10)    

                plt.scatter(range(0,512),meanthrs,s=.1)
                plt.xticks([0,100,200,300,400,500])
                meanthrs_chip = np.nanmean(meanthrs)
                
                plt.xlim(0,512)
                self.ShowPadY()
                plt.ylim(meanthrs_chip-15,meanthrs_chip+15)
                plt.xlabel('row')
                plt.ylabel('threshold')
            
            if myaxis == "X":
                for j in range(0,1024):
                    meanthrs.append(np.nanmean(self.totalnpy[0,:,j])*10)
                
                ### Color distribution
                ###------------------------------------------------------
                # for j in range(0,1024):
                #     mod = j%4
                #     if mod == 0:
                #         plt.scatter(j,meanthrs[j],s=.3,color="red")
                #     if mod == 1:
                #         plt.scatter(j,meanthrs[j],s=.3,color="green")
                #     if mod == 2:
                #         plt.scatter(j,meanthrs[j],s=.3,color="orange")
                #     if mod == 3:
                #         plt.scatter(j,meanthrs[j],s=.3,color="blue")
                ###------------------------------------------------------
                
                plt.scatter(range(0,1024),meanthrs,s=.1)
                plt.xticks([0,256,512,768,1024])
                meanthrs_chip = np.nanmean(meanthrs)
                
                plt.xlim(0,1024)
                self.ShowPadX()
                plt.ylim(meanthrs_chip-15,meanthrs_chip+15)
                plt.xlabel('column')
                plt.ylabel('threshold')

            # break
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        # plt.savefig(self.__output,dpi=300)
        
    def ShowPadY_Map(self,):
        plt.imshow(self.totalnpy[0]*10,interpolation='none')
        
        p1_i = 10;p1_f = 25;p2_i = 35;p2_f = 50;p3_i = 120;p3_f = 135;p4_i = 180;p4_f = 195;p5_i = 255;p5_f = 270
        
        plt.plot([0,1023],  [p1_i,p1_i],    color='red',linewidth=1)
        plt.plot([0,1023],  [p1_f,p1_f],    color='red',linewidth=1)
        plt.plot([0,1023],  [p2_i,p2_i],    color='red',linewidth=1)
        plt.plot([0,1023],  [p2_f,p2_f],    color='red',linewidth=1)
        plt.plot([0,1023],  [p3_i,p3_i],    color='red',linewidth=1)
        plt.plot([0,1023],  [p3_f,p3_f],    color='red',linewidth=1)
        plt.plot([0,1023],  [p4_i,p4_i],    color='red',linewidth=1)
        plt.plot([0,1023],  [p4_f,p4_f],    color='red',linewidth=1)
        plt.plot([0,1023],  [p5_i,p5_i],    color='red',linewidth=1)
        plt.plot([0,1023],  [p5_f,p5_f],    color='red',linewidth=1)
    
    def ShowPadX_Map(self,):
        plt.imshow(self.totalnpy[0]*10,interpolation='none')
        
        pad_size = 15
        pad_width = 48
        p1_i = 65; p1_f = p1_i + pad_size; p2_i = p1_f + pad_width; p2_f = p2_i + pad_size; p3_i = p2_f + pad_width; p3_f = p3_i + pad_size; p4_i = p3_f + pad_width; p4_f = p4_i + pad_size; p5_i = p4_f + pad_width; p5_f = p5_i + pad_size; p6_i = p5_f + pad_width; p6_f = p6_i + pad_size; p7_i = p6_f + pad_width; p7_f = p7_i + pad_size; p8_i = p7_f + pad_width; p8_f = p8_i + pad_size; p9_i = p8_f + pad_width; p9_f = p9_i + pad_size; p10_i = p9_f  + pad_width; p10_f = p10_i+ pad_size; p11_i = p10_f + pad_width; p11_f = p11_i+ pad_size; p12_i = p11_f + pad_width; p12_f = p12_i+ pad_size; p13_i = p12_f + pad_width; p13_f = p13_i+ pad_size; p14_i = p13_f + pad_width; p14_f = p14_i+ pad_size; p15_i = p14_f + pad_width; p15_f = p15_i+ pad_size
        
        plt.plot([p1_i ,p1_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p1_f ,p1_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p2_i ,p2_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p2_f ,p2_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p3_i ,p3_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p3_f ,p3_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p4_i ,p4_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p4_f ,p4_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p5_i ,p5_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p5_f ,p5_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p6_i ,p6_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p6_f ,p6_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p7_i ,p7_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p7_f ,p7_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p8_i ,p8_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p8_f ,p8_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p9_i ,p9_i ],   [0,511],  color='red',linewidth=1)
        plt.plot([p9_f ,p9_f ],   [0,511],  color='red',linewidth=1)
        plt.plot([p10_i,p10_i],   [0,511],  color='red',linewidth=1)
        plt.plot([p10_f,p10_f],   [0,511],  color='red',linewidth=1)
        plt.plot([p11_i,p11_i],   [0,511],  color='red',linewidth=1)
        plt.plot([p11_f,p11_f],   [0,511],  color='red',linewidth=1)
        plt.plot([p12_i,p12_i],   [0,511],  color='red',linewidth=1)
        plt.plot([p12_f,p12_f],   [0,511],  color='red',linewidth=1)
        plt.plot([p13_i,p13_i],   [0,511],  color='red',linewidth=1)
        plt.plot([p13_f,p13_f],   [0,511],  color='red',linewidth=1)
        plt.plot([p14_i,p14_i],   [0,511],  color='red',linewidth=1)
        plt.plot([p14_f,p14_f],   [0,511],  color='red',linewidth=1)
        plt.plot([p15_i,p15_i],   [0,511],  color='red',linewidth=1)
        plt.plot([p15_f,p15_f],   [0,511],  color='red',linewidth=1)
    
    def ShowPadX(self,):
        mylinewidth = .5
        
        pad_size = 15
        pad_width = 48
        p1_i = 65; p1_f = p1_i + pad_size; p2_i = p1_f + pad_width; p2_f = p2_i + pad_size; p3_i = p2_f + pad_width; p3_f = p3_i + pad_size; p4_i = p3_f + pad_width; p4_f = p4_i + pad_size; p5_i = p4_f + pad_width; p5_f = p5_i + pad_size; p6_i = p5_f + pad_width; p6_f = p6_i + pad_size; p7_i = p6_f + pad_width; p7_f = p7_i + pad_size; p8_i = p7_f + pad_width; p8_f = p8_i + pad_size; p9_i = p8_f + pad_width; p9_f = p9_i + pad_size; p10_i = p9_f  + pad_width; p10_f = p10_i+ pad_size; p11_i = p10_f + pad_width; p11_f = p11_i+ pad_size; p12_i = p11_f + pad_width; p12_f = p12_i+ pad_size; p13_i = p12_f + pad_width; p13_f = p13_i+ pad_size; p14_i = p13_f + pad_width; p14_f = p14_i+ pad_size; p15_i = p14_f + pad_width; p15_f = p15_i+ pad_size
        
        plt.plot([p1_i ,p1_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p1_f ,p1_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p2_i ,p2_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p2_f ,p2_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p3_i ,p3_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p3_f ,p3_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p4_i ,p4_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p4_f ,p4_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p5_i ,p5_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p5_f ,p5_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p6_i ,p6_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p6_f ,p6_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p7_i ,p7_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p7_f ,p7_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p8_i ,p8_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p8_f ,p8_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p9_i ,p9_i ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p9_f ,p9_f ],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p10_i,p10_i],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p10_f,p10_f],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p11_i,p11_i],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p11_f,p11_f],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p12_i,p12_i],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p12_f,p12_f],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p13_i,p13_i],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p13_f,p13_f],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p14_i,p14_i],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p14_f,p14_f],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p15_i,p15_i],   [0,511],  color='red',linewidth=mylinewidth)
        plt.plot([p15_f,p15_f],   [0,511],  color='red',linewidth=mylinewidth)
        
    def ShowPadY(self,):
        mylinewidth = .5
        
        p1_i = 10;p1_f = 25;p2_i = 35;p2_f = 50;p3_i = 120;p3_f = 135;p4_i = 180;p4_f = 195;p5_i = 255;p5_f = 270
        
        plt.plot([p1_i,p1_i],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p1_f,p1_f],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p2_i,p2_i],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p2_f,p2_f],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p3_i,p3_i],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p3_f,p3_f],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p4_i,p4_i],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p4_f,p4_f],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p5_i,p5_i],    [0,1023],  color='red',linewidth=mylinewidth)
        plt.plot([p5_f,p5_f],    [0,1023],  color='red',linewidth=mylinewidth)
    
    def OddEvenRowThrs_projX(self,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
        
        self.SetAllMonthsData()
        
        for i in range(0,np.shape(self.totalnpy)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.totalnpy)[0]/2),2,i+1)
            meanthrs_odd = list()
            meanthrs_even = list()
            
            for j in range(0,1024):
                if j%2 == 0:
                    meanthrs_even.append(np.nanmean(self.totalnpy[i,:,j])*10)
                else :
                    meanthrs_odd.append(np.nanmean(self.totalnpy[i,:,j])*10)
                    
            plt.scatter(range(0,1024,2),meanthrs_even,s=.1,color='red')
            plt.scatter(range(1,1024,2),meanthrs_odd,s=.1,color='blue')
            meanthrs_chip = np.nanmean(meanthrs_even + meanthrs_odd)
                
            plt.xlim(0,512)
            self.ShowPadX()
            plt.ylim(meanthrs_chip-15,meanthrs_chip+15)
            plt.xticks([0,256,512,768,1024])
            
            
            plt.xlabel('column')
            plt.ylabel('threshold')
            # break
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        
    def OddEvenRowThrs(self,myhspace=0.5,mywspace=0.3,mymarkersize=1.,isall=False):
        plt.figure(1,figsize=(7,9),facecolor='white')
        
        meanthrs_all = list()
        meanthrs_odd_all = list()
        meanthrs_even_all = list()

        for i in range(0,np.shape(self.totalnpy)[0]):
            meanthrs_odd_one_chip = list()
            meanthrs_even_one_chip = list()
            
            meanthrs_all.append(np.nanmean(self.totalnpy[i,:,:]*10))
            for j in range(0,1024):
                if j%2 == 0:
                    meanthrs_even_one_chip.append(np.nanmean(self.totalnpy[i,:,j])*10)
                else :
                    meanthrs_odd_one_chip.append(np.nanmean(self.totalnpy[i,:,j])*10)
                    
            meanthrs_odd_all.append(np.nanmean(meanthrs_odd_one_chip))
            meanthrs_even_all.append(np.nanmean(meanthrs_even_one_chip))
            
        
        # print(self.__mydose_list)
        # print(meanthrs_even_all)
        if isall:
            plt.plot(self.__mydose_list,meanthrs_all,color='green',marker='o',markersize=mymarkersize,label="All")
        plt.plot(self.__mydose_list,meanthrs_even_all,color='red',marker='o',markersize=mymarkersize,label="Even")
        plt.plot(self.__mydose_list,meanthrs_odd_all,color='blue',marker='o',markersize=mymarkersize,label="Odd")
        
        
        meanthrs_chip = np.nanmean(meanthrs_even_all + meanthrs_odd_all)
        
        plt.ylim(meanthrs_chip-30,meanthrs_chip+30)
        plt.legend()
        
        plt.xlabel('dose')
        plt.ylabel('threshold')


        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        
        
    def OddEvenRowThrs_all(self,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        exp_path=[
                  "processed/totalnpy/Apr_threshold_revision_total.npy",
                  "processed/totalnpy/Jun_threshold_revision_total.npy",
                  "processed/totalnpy/Jul_RPI_threshold_revision_total.npy",
                  "processed/totalnpy/Jul_RAS_threshold_revision_total.npy",
                  "processed/totalnpy/Sep_threshold_revision_total.npy",
                  "processed/totalnpy/Nov_threshold_revision_total.npy"
                    ]
        
        dose_path=[
                  "doseinfo/Apr_dose.txt",
                  "doseinfo/Jun_dose.txt",
                  "doseinfo/Jul_sepe_dose.txt",
                  "doseinfo/Jul_cont_dose.txt",
                  "doseinfo/Sep_dose.txt",
                  "doseinfo/Nov_dose.txt"
                    ]
        
        totaExpNum = np.shape(exp_path)[0]
        
        
        for i in range(0,totaExpNum):
            self.load(exp_path[i])
            self.loaddose(dose_path[i])
            print("{}th exp".format(i+1))
            ax = plt.figure(1).add_subplot(totaExpNum/2,2,i+1)
            self.OddEvenRowThrs(isall=True)
            self.resetdoselist()
            
    def Sub_FHR_Thrs(self,myhitmappath,mythrspath,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
        
        hitmap_npy_path = myhitmappath
        thrs_npy_path = mythrspath
        
        myhitmapnpy = np.load(hitmap_npy_path)
        mythrsnpy = np.load(thrs_npy_path)
        
        bool_hitmap = np.where(myhitmapnpy>0,1,0)
        bool_thrs = np.where(mythrsnpy>0,1,0)
        
        # for i in range(0,512):
        #     for j in range(0,1024):
        #         if bool_thrs[i,j] != 0 and bool_thrs[i,j] !=1 :
        #             print("hello")
        
        nullnpy = 1 - bool_thrs
        subnpy = bool_hitmap - nullnpy
        # subnpy = nullnpy
        # xornpy = np.logical_xor(bool_hitmap,nullnpy)
        
        ax = plt.axes()
        im = plt.imshow(subnpy,cmap="viridis",interpolation='none')
        # im = plt.imshow(xornpy,cmap="viridis",interpolation='none')
        # im = plt.imshow(bool_hitmap,cmap="Reds",interpolation='none')
        # im = plt.imshow(nullnpy,cmap="Blues",interpolation='none')
        self.SetCbar(ax,im)
        # plt.clim(0,10)