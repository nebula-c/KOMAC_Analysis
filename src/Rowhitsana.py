#!/usr/bin/env python3

#---------------------------------------------------------------------
# Analyzing Numpy-files for Row-hits of ALPIDE
#---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import sys
import os
        
class Rowhits:
    __totalrowhits = []
    __myregionrowhits = []
    __output = 'test'
    __path = ''
    
    def SetOutput(self,myoutput): self.__output = myoutput
    
    def pltshow(self,): plt.show()
    
    def pltsave(self, myname): 
        self.__output = myname
        plt.savefig(self.__output,dpi=300)
    
    def plttitle(self, mytitle): 
        plt.title(mytitle)
    
    def load(self, path):
        self.__path = path
        self.__totalrowhits = np.load(self.__path)
    
    def printshape(self,):
        print(np.shape(self.__totalrowhits))
        
    def reshape(self,axis1,axis2,issave):
        print("Before reshape")
        self.printshape()
        self.__totalrowhits = self.__totalrowhits.swapaxes(axis1,axis2)
        print("After reshape")
        self.printshape()
        if issave:
            np.save(self.__path,self.__totalrowhits)
            print("It was saved successfully")
            
    def setregion(self,xmin,xmax,ymin,ymax):
        self.__myregionrowhits = self.totalvals
        print("Not yet")
    
    def oneexample(self,):
        ith = 2
        x   = 500
        y   = 191
        t = np.arange(0, 210, 10)
        print(self.__totalrowhits[ith,x,y])
        plt.plot(t,self.__totalrowhits[ith,x,y],'-o')
        plt.xlabel("Number of Electron",fontsize=14)
        plt.ylabel("Number of Detection(/50times)",fontsize=14)
        plt.savefig(self.__output,dpi=300)
        
    def rh1stvalmap(self,val=0):
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
        for i in range(0,np.shape(self.__totalrowhits)[0]):
            fig.add_subplot(int(np.shape(self.__totalrowhits)[0]/2)+1,2,i+1)
            myrh = self.__totalrowhits[i,0]>val
            # plt.imshow(myrh,interpolation='none',cmap = "Blues")
            plt.imshow(self.__totalrowhits[i,0],interpolation='none',cmap = "Blues")
            
            plt.clim(0,1)
            
        # plt.savefig(self.__output,dpi=300)
            
    
    def valNst(self,Nth):
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
        for ith in range(np.shape(self.__totalrowhits)[0]):
            vals = []
            fig.add_subplot(int(np.shape(self.__totalrowhits)[0]/2)+1,2,ith+1)
            for x in range(0,512):
                for y in range(0,1024):
                    # if self.__totalrowhits[ith,x,y,0] > 0:
                    # mytext = "ith :{}, x : {}, y : {}".format(ith,x,y)
                    # print(mytext)
                    vals.append(self.__totalrowhits[ith,Nth,x,y,])
            plt.hist(vals,bins=51,range=(0,50))
            plt.xticks([0,10,20,30,40,50])
            plt.ylim(0,1000000)
            plt.yscale('symlog')
            plt.grid(True)
        plt.savefig(self.__output,dpi=300)
    
    def valNst(self,Nth):
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
        for ith in range(np.shape(self.__totalrowhits)[0]):
            vals = []
            fig.add_subplot(int(np.shape(self.__totalrowhits)[0]/2)+1,2,ith+1)
            for x in range(0,512):
                for y in range(0,1024):
                    # if self.__totalrowhits[ith,x,y,0] > 0:
                    # mytext = "ith :{}, x : {}, y : {}".format(ith,x,y)
                    # print(mytext)
                    vals.append(self.__totalrowhits[ith,x,y,Nth])
            print(np.shape(vals))
            plt.hist(vals,bins=51,range=(0,50))
            plt.xticks([0,10,20,30,40,50])
            plt.ylim(0,1000000)
            plt.yscale('symlog')
            plt.grid(True)
        plt.savefig(self.__output,dpi=300)
    
    def val1_10st(self,MaxNth):
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
        # total cycle
        for ith in range(np.shape(self.__totalrowhits)[0]):
            totalvals = []
            fig.add_subplot(int(np.shape(self.__totalrowhits)[0]/2)+1,2,ith+1)
            for Nth in range(0,MaxNth):
                vals= []
                for x in range(0,512):
                    for y in range(0,1024):
                        # vals.append(self.__totalrowhits[ith,Nth,x,y,])
                        vals.append(self.__totalrowhits[ith,x,y,Nth])
                totalvals.append(vals)
            for Nth in range(0,MaxNth):
                plt.hist(totalvals[Nth],bins=51,range=(0,50),histtype='step',label=Nth)
                
                ###------------------------------------------------------------
                # Code to change hists to plots with dots
                # n,bins,patches=plt.hist(totalvals[Nth],bins=51,alpha=0)
                # plt.plot(bins[:-1]+ 0.5*(bins[1:] - bins[:-1]), n, marker='o',markersize=1,linewidth=0.1)#, s=40, alpha=1)
                # plt.scatter(bins,n, marker='o', c='red', s=40, alpha=1)
                ###------------------------------------------------------------
            
            plt.xticks([0,10,20,30,40,50])
            plt.ylim(0,1000000)
            plt.yscale('symlog')
            plt.grid(True)
            plt.legend(fontsize=6)
        plt.savefig(self.__output,dpi=300)
    
    
    def projectionY(self,myhspace=0.5,mywspace=0.3):
        plt.figure(1,figsize=(7,9),facecolor='white')
    
        for i in range(0,np.shape(self.__totalrowhits)[0]):
            plt.figure(1).add_subplot(int(np.shape(self.__totalrowhits)[0]/2)+1,2,i+1)
            totalnull = list()
            
            for j in range(0,512):
                # print("{}th".format(j))
                # print(np.count_nonzero(self.__totalrowhits[i,j,:,0]))
                totalnull.append(np.count_nonzero(self.__totalrowhits[i,j,:,0]))
                
            plt.plot(range(0,512),totalnull)
            # print(totalnull)
            plt.xticks([0,100,200,300,400,500])
            
            plt.xlim(0,512)
            plt.ylim(0,1024)
            plt.xlabel('row')
            plt.ylabel('#')
            

        
        plt.subplots_adjust(hspace = myhspace,wspace = mywspace)
        plt.savefig(self.__output,dpi=300)
        
    def Nst(self,ith,Nth):
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
        mybins=np.arange(0,52,1)-.5
        
        
        totalvals = []
        vals= []
        for x in range(0,512):
            for y in range(0,1024):
                vals.append(self.__totalrowhits[ith,x,y,Nth])
        # totalvals.append(vals)
        print(vals)
        
        plt.hist(vals,bins=mybins,edgecolor='black')
        
        # n,bins,patches=plt.hist(vals,bins=51,alpha=0)
        # plt.plot(bins[:-1]+ 0.5*(bins[1:] - bins[:-1]), n, marker='o',markersize=3,linewidth=0.9)
        # # plt.plot(bins[:-1], n, marker='o',markersize=3,linewidth=0.9)
        # # plt.scatter(bins,n, marker='o', c='red', s=40, alpha=1)
        # print(bins[:-1])
        # print(bins[:-1]+ 0.5*(bins[1:] - bins[:-1]))
        plt.xlabel("Number of electrons")
        plt.ylabel("Number of detection(total:50)")
        plt.xticks([0,10,20,30,40,50])
        # plt.xlim(0,51)
        plt.ylim(0,1000000)
        plt.yscale('symlog')
        plt.grid(True)
        plt.legend(fontsize=6)
        plt.savefig(self.__output,dpi=300)