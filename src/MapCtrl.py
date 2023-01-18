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
        
        extractPCBMap = []
        extractKaptonMap = []
        extractLeftMap = []
        extractMidMap = []
        extractLEdgeMap = []
        extractREdgeMap = []
        extractBellowMap = []
        
        resultMap = []
        
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
            plt.imshow(self.OriginMap,interpolation='none')
        
        def ShowPart_rowhits(self,):
            self.RemovedValMap =  copy.deepcopy(self.OriginMap[:,:,20])
            # print(self.OriginMap)
            plt.hlines(self.ymin, self.xmin, self.xmax, color='red', linestyle='solid', linewidth=3)
            plt.hlines(self.ymax, self.xmin, self.xmax, color='red', linestyle='solid', linewidth=3)
            plt.vlines(self.xmin, self.ymin, self.ymax, color='red', linestyle='solid', linewidth=3)
            plt.vlines(self.xmax, self.ymin, self.ymax, color='red', linestyle='solid', linewidth=3)
            plt.imshow(self.RemovedValMap,interpolation='none')
        
        def SetPCBRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 145
            x11 = 150
            x2 = 257
            x22 = 300
            x3 = 420
            x33 = 427
            
            y1 = 512 - 200 - 10
            y11 = 512 - 200 + 10
            y2  = 512 - 456
            y22 = 512 - 456
            y3 = 512 - 200 + 10
            y33 = 512 - 200 - 10
            
            plt.plot([x11,x3],  [y11,y3],  color='red',linewidth=1)
            plt.plot([x3,x33],  [y3,y33] , color='red',linewidth=1)
            plt.plot([x33,x22], [y33,y22],  color='red',linewidth=1)
            plt.plot([x22,x2],  [y22,y2] ,  color='red',linewidth=1)
            plt.plot([x2,x1],   [y2,y1] ,  color='red',linewidth=1)
            plt.plot([x1,x11],  [y1,y11],  color='red',linewidth=1)
            
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
            
        def SetLeftRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 0
            x2 = 100
            x3 = 100
            x4 = 0
            
            y1 = 429
            y2 = 429
            y3 = 512 - 512
            y4 = 512 - 512
            
            
            plt.plot([x1,x2],   [y1,y2],    color='blue',linewidth=1)
            plt.plot([x2,x3],   [y2,y3],    color='blue',linewidth=1)
            plt.plot([x3,x4],   [y3,y4],    color='blue',linewidth=1)
            plt.plot([x4,x1],   [y4,y1],    color='blue',linewidth=1)
        
        def SetMidRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 500
            x2 = 600
            x3 = 600
            x4 = 500
            
            y1 = 429
            y2 = 429
            y3 = 512 - 512
            y4 = 512 - 512
            
            
            plt.plot([x1,x2],   [y1,y2],    color='blue',linewidth=1)
            plt.plot([x2,x3],   [y2,y3],    color='blue',linewidth=1)
            plt.plot([x3,x4],   [y3,y4],    color='blue',linewidth=1)
            plt.plot([x4,x1],   [y4,y1],    color='blue',linewidth=1)
        
        def SetLEdgeRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 0
            x2 = 71
            x3 = 0
            
            y1 = 71
            y2 = 0
            y3 = 0
            
            
            plt.plot([x1,x2],   [y1,y2],    color='lawngreen',linewidth=1)
            plt.plot([x2,x3],   [y2,y3],    color='lawngreen',linewidth=1)
            plt.plot([x3,x1],   [y3,y1],    color='lawngreen',linewidth=1)
        
        def SetREdgeRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 953
            x2 = 1024
            x3 = 1024
            
            y1 = 0
            y2 = 71
            y3 = 0
            
            
            plt.plot([x1,x2],   [y1,y2],    color='lawngreen',linewidth=1)
            plt.plot([x2,x3],   [y2,y3],    color='lawngreen',linewidth=1)
            plt.plot([x3,x1],   [y3,y1],    color='lawngreen',linewidth=1)
            
        def SetBelowRegion(self,):
            # plt.figure(1,figsize=(7,9),facecolor='white')
            
            x1 = 0
            x2 = 1024
            x3 = 1024
            x4 = 0
            
            y1 = 511
            y2 = 511
            y3 = 400
            y4 = 400
            
            
            plt.plot([x1,x2],   [y1,y2],    color='lawngreen',linewidth=1)
            plt.plot([x2,x3],   [y2,y3],    color='lawngreen',linewidth=1)
            plt.plot([x3,x4],   [y3,y4],    color='lawngreen',linewidth=1)
            plt.plot([x4,x1],   [y4,y1],    color='lawngreen',linewidth=1)
            
            
        def ExtractPCB(self,):
            
            x1 = 145
            x11 = 150
            x2 = 257
            x22 = 300
            x3 = 420
            x33 = 427
            
            y1 = 512 - 200 - 10
            y11 = 512 - 200 + 10
            y2  = 512 - 456
            y22 = 512 - 456
            y3 = 512 - 200 + 10
            y33 = 512 - 200 - 10
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractPCBMap = mine[y22:y11,x1:x33]

            
            for y in range(y2-y2,y1-y2):
                for x in range(x1-x1,x2-x1):
                    if y < ((y2-y1)/(x2-x1)) * x + y1 - y2:
                        self.extractPCBMap[y,x]=0
            
            for y in range(y22-y22,y33-y22):
                for x in range(x22-x1,x33-x1):
                    if y < ((y33-y22)/(x33-x22)) * x - y33:
                        self.extractPCBMap[y,x]=0
            
            for y in range(y1-y2,y11-y2):
                for x in range(x1-x1,x11-x1):
                    if y > ((y11-y1)/(x11-x1)) * x + y1 - y2:
                        self.extractPCBMap[y,x]=0
            
            for y in range(y33-y2,y3-y2):
                for x in range(x3-x1,x33-x1):
                    if y > ((y3-y33)/(x3-x33)) * x + 1051:
                        self.extractPCBMap[y,x]=0
            
            self.resultMap = copy.deepcopy(self.extractPCBMap)
            # plt.imshow(self.extractPCBMap)
            
        def ExtractKapton(self,):
            x1 = 679
            x2 = 1024
            x3 = 1024
            x4 = 679
            
            y1 = 429
            y2 = 429
            y3 = 512 - 512
            y4 = 512 - 512
        
            mine = copy.deepcopy(self.OriginMap)
            self.extractKaptonMap = mine[y3:y1,x1:x2]
            
            self.resultMap = copy.deepcopy(self.extractKaptonMap)
            # plt.imshow(self.extractKaptonMap)
            
        def ExtractLeft(self,):
            x1 = 0
            x2 = 100
            x3 = 100
            x4 = 0
            
            y1 = 429
            y2 = 429
            y3 = 512 - 512
            y4 = 512 - 512
        
            mine = copy.deepcopy(self.OriginMap)
            self.extractLeftMap = mine[y3:y1,x1:x2]
            
            self.resultMap = copy.deepcopy(self.extractLeftMap)
            # plt.imshow(self.extractLeftMap)
        
        def ExtractMid(self,):
            x1 = 500
            x2 = 600
            x3 = 600
            x4 = 500
            
            y1 = 429
            y2 = 429
            y3 = 512 - 512
            y4 = 512 - 512
        
            mine = copy.deepcopy(self.OriginMap)
            self.extractMidMap = mine[y3:y1,x1:x2]
            
            self.resultMap = copy.deepcopy(self.extractMidMap)
            # plt.imshow(self.extractMidMap)
            
        def ExtractBellow(self,):
            x1 = 0
            x2 = 1024
            x3 = 1024
            x4 = 0
            
            y1 = 511
            y2 = 511
            y3 = 400
            y4 = 400
        
            mine = copy.deepcopy(self.OriginMap)
            self.extractBellowMap = mine[y3:y1,x1:x2]
            
            self.resultMap = copy.deepcopy(self.extractBellowMap)
            # plt.imshow(self.extractBellowMap)
            
        def ExtractLEdge(self,):
            
            x1 = 0
            x2 = 71
            x3 = 0
            
            y1 = 71
            y2 = 0
            y3 = 0
            
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractLEdgeMap = mine[y2:y1,x1:x2]

            
            for y in range(y3,y1):
                for x in range(x3,x2):
                    if y >= -x + y1:
                        self.extractLEdgeMap[y,x]=0
            
            
            self.resultMap = copy.deepcopy(self.extractLEdgeMap)
            # plt.imshow(self.resultMap)
        
        def ExtractREdge(self,):
            
            x1 = 953
            x2 = 1024
            x3 = 1024
            
            y1 = 0
            y2 = 71
            y3 = 0
            
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractREdgeMap = mine[y1:y2,x1:x2]

            
            for y in range(y3,y2):
                for x in range(x1-x1,x2-x1):
                    if y > x:
                        self.extractREdgeMap[y,x]=0
            
            
            self.resultMap = copy.deepcopy(self.extractREdgeMap)
            # plt.imshow(self.resultMap)
        
        ### Change values outside PCB as -1000
        def ConvertPCBOutside(self,):
            x1 = 145
            x11 = 150
            x2 = 257
            x22 = 300
            x3 = 420
            x33 = 427
            
            y1 = 512 - 200 - 10
            y11 = 512 - 200 + 10
            y2  = 512 - 456
            y22 = 512 - 456
            y3 = 512 - 200 + 10
            y33 = 512 - 200 - 10
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractPCBMap = mine[y22:y11,x1:x33]

            
            for y in range(y2-y2,y1-y2):
                for x in range(x1-x1,x2-x1):
                    if y < ((y2-y1)/(x2-x1)) * x + y1 - y2:
                        self.extractPCBMap[y,x]= -1000
            
            for y in range(y22-y22,y33-y22):
                for x in range(x22-x1,x33-x1):
                    if y < ((y33-y22)/(x33-x22)) * x - y33:
                        self.extractPCBMap[y,x]= -1000
            
            for y in range(y1-y2,y11-y2):
                for x in range(x1-x1,x11-x1):
                    if y > ((y11-y1)/(x11-x1)) * x + y1 - y2:
                        self.extractPCBMap[y,x]= -1000
            
            for y in range(y33-y2,y3-y2):
                for x in range(x3-x1,x33-x1):
                    if y > ((y3-y33)/(x3-x33)) * x + 1051:
                        self.extractPCBMap[y,x]= -1000
                        
            self.resultMap = copy.deepcopy(self.extractPCBMap)
            
        def ConvertLEdgeOutside(self,):
            
            x1 = 0
            x2 = 71
            x3 = 0
            
            y1 = 71
            y2 = 0
            y3 = 0
            
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractLEdgeMap = mine[y2:y1,x1:x2]

            
            for y in range(y3,y1):
                for x in range(x3,x2):
                    if y > -x + y1:
                        self.extractLEdgeMap[y,x]=-1000
            
            
            self.resultMap = copy.deepcopy(self.extractLEdgeMap)
            
        def ConvertREdgeOutside(self,):
            
            x1 = 953
            x2 = 1024
            x3 = 1024
            
            y1 = 0
            y2 = 71
            y3 = 0
            
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractREdgeMap = mine[y1:y2,x1:x2]

            
            for y in range(y3,y2):
                for x in range(x1-x1,x2-x1):
                    if y > x:
                        self.extractREdgeMap[y,x]=-1000
            
            
            self.resultMap = copy.deepcopy(self.extractREdgeMap)
            plt.imshow(self.resultMap)
        
        def ExtractAll(self,):
            self.resultMap = copy.deepcopy(self.OriginMap)
            
        def NumberOfOutsidePCBpixel(self,):
            x1 = 145
            x11 = 150
            x2 = 257
            x22 = 300
            x3 = 420
            x33 = 427
            
            y1 = 512 - 200 - 10
            y11 = 512 - 200 + 10
            y2  = 512 - 456
            y22 = 512 - 456
            y3 = 512 - 200 + 10
            y33 = 512 - 200 - 10
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractPCBMap = mine[y22:y11,x1:x33]

            countoutside = 0
            
            for y in range(y2-y2,y1-y2):
                for x in range(x1-x1,x2-x1):
                    if y < ((y2-y1)/(x2-x1)) * x + y1 - y2:
                        countoutside += 1
            
            for y in range(y22-y22,y33-y22):
                for x in range(x22-x1,x33-x1):
                    if y < ((y33-y22)/(x33-x22)) * x - y33:
                        countoutside += 1
            
            for y in range(y1-y2,y11-y2):
                for x in range(x1-x1,x11-x1):
                    if y > ((y11-y1)/(x11-x1)) * x + y1 - y2:
                        countoutside += 1
            
            for y in range(y33-y2,y3-y2):
                for x in range(x3-x1,x33-x1):
                    if y > ((y3-y33)/(x3-x33)) * x + 1051:
                        countoutside += 1
                        
            return countoutside
        
        def NumberOfOutsideLEdgepixel(self,):
            x1 = 0
            x2 = 71
            x3 = 0
            
            y1 = 71
            y2 = 0
            y3 = 0
            
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractLEdgeMap = mine[y2:y1,x1:x2]

            countoutside = 0
            
            for y in range(y3,y1):
                for x in range(x3,x2):
                    if y >= -x + y1:
                        countoutside += 1
            
            return countoutside
        
        def NumberOfOutsideREdgepixel(self,):
            x1 = 953
            x2 = 1024
            x3 = 1024
            
            y1 = 0
            y2 = 71
            y3 = 0
            
            
            mine = copy.deepcopy(self.OriginMap)
            self.extractREdgeMap = mine[y1:y2,x1:x2]

            countoutside = 0
            
            for y in range(y3,y2):
                for x in range(x1-x1,x2-x1):
                    if y > x:
                        countoutside += 1
            
            return countoutside
        
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
        
    def copynpyfrom(self, npyfromotherside):
        self.__onemap = npyfromotherside
        self.myPM.OriginMap = copy.deepcopy(self.__onemap)
    
    def printOneMap(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        plt.imshow(self.__onemap,interpolation='none')
        # plt.savefig(self.__output,dpi=300)
        
    def printRegion(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        self.myPM.ShowPart()
        # plt.imshow(self.myPM.PartialMap)
        plt.savefig(self.__output,dpi=300)
    
    def printPartial(self,):
        # plt.figure(1,figsize=(7,9),facecolor='white')
        plt.imshow(self.myPM.PartialMap,interpolation='none')
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
    
    def SetCbar(self, myax, myim):
        
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(myax)
        width = axes_size.AxesY(myax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        plt.colorbar(myim,cax=cax)
        # plt.clim(-30,30)
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
            
    def ShowOtherRegion(self,):
        for i in range(0,np.shape(self.__totalmap)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.__totalmap)[0]/2)+1,2,i+1)
            plt.subplots_adjust(wspace = .35)
            self.loadonemap(i)
            self.myPM.SetLeftRegion()
            self.myPM.SetMiddleRegion()
            self.InputSubplot(ax,self.myPM.OriginMap*10)
            
    def ShowAllRegion(self,):
        for i in range(0,np.shape(self.__totalmap)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.__totalmap)[0]/2)+1,2,i+1)
            plt.subplots_adjust(wspace = .35)
            self.loadonemap(i)
            self.myPM.SetKaptonRegion()
            self.myPM.SetPCBRegion()
            self.myPM.SetLeftRegion()
            self.myPM.SetMidRegion()
            self.myPM.SetLEdgeRegion()
            self.myPM.SetREdgeRegion()
            self.myPM.SetBelowRegion()
            self.InputSubplot(ax,self.myPM.OriginMap*10)
    
    def ShowAllRegion_onemap(self,):
        ax = plt.figure(1,figsize=(7,9),facecolor='white')
        self.myPM.SetKaptonRegion()
        self.myPM.SetPCBRegion()
        self.myPM.SetLeftRegion()
        self.myPM.SetMidRegion()
        self.myPM.SetLEdgeRegion()
        self.myPM.SetREdgeRegion()
        self.myPM.SetBelowRegion()
        
        ax = plt.axes()
        im = plt.imshow(self.myPM.OriginMap*10,interpolation='none')
        self.SetCbar(ax,im)
        
        
            

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
    
    def ShowExtractPCB(self,):
        self.myPM.ExtractPCB()

    def ShowExtractKapton(self,):
        self.myPM.ExtractKapton()
        
    def ShowExtractLeft(self,):
        self.myPM.ExtractLeft()
    
    def ShowExtractMid(self,):
        self.myPM.ExtractMid()
    
    def ShowExtractBellow(self,):
        self.myPM.ExtractBellow()
        
    def ShowExtractLEdge(self,):
        self.myPM.ExtractLEdge()
        
    def ShowExtractREdge(self,):
        self.myPM.ExtractREdge()
        
    def ShowNumPixelSomeRegion(self,):
        numLEdge = self.myPM.NumberOfOutsideLEdgepixel()
        numREdge = self.myPM.NumberOfOutsideREdgepixel()
        numPCB = self.myPM.NumberOfOutsidePCBpixel()
        
        total_num_LEdge =   0
        total_num_REdge =   0
        total_num_PCB   =   0
        
        print("Number of pixel @ Outside of Left Edge : {}".format(numLEdge))
        print("Number of pixel @ Outside of Right Edge : {}".format(numREdge))
        print("Number of pixel @ Outside of PCB Edge : {}".format(numPCB))
        
        print("--------------------------------------------------------")
        
        print("Number of pixel @ Outside of Left Edge : {}".format(numLEdge))
        print("Number of pixel @ Outside of Right Edge : {}".format(numREdge))
        print("Number of pixel @ Outside of PCB Edge : {}".format(numPCB))