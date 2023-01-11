#!/usr/bin/env python3

#---------------------------------------------------------------------
# Specific analysis on Numpy
#---------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size

import sys
import os
import copy

class MapCtrl:
    def __init__(self,):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
    class PartialMap:
        OriginMap = []
        PartialMap = []
        RemovedValMap = []
        
        xmin = 0
        xmax = 1024
        ymin = 0
        ymax = 512
        
        ### test function
        def sayhi(self,):
            print("hi")
            
        def SetLangeMap(self,xmin,xmax,ymin,ymax):
            self.xmin = xmin
            self.xmax = xmax
            self.ymin = ymin
            self.ymax = ymax
            self.PartialMap = copy.deepcopy(self.OriginMap[self.ymin:self.ymax,self.xmin:self.xmax])
        
        def ShowPart(self,):
            # print(self.OriginMap)
            plt.hlines(self.ymin, self.xmin, self.xmax, color='red', linestyle='solid', linewidth=3)
            plt.hlines(self.ymax, self.xmin, self.xmax, color='red', linestyle='solid', linewidth=3)
            plt.vlines(self.xmin, self.ymin, self.ymax, color='red', linestyle='solid', linewidth=3)
            plt.vlines(self.xmax, self.ymin, self.ymax, color='red', linestyle='solid', linewidth=3)
            plt.imshow(self.OriginMap)
        
        def ShowPart_rowhits(self,):
            self.RemovedValMap =  copy.deepcopy(self.OriginMap[:,:,20])
            # print(self.OriginMap)
            plt.hlines(self.ymin, self.xmin, self.xmax, color='red', linestyle='solid', linewidth=3)
            plt.hlines(self.ymax, self.xmin, self.xmax, color='red', linestyle='solid', linewidth=3)
            plt.vlines(self.xmin, self.ymin, self.ymax, color='red', linestyle='solid', linewidth=3)
            plt.vlines(self.xmax, self.ymin, self.ymax, color='red', linestyle='solid', linewidth=3)
            plt.imshow(self.RemovedValMap)
        
        def SetPCBRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 145
            x11 = 150
            x2 = 257
            x22 = 300
            x3 = 420
            x33 = 427
            
            y11 = 512 - 200 - 10
            y12 = 512 - 200 + 10
            y13 = 512 - 200 + 10
            y14 = 512 - 200 - 10
            y2  = 512 - 456
            y22 = 512 - 456
            
            plt.plot([x11,x3],  [y12,y13],  color='red',linewidth=1)
            plt.plot([x3,x33],  [y13,y14] , color='red',linewidth=1)
            plt.plot([x33,x22], [y14,y22],  color='red',linewidth=1)
            plt.plot([x22,x2],  [y22,y2] ,  color='red',linewidth=1)
            plt.plot([x2,x1],   [y2,y11] ,  color='red',linewidth=1)
            plt.plot([x1,x11],  [y11,y12],  color='red',linewidth=1)
            
        def SetKaptonRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 679
            x2 = 1024
            x3 = 1024
            x4 = 679
            
            y1 = 429
            y2 = 429
            y3 = 512 - 512
            y4 = 512 - 512
            
            
            plt.plot([x1,x2],   [y1,y2],    color='red',linewidth=1)
            plt.plot([x2,x3],   [y2,y3],    color='red',linewidth=1)
            plt.plot([x3,x4],   [y3,y4],    color='red',linewidth=1)
            plt.plot([x4,x1],   [y4,y1],    color='red',linewidth=1)
            
        
        
    myPM = PartialMap()
        
    __totalmap = []
    __onemap = []
    __output = 'test'
    __path = ''

    def pltshow(self,): plt.show()
    
    def pltsave(self, myname): 
        self.__output = myname
        plt.savefig(self.__output,dpi=300)
        
    def SetOutput(self,myoutput): 
        self.__output = myoutput
    
    def loadtotalmap(self, path):
        self.__path = path
        self.__totalmap = np.load(self.__path)
    
    def loadonemap(self, ith):
        self.__onemap = self.__totalmap[ith]
        self.myPM.OriginMap = copy.deepcopy(self.__onemap)
    
    def loadonemoremap(self, ith):
        self.__onemap = self.__onemap[ith]
        self.myPM.OriginMap = copy.deepcopy(self.__onemap)
    
    def printOneMap(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        plt.imshow(self.__onemap)
        plt.savefig(self.__output,dpi=300)
        
    def printRegion(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        self.myPM.ShowPart()
        # plt.imshow(self.myPM.PartialMap)
        plt.savefig(self.__output,dpi=300)
    
    def printPartial(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        plt.imshow(self.myPM.PartialMap)
        plt.savefig(self.__output,dpi=300)

    def printPartialRowhits(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        # plt.imshow(self.myPM.PartialMap)
        # plt.imshow(self.myPM.PartialMap[:,:,20])
        self.myPM.ShowPart_rowhits()
        plt.savefig(self.__output,dpi=300)

    def Slice(self,myxmin,myxmax,myymin,myymax):
        self.myPM.SetLangeMap(myxmin,myxmax,myymin,myymax)
        # self.myPM.ShowPart()
        # plt.savefig(self.__output,dpi=300)
    
    def InputSubplot(self, myax, myimage):
        im = plt.imshow(myimage,interpolation='none')
        
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(myax)
        width = axes_size.AxesY(myax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        plt.colorbar(cax=cax)
        plt.clim(0,200)
        
    def CountNull(self,):
        mycount = 0
        print(np.shape(self.myPM.PartialMap))
        for x in range(self.myPM.xmin,self.myPM.xmax):
            for y in range(self.myPM.ymin,self.myPM.ymax):
                if np.isnan(self.myPM.OriginMap[y,x]):
                    mycount += 1
        print(mycount)
    
    def AllPartCountNull(self,myxmin,myxmax,myymin,myymax):
        for i in range(0,np.shape(self.__totalmap)[0]):
            self.loadonemap(i)
            self.Slice(myxmin,myxmax,myymin,myymax)
            self.CountNull()
    
    def ShowPCBPart(self,):
        self.myPM.ShowPCB()
    
    def ShowAllPCB(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        
        for i in range(0,np.shape(self.__totalmap)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.__totalmap)[0]/2)+1,2,i+1)
            plt.subplots_adjust(wspace = .35)
            self.loadonemap(i)
            self.myPM.SetPCBRegion()
            self.InputSubplot(ax,self.myPM.OriginMap*10)    
    
    def ShowAllKapton(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        # self.loadonemap(1)
        # self.myPM.SetKaptonRegion()
        # plt.imshow(self.myPM.OriginMap*10)
        
        for i in range(0,np.shape(self.__totalmap)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.__totalmap)[0]/2)+1,2,i+1)
            plt.subplots_adjust(wspace = .35)
            self.loadonemap(i)
            self.myPM.SetKaptonRegion()
            self.InputSubplot(ax,self.myPM.OriginMap*10)    
        
    def ShowKaptonPCB(self,):
        for i in range(0,np.shape(self.__totalmap)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.__totalmap)[0]/2)+1,2,i+1)
            plt.subplots_adjust(wspace = .35)
            self.loadonemap(i)
            self.myPM.SetKaptonRegion()
            self.myPM.SetPCBRegion()
            self.InputSubplot(ax,self.myPM.OriginMap*10)
            

    def XProjectionUp_row(self,myhspace=0.5,mywspace=0.3):
        # plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.__totalmap)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.__totalmap)[0]/2)+1,2,i+1)
            totalnull = list()
            self.loadonemap(i)
            ymin_temp = 400
            self.Slice(0,1023,0,ymin_temp)
            
            
            # for j in range(0,512):
            #     print(np.nanmean(self.__totalmap[i][j]))
            #     meanthrs.append(np.nanmean(self.__totalmap[i][j])*10)
            for j in range(0,1023):
                # print("{}th".format(j))
                # print(np.count_nonzero(self.__totalmap[i,j,:,0]))
                totalnull.append(np.count_nonzero(self.myPM.PartialMap[:,j,0]))
                
            plt.plot(range(0,1023),totalnull)
            # print(totalnull)
            # plt.xticks([0,100,200,300,400,500])
            
            plt.xlim(0,1023)
            plt.ylim(0,100)
            plt.xlabel('row')
            plt.ylabel('#')
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        plt.savefig(self.__output,dpi=300)
    
    def CountFakefire(self,):
        mycount = 0
        print(np.shape(self.myPM.PartialMap))
        for x in range(self.myPM.xmin,self.myPM.xmax):
            for y in range(self.myPM.ymin,self.myPM.ymax):
                # print("x: {}, y: {}".format(x,y))
                # if self.myPM.PartialMap[x-self.myPM.xmin,y-self.myPM.xmin,0] == 0:
                if self.myPM.PartialMap[y-self.myPM.ymin,x-self.myPM.xmin,0] != 0:
                    mycount += 1
                
                # if np.isnan(self.myPM.OriginMap[y,x]):
                #     mycount += 1
        print(mycount)
        return mycount
    
    def AllNullScatter(self,):
        Apr_path = "processed/totalnpy/Apr_rowhits_origin_total.npy"    
        Jun_path = "processed/totalnpy/Jun_rowhits_origin_total.npy"    
        Jul_RPI_path = "processed/totalnpy/Jul_RPI_rowhits_origin_total.npy"
        Jul_RAS_path = "processed/totalnpy/Jul_RAS_rowhits_origin_total.npy"
        Sep_path = "processed/totalnpy/Sep_rowhits_origin_total.npy"    
        Nov_path = "processed/totalnpy/Nov_rowhits_origin_total.npy"    
        
        plt.figure(1,figsize=(7,5),facecolor='white')
        self.innerScatter(Apr_path,99.2,'red')
        self.innerScatter(Jun_path,97.66,'gold')
        self.innerScatter(Jul_RAS_path,99.1,'blue')
        self.innerScatter(Jul_RPI_path,99.1,'lime')
        self.innerScatter(Sep_path,24.26,'navy')
        self.innerScatter(Nov_path,54.01,'magenta')
        
        plt.xlabel("Energy(MeV)")
        plt.ylabel("Number of Fake fire")
        plt.savefig(self.__output,dpi=300)
        
    def innerScatter(self,mypath,myenergy,mycolor):
        self.loadtotalmap(mypath)
        for i in range(0,np.shape(self.__totalmap)[0]):
            self.loadonemap(i)
            self.Slice(0,1023,400,512)
            plt.scatter(myenergy,self.CountFakefire(),color=mycolor,s=5)