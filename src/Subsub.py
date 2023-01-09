#!/usr/bin/env python3

#---------------------------------------------------------------------
# Code for control serveral threshold and rowhits
# I made sub.py to control serveral analysios file,
# But I made some files too much and I need to sub-sub.py
# When I want to use two raw-files, if I use sub.py, 
# It will be difficult to see it.
# So, it is just for when I need serveral instances.
#---------------------------------------------------------------------

from . import ANTA
from . import Rowhitsana

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')  # Or any other X11 back-end

class Subsub:
    __output = ''

    mythrs1 = ANTA.Thrs()
    mythrs2 = ANTA.Thrs()
    resthrs = ANTA.Thrs()
    
    mymap1 = []
    mymap2 = []
    resmap = []
    
    myrha1   = Rowhitsana.Rowhits()
    myrha2   = Rowhitsana.Rowhits()
    
    def SetOutput(self,myoutput): self.__output = myoutput
    
    def pltshow(self,): plt.show()
    
    def pltsave(self, myname): 
        self.__output = myname
        plt.savefig(self.__output,dpi=300)

    def testfunc(self,):
        self.mythrs1.testfunction()
        
    def loadthrs1(self, path):
        self.mythrs1.load(path)
    
    def loadthrs2(self, path):
        self.mythrs2.load(path)
    
    def loadrha1(self, path):
        self.myrha1.load(path)
    
    def loadrha2(self, path):
        self.myrha2.load(path)
        
    def SetMap1(self,ith):
        self.mymap1 = self.mythrs1.totalnpy[ith]
    
    def SetMap2(self,ith):
        self.mymap2 = self.mythrs2.totalnpy[ith]
    
    def PutNullas0(self,):
        self.mymap1[np.isnan(self.mymap1)] = 0
        self.mymap2[np.isnan(self.mymap2)] = 0
    
    def subThrsNpy(self, ):
        self.resthrs.totalnpy = self.mythrs1.totalnpy - self.mythrs2.totalnpy
        self.resthrs.SetOutput("test")
        self.resthrs.allmaps()
        
    def subThrsMap(self,):
        self.resmap = self.mymap1 - self.mymap2
        # self.resmap = self.mymap1
        
        plt.figure(1,figsize=(7,9),facecolor='white')
        ax = plt.axes()
        im = ax.imshow(self.resmap)
        
        ### Code for zbar
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(ax)
        width = axes_size.AxesY(ax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        plt.colorbar(im,cax=cax)
        
        
    ### To draw 3d surface, incompleted
    def testFunc(self,):
        self.resmap = self.mymap1 - self.mymap2
        # self.resmap = self.mymap2
        
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
        ax = fig.add_subplot(111, projection='3d')
        # ax = plt.axes()
        # im = ax.imshow(self.resmap)
        # im = ax.plot(self.resmap[:,0],self.resmap[:,1],self.resmap[:,2])
        # ax.imshow(self.resmap)
        # X,Y = np.meshgrid(range(0,512),range(0,1024))
        # ax.plot_surface(range(0,512),range(0,1024),self.resmap)
        
        X = np.arange(0, 1024)
        Y = np.arange(0, 512)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)
        print(self.resmap)
        
        # ax.view_init(90,0)

        surf = ax.plot_surface(X, Y, self.resmap,linewidth=0, antialiased=False)

    
    
    def rebin(self, x, y, mapnum=3):
        if mapnum == 1: targetmap = self.mymap1
        if mapnum == 2: targetmap = self.mymap2
        if mapnum == 3: targetmap = self.resmap
        
        shape = (y,x)
        sh = shape[0],targetmap.shape[0]//shape[0],shape[1],targetmap.shape[1]//shape[1]
        result =  targetmap.reshape(sh).mean(-1).mean(1)
        
        
        
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(ax)
        width = axes_size.AxesY(ax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        plt.colorbar(im,cax=cax)
        
        
        plt.imshow(result)
        
    def pltCbarSet(self,myimage):
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(ax)
        width = axes_size.AxesY(ax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        plt.colorbar(myimage,cax=cax)