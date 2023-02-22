#!/usr/bin/env python3

import argparse
import json
import numpy as np
from scipy import optimize
from scipy import special
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
import copy
import sys
import os

class Analognpyana:
    plt.figure(1,figsize=(7,9),facecolor='white')
        
    def SetOutput(self,myoutput): self.__output = myoutput
    
    def pltshow(self,): plt.show()
    
    def pltsave(self, myname): 
        self.__output = myname
        plt.savefig(self.__output,dpi=300)
    
    def pltxlim(self,min,max):
        plt.xlim(min,max)
    
    def pltylim(self,min,max):
        plt.ylim(min,max)
        
    
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

    def make_each_analog_npy(self, inputpath, outpath='.'):
        myrawdir = inputpath
        myoutpath = "/home/suchoi/KOMAC/analysis/processed/analognpy/each/ana50"
        outpath = myoutpath
        
        filelist = os.listdir(myrawdir)
        rawfilelist = []
        jsonfilelist = []
        f = open("{}/tempcmd.txt".format(outpath), 'w')
        for afile in filelist:
            filetype = afile.split('.')[1]
            # if filetype == 'json': jsonfilelist.append(afile)
            if filetype == 'raw': 
                # rawfilelist.append(afile)
                cmd = "/home/suchoi/KOMAC/analysis/src/myanalogana.py {}/{} --save -p {} ".format(inputpath,afile,outpath)
                f.write(cmd+'\n')
        f.close()
        totalcmd = "/home/suchoi/IMF/IMF.py {}/tempcmd.txt -c 10".format(outpath)
        os.system(totalcmd)
        
    def Draw_total_analog_npy(self, inputpath, outpath='.', mymin=0, mymax=50):
        myrawdir = inputpath
        myoutpath = "/home/suchoi/KOMAC/analysis/processed/analognpy/total"
        outpath = myoutpath
        
        filelist = os.listdir(myrawdir)
        filelist.sort()
        
        npyfilelist = []
        totalnpy = np.zeros((512,1024))
        
        i=0
        for afile in filelist:
            filetype = afile.split('.')[1]
            if filetype == 'npy': 
                # npyfilelist.append(afile)
                tempnpy = np.load(myrawdir+'/'+afile)
                totalnpy = totalnpy + tempnpy
                i+=1
                if i==mymax:
                     print("Files from '{}' to '{}'".format(firstfile,afile))
                     break
            if i==mymin+1:
                firstfile = afile

                
        print(totalnpy)
        # print(np.shape(totalnpy))
        ax = plt.axes()
        # im = plt.imshow(totalnpy,interpolation='none')
        im = plt.imshow(totalnpy,cmap="Blues",interpolation='none')
        
        self.SetCbar(ax,im)

    def DrawOneNpy(self,myinput):
        tempnpy = np.load(myinput)
        ax = plt.axes()
        im = plt.imshow(tempnpy,cmap="Blues",interpolation='none')


if __name__=="__main__":
    import decoder
    parser=argparse.ArgumentParser(description='My analysis file for alpide-analog')
    parser.add_argument('rawdata', metavar='RAWFILE',help='raw data file to be processed')
    parser.add_argument('params', metavar='JSONFILE',help='json file with scan setteing')
    parser.add_argument('--path','-p',help='Output path', default='.' )
    parser.add_argument('--output','-o',default='myoutput',help='numpy output (default: thresholds.npy)')
    args=parser.parse_args()

    # print(args)

    mythrscanana(args)