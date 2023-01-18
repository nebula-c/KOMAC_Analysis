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
from . import MapCtrl

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
import matplotlib.ticker as mticker

import copy

matplotlib.use('TkAgg')  # Or any other X11 back-end

class Subsub:
    
    def __init__(self,):
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
    
    __output = ''

    mythrs1 = ANTA.Thrs()
    mythrs2 = ANTA.Thrs()
    resthrs = ANTA.Thrs()
    
    mymap1 = []
    mymap2 = []
    resmap = []
    
    PCB_npy = []
    Kapton_npy = []
    Left_npy = []
    Mid_npy = []
    origin_part_npy = []
    
    myrha1   = Rowhitsana.Rowhits()
    myrha2   = Rowhitsana.Rowhits()
    
    mymapctrl   =   MapCtrl.MapCtrl()
    mymapctrl.PartMap = mymapctrl.PartialMap()
    
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
        self.mymap1 = self.mymap1 * 10
    
    def SetMap2(self,ith):
        self.mymap2 = self.mythrs2.totalnpy[ith]
        self.mymap2 = self.mymap2 * 10
    
    def PutNullas0(self,):
        # self.mymap1[np.isnan(self.mymap1)] = 0
        self.mymap2[np.isnan(self.mymap2)] = 0
    
    def subThrsNpy(self, ):
        self.resthrs.totalnpy = self.mythrs1.totalnpy - self.mythrs2.totalnpy
        self.resthrs.SetOutput("test")
        self.resthrs.allmaps()
        
    def SetCbar(self, myax, myim):
        
        aspect = 20
        pad_fraction = 0.5
        divider = make_axes_locatable(myax)
        width = axes_size.AxesY(myax, aspect=1./aspect)
        pad = axes_size.Fraction(pad_fraction, width)
        cax = divider.append_axes("right", size=width, pad=pad)
        plt.colorbar(myim,cax=cax)
        plt.clim(-30,30)
        # plt.clim(0,30)
        
    ### map1 - map2
    def SubThrsMap(self,):
        # self.resmap = self.mymap1 - self.mymap2
        # self.resmap = self.mymap2 - self.mymap1
        self.resmap = self.mymap2
        
        plt.figure(1,figsize=(7,9),facecolor='white')
        ax = plt.axes()
        im = plt.imshow(self.resmap,interpolation='none')
        # im = plt.imshow(self.resmap, norm=LogNorm(vmin=0.01),interpolation='none')
        plt.xlim(0,1024)
        
        self.mymapctrl.PartMap.SetPCBRegion()
        self.mymapctrl.PartMap.SetKaptonRegion()
                
        self.SetCbar(ax,im)
        
        
        ### Code for zbar
        # aspect = 20
        # pad_fraction = 0.5
        # divider = make_axes_locatable(ax)
        # width = axes_size.AxesY(ax, aspect=1./aspect)
        # pad = axes_size.Fraction(pad_fraction, width)
        # cax = divider.append_axes("right", size=width, pad=pad)
        # plt.colorbar(im,cax=cax)
        
        
    ### To draw 3d surface, incompleted
    def SubThrsMap_3D(self,):
        # self.resmap = self.mymap1 - self.mymap2
        self.resmap = self.mymap2
        
        fig = plt.figure(1,figsize=(7,9),facecolor='white')
        ax = fig.add_subplot(111, projection='3d')
        
        X = np.arange(0, 1024)
        Y = np.arange(0, 512)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)
        print(self.resmap)

        Z = np.log10(Z)
        ax.plot_surface(X,Y,Z)
        zticks = [1e+0, 1e+1, 1e+2, 1e3]
        ax.set_zticks(np.log10(zticks))
        ax.set_zticklabels(zticks)

        # ax.view_init(0,0)
        # ax.set_zlim(0,1000000)

        # surf = ax.plot_surface(X, Y, self.resmap,linewidth=0, antialiased=False)

    
    
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
        
    def SubThrsMapPack(self,):
        self.mymap1 = self.mythrs2.totalnpy[0] * 10
        
        for i in range(0,np.shape(self.mythrs2.totalnpy)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.mythrs2.totalnpy)[0]/2)+1,2,i+1)
            
            self.SetMap2(i)
            self.resmap = self.mymap2 - self.mymap1
            # self.resmap = self.mymap2
            
            plt.subplots_adjust(wspace = .4)
            # im = plt.imshow(self.resmap, norm=LogNorm(vmin=0.01))
            im = plt.imshow(self.resmap,interpolation='none')
            plt.xlim(0,1024)
            
            self.mymapctrl.PartMap.SetPCBRegion()
            self.mymapctrl.PartMap.SetKaptonRegion()
            self.mymapctrl.PartMap.SetLeftRegion()
            self.mymapctrl.PartMap.SetMidRegion()

            self.SetCbar(ax,im)
            
            print(1024*512 - np.count_nonzero(~np.isnan(self.resmap)))
    

    def SubThrsMapPackPart(self,mode):
        self.mymap1 = self.mythrs2.totalnpy[0] * 10
        
        for i in range(0,np.shape(self.mythrs2.totalnpy)[0]):
            ax = plt.figure(1).add_subplot(int(np.shape(self.mythrs2.totalnpy)[0]/2)+1,2,i+1)
            
            self.SetMap2(i)
            self.resmap = self.mymap2 - self.mymap1
            
            self.mymapctrl.copynpyfrom(self.resmap)
            
            if mode == "PCB":
                self.mymapctrl.myPM.ExtractPCB()
                # self.mymapctrl.myPM.ConvertPCBOutside()
            if mode == "Kapton":
                self.mymapctrl.myPM.ExtractKapton()
            if mode == "Left":
                self.mymapctrl.myPM.ExtractLeft()
            if mode == "Mid":
                self.mymapctrl.myPM.ExtractMid()
            if mode == "LEdge":
                self.mymapctrl.myPM.ExtractLEdge()
                # self.mymapctrl.myPM.ConvertLEdgeOutside
            if mode == "REdge":
                self.mymapctrl.myPM.ExtractREdge()
                # self.mymapctrl.myPM.ConvertREdgeOutside
            if mode == "Bellow":
                self.mymapctrl.myPM.ExtractBellow()
            
            plt.subplots_adjust(wspace = .4)
            
            im = plt.imshow(self.mymapctrl.myPM.resultMap,interpolation='none')
            # plt.xlim(0,1024)


            self.SetCbar(ax,im)
            
        
    def SubThrsMapPackPartHisto(self,mode):
        self.mymap1 = copy.deepcopy(self.mythrs2.totalnpy[0] * 10)
        
        dose_list = [0,10.12,21.66,31.06,37.04]
        NumberOfNull_list = []
        
        All_num = 1024*512
        PCB_num = 45604
        Kapton_num = 148005
        left_num = 42900
        mid_num = 42900
        Ledge_num = 2556
        Redge_num = 2556
        bellow_num = 113664
        
        myarea = 0
        
        for i in range(0,np.shape(self.mythrs2.totalnpy)[0]):
            # ax = plt.figure(1).add_subplot(int(np.shape(self.mythrs2.totalnpy)[0]/2)+1,2,i+1)
            self.SetMap2(i)
            
            self.resmap = self.mymap2 - self.mymap1
            self.resmap = self.mymap1 - self.mymap2
            # self.resmap = self.mymap2
            self.mymapctrl.copynpyfrom(self.resmap)
            self.extractedmap = []
            
            if mode == "All":
                self.mymapctrl.myPM.ExtractAll()
                myarea = All_num
            if mode == "PCB":
                self.mymapctrl.myPM.ExtractPCB()
                # self.mymapctrl.myPM.ConvertPCBOutside()
                myarea = PCB_num
            if mode == "Kapton":
                self.mymapctrl.myPM.ExtractKapton()
                myarea = Kapton_num
            if mode == "Left":
                self.mymapctrl.myPM.ExtractLeft()
                myarea = left_num
            if mode == "Mid":
                self.mymapctrl.myPM.ExtractMid()
                myarea = mid_num
            if mode == "LEdge":
                self.mymapctrl.myPM.ExtractLEdge()
                # self.mymapctrl.myPM.ConvertLEdgeOutside
                myarea = Ledge_num
            if mode == "REdge":
                self.mymapctrl.myPM.ExtractREdge()
                # self.mymapctrl.myPM.ConvertREdgeOutside
                myarea = Redge_num
            if mode == "Bellow":
                self.mymapctrl.myPM.ExtractBellow()
                myarea = bellow_num
                
            
            self.extractedmap = self.mymapctrl.myPM.resultMap
            xlength, ylength = np.shape(self.extractedmap)
            Total_Num_null = xlength * ylength - np.count_nonzero(~np.isnan(self.extractedmap))
            Num_Null_per_area = Total_Num_null / myarea
            NumberOfNull_list.append(Num_Null_per_area)
            # NumberOfNull_list.append(Total_Num_null)
            print(np.shape(self.extractedmap))
            break
        
        print(NumberOfNull_list)
        # plt.plot(dose_list,NumberOfNull_list,label=mode)
        plt.scatter(0,NumberOfNull_list,label=mode)
        plt.legend()

    def SubThrsMapPackPartHisto_All(self,):
        self.SubThrsMapPackPartHisto("All")
        self.SubThrsMapPackPartHisto("PCB")
        self.SubThrsMapPackPartHisto("Kapton")
        self.SubThrsMapPackPartHisto("Left")
        self.SubThrsMapPackPartHisto("Mid")
        
        plt.title("# of null pixel for each region per pixelss")
        # plt.yscale('log')
        plt.xlabel("Dose(krad)")
        # plt.xticks([0,1,2,3,4])
        
        
    def ThrsMapPackPartHisto(self,mode):
        self.mymap1 = self.mythrs2.totalnpy[0] * 10
        
        dose_list = [0,10.12,21.66,31.06,37.04]
        MeanThreshold_list = []
        
        for i in range(0,np.shape(self.mythrs2.totalnpy)[0]):
            self.SetMap2(i)
            
            self.resmap = self.mymap2
            self.mymapctrl.copynpyfrom(self.resmap)
            self.extractedmap = []
            
            if mode == "All":
                self.mymapctrl.myPM.ExtractAll()
            if mode == "PCB":
                self.mymapctrl.myPM.ExtractPCB()
            if mode == "Kapton":
                self.mymapctrl.myPM.ExtractKapton()
            if mode == "Left":
                self.mymapctrl.myPM.ExtractLeft()
            if mode == "Mid":
                self.mymapctrl.myPM.ExtractMid()
            if mode == "LEdge":
                self.mymapctrl.myPM.ExtractLEdge()
            if mode == "REdge":
                self.mymapctrl.myPM.ExtractREdge()
            if mode == "Bellow":
                self.mymapctrl.myPM.ExtractBellow()
                
            self.extractedmap = self.mymapctrl.myPM.resultMap
            xlength, ylength = np.shape(self.extractedmap)
            if mode == "PCB":
                sumval = np.nansum(self.extractedmap)
                meanval = sumval / (xlength * ylength - self.mymapctrl.myPM.NumberOfOutsidePCBpixel() - np.count_nonzero(np.isnan(self.extractedmap)))
                # print((xlength * ylength - self.mymapctrl.myPM.NumberOfOutsidePCBpixel() - np.count_nonzero(np.isnan(self.extractedmap))))
                print("sumval : {}".format(sumval))
                print("pixel # : {}".format((xlength * ylength - self.mymapctrl.myPM.NumberOfOutsidePCBpixel() - np.count_nonzero(np.isnan(self.extractedmap)))))
                print("meanval : {}".format(meanval))
            elif mode == "LEdge":
                sumval = np.nansum(self.extractedmap)
                meanval = sumval / (xlength * ylength - self.mymapctrl.myPM.NumberOfOutsideLEdgepixel() - np.count_nonzero(np.isnan(self.extractedmap)))
                print((xlength * ylength - self.mymapctrl.myPM.NumberOfOutsideLEdgepixel() - np.count_nonzero(np.isnan(self.extractedmap))))
                print(sumval)
            elif mode == "REdge":
                sumval = np.nansum(self.extractedmap)
                meanval = sumval / (xlength * ylength - self.mymapctrl.myPM.NumberOfOutsideREdgepixel() - np.count_nonzero(np.isnan(self.extractedmap)))
                print((xlength * ylength - self.mymapctrl.myPM.NumberOfOutsideREdgepixel() - np.count_nonzero(np.isnan(self.extractedmap))))
                print(sumval)
            else:
                meanval = np.nanmean(self.extractedmap)
            MeanThreshold_list.append(meanval)
            
            
            # break
        print("Mode : {}-> {}".format(mode,MeanThreshold_list))
        # print(MeanThreshold_list)
        plt.plot(dose_list,MeanThreshold_list,label=mode)
        # plt.scatter(0,MeanThreshold_list,label=mode)
        plt.legend()
        
    def ThrsMapPackPartHisto_All(self,):
        self.ThrsMapPackPartHisto("All")
        self.ThrsMapPackPartHisto("PCB")
        self.ThrsMapPackPartHisto("Kapton")
        self.ThrsMapPackPartHisto("Left")
        self.ThrsMapPackPartHisto("Mid")
        self.ThrsMapPackPartHisto("LEdge")
        self.ThrsMapPackPartHisto("REdge")
        self.ThrsMapPackPartHisto("Bellow")
        
        plt.title("Mean threshold of each region for dose")
        plt.xlabel("Dose(krad)")
        # plt.xticks(range(0,100,10))
        # plt.ylim(0,200)
        
    
    
    
    
    
    def NullPackPartHistoForArea(self,mode):
        self.mymap1 = copy.deepcopy(self.mythrs2.totalnpy[0] * 10)
        
        dose_list = [0,10.12,21.66,31.06,37.04]
        NumberOfNull_list = []
        
        All_num = 1024*512
        PCB_num = 45604
        Kapton_num = 148005
        left_num = 42900
        mid_num = 42900
        Ledge_num = 2556
        Redge_num = 2556
        bellow_num = 113664
        
        myarea = 0
        
        for i in range(0,np.shape(self.mythrs2.totalnpy)[0]):
            # ax = plt.figure(1).add_subplot(int(np.shape(self.mythrs2.totalnpy)[0]/2)+1,2,i+1)
            self.SetMap2(i)
            self.resmap = self.mymap2
            
            self.mymapctrl.copynpyfrom(self.resmap)
            self.extractedmap = []
            
            if mode == "All":
                self.mymapctrl.myPM.ExtractAll()
                myarea = All_num
            if mode == "PCB":
                self.mymapctrl.myPM.ExtractPCB()
                # self.mymapctrl.myPM.ConvertPCBOutside()
                myarea = PCB_num
            if mode == "Kapton":
                self.mymapctrl.myPM.ExtractKapton()
                myarea = Kapton_num
            if mode == "Left":
                self.mymapctrl.myPM.ExtractLeft()
                myarea = left_num
            if mode == "Mid":
                self.mymapctrl.myPM.ExtractMid()
                myarea = mid_num
            if mode == "LEdge":
                self.mymapctrl.myPM.ExtractLEdge()
                # self.mymapctrl.myPM.ConvertLEdgeOutside
                myarea = Ledge_num
            if mode == "REdge":
                self.mymapctrl.myPM.ExtractREdge()
                # self.mymapctrl.myPM.ConvertREdgeOutside
                myarea = Redge_num
            if mode == "Bellow":
                self.mymapctrl.myPM.ExtractBellow()
                myarea = bellow_num
                
            
            self.extractedmap = self.mymapctrl.myPM.resultMap
            xlength, ylength = np.shape(self.extractedmap)
            Total_Num_null = xlength * ylength - np.count_nonzero(~np.isnan(self.extractedmap))
            Num_Null_per_area = Total_Num_null / myarea
            # print("Num_Null_per_area : {}".format(Num_Null_per_area))
            NumberOfNull_list.append(Num_Null_per_area)
            # NumberOfNull_list.append(Total_Num_null)
            # print(np.shape(self.extractedmap))

        
        print(NumberOfNull_list)
        plt.plot(dose_list,NumberOfNull_list,label=mode)
        # plt.scatter(0,NumberOfNull_list,label=mode)
        plt.legend()

    def NullPackPartHistoForArea_All(self,):
        self.NullPackPartHistoForArea("All")
        self.NullPackPartHistoForArea("PCB")
        self.NullPackPartHistoForArea("Kapton")
        self.NullPackPartHistoForArea("Left")
        self.NullPackPartHistoForArea("Mid")
        self.NullPackPartHistoForArea("LEdge")
        self.NullPackPartHistoForArea("REdge")
        self.NullPackPartHistoForArea("Bellow")
        
        plt.title("# of null pixel for each region per pixelss")
        # plt.yscale('log')
        plt.xlabel("Dose(krad)")
        # plt.xticks([0,1,2,3,4])
        
        
    def NullPackPartHisto(self,mode):
        self.mymap1 = copy.deepcopy(self.mythrs2.totalnpy[0] * 10)
        
        dose_list = [0,10.12,21.66,31.06,37.04]
        NumberOfNull_list = []
        
        All_num = 1024*512
        PCB_num = 45604
        Kapton_num = 148005
        left_num = 42900
        mid_num = 42900
        Ledge_num = 2556
        Redge_num = 2556
        bellow_num = 113664
        
        myarea = 0
        
        for i in range(0,np.shape(self.mythrs2.totalnpy)[0]):
            # ax = plt.figure(1).add_subplot(int(np.shape(self.mythrs2.totalnpy)[0]/2)+1,2,i+1)
            self.SetMap2(i)
            self.resmap = self.mymap2
            
            self.mymapctrl.copynpyfrom(self.resmap)
            self.extractedmap = []
            
            if mode == "All":
                self.mymapctrl.myPM.ExtractAll()
                myarea = All_num
            if mode == "PCB":
                self.mymapctrl.myPM.ExtractPCB()
                # self.mymapctrl.myPM.ConvertPCBOutside()
                myarea = PCB_num
            if mode == "Kapton":
                self.mymapctrl.myPM.ExtractKapton()
                myarea = Kapton_num
            if mode == "Left":
                self.mymapctrl.myPM.ExtractLeft()
                myarea = left_num
            if mode == "Mid":
                self.mymapctrl.myPM.ExtractMid()
                myarea = mid_num
            if mode == "LEdge":
                self.mymapctrl.myPM.ExtractLEdge()
                # self.mymapctrl.myPM.ConvertLEdgeOutside
                myarea = Ledge_num
            if mode == "REdge":
                self.mymapctrl.myPM.ExtractREdge()
                # self.mymapctrl.myPM.ConvertREdgeOutside
                myarea = Redge_num
            if mode == "Bellow":
                self.mymapctrl.myPM.ExtractBellow()
                myarea = bellow_num
                
            
            self.extractedmap = self.mymapctrl.myPM.resultMap
            xlength, ylength = np.shape(self.extractedmap)
            Total_Num_null = xlength * ylength - np.count_nonzero(~np.isnan(self.extractedmap))
            NumberOfNull_list.append(Total_Num_null)
            print(np.shape(self.extractedmap))

        
        print(NumberOfNull_list)
        plt.plot(dose_list,NumberOfNull_list,label=mode)
        # plt.scatter(0,NumberOfNull_list,label=mode)
        plt.legend()

    def NullPackPartHisto_All(self,):
        self.NullPackPartHisto("All")
        self.NullPackPartHisto("PCB")
        self.NullPackPartHisto("Kapton")
        self.NullPackPartHisto("Left")
        self.NullPackPartHisto("Mid")
        self.NullPackPartHisto("LEdge")
        self.NullPackPartHisto("REdge")
        self.NullPackPartHisto("Bellow")
        
        plt.title("# of null pixel for each region")
        plt.yscale('symlog')
        plt.xlabel("Dose(krad)")
        # plt.xticks([0,1,2,3,4])
        
        