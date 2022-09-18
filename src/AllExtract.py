#!/usr/bin/env python3

import argparse
import json
import numpy as np
from alpidedaqboard import decoder
from tqdm import tqdm
from scipy import optimize
from scipy import special
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import copy
import sys
import os


class AllExtractNpy:
    __outfilename   =   'firenum'
    __outpath       =   './'
    __Is_d          =   False
    
    __target_list_json = []
    __target_list_raw = []
    
    

    def SetName(self, myname):    self.__outfilename = myname
    def SetPath(self, mypath):    self.__outpath = mypath

    def __SetTarget(self, target_list_json_file, target_list_raw_file):
        jsonfiles = open('%s'%(target_list_json_file))
        for onefile in jsonfiles:
            onefile = onefile.split()
            self.__target_list_json.append(onefile[0])


        rawfiles = open('%s'%(target_list_raw_file))
        for onefile in rawfiles:
            onefile = onefile.split()
            self.__target_list_raw.append(onefile[0])
        

    def SaveNpy(self,file_json,file_raw):
        TotalOriFireNum = []
        TotalRevFireNum = []

        try:
            with open('%s'%(file_json),'r') as f:
                params=json.loads(f.read())
        except IOError:
            print('ERROR: File %s could not be read!'%(file_json))
            raise SystemExit(1)
        
        try:
            with open('%s'%(file_raw),'rb') as f:
                data=f.read()
        except IOError:
            print('ERROR: File %s could not be read!'%(file_raw))
            raise SystemExit(1)


        dvmin,dvmax=params['dvmin'],params['dvmax']
        if params['row']==None: params['row']=range(512)
        ntrg = params['ntrg']
        pbar=tqdm(total=len(data))
        
        thresholds=np.zeros((512,1024))
        noise=np.zeros((512,1024))
        dead=[]
        bad=[]

        thresholdsr=np.zeros((512,1024))
        noiser=np.zeros((512,1024))
        deadr=[]
        badr=[]


        OriFireNum=[]
        RevFireNum=[]
        OriThrs=[]
        RevThrs=[]

        
        i=0

        
        
        for row in params['row']:
            rowhits=np.zeros((dvmax-dvmin+1,1024))
            for dv in range(dvmin,dvmax+1):
                for itrg in range(params['ntrg']):
                    hits,iev,tev,j=decoder.decode_event(data,i)
                    pbar.update(j-i)
                    i=j
                    for x,y in hits:
                        if y!=row:
                            print('warning: hit from bad row: hit=(%d,%d) row=%d \n'%(x,y,row))
                        else:
                            rowhits[dv-dvmin,x]+=1




            OriFireNum = copy.deepcopy(rowhits)
            
            for mynum in range(1024):
                if (rowhits[0,mynum] != 0) & (rowhits[0,mynum] != 50):
                    rowhits[0,mynum]=0

            RevFireNum = copy.deepcopy(rowhits)



            d=np.diff(OriFireNum,axis=0)
            nhits = np.sum(d,axis=0)
            if np.any(nhits<ntrg):
                bad.extend([(col,row) for col in np.where(nhits<ntrg)[0]])
            if np.any(nhits==0):
                dead.extend([(col,row) for col in np.where(nhits==0)[0]])
            nhits[nhits<ntrg] = np.nan # exclude from calculation

            dr=np.diff(RevFireNum,axis=0)
            nhitsr = np.sum(dr,axis=0)
            if np.any(nhitsr<ntrg):
                badr.extend([(col,row) for col in np.where(nhitsr<ntrg)[0]])
            if np.any(nhitsr==0):
                deadr.extend([(col,row) for col in np.where(nhitsr==0)[0]])
            nhitsr[nhitsr<ntrg] = np.nan # exclude from calculation


            # nhits[nhits<ntrg] = np.nan # exclude from calculation
            d/=nhits
            dv=np.linspace(0.5,OriFireNum.shape[0]-1.5,OriFireNum.shape[0]-1)[:,np.newaxis]    
            t=np.sum(d*dv,axis=0)
            n=np.sqrt(np.sum((dv-t)**2*d,axis=0))
            thresholds[row,:]=t
            noise[row,:]=n
            
            dr/=nhitsr
            dvr=np.linspace(0.5,RevFireNum.shape[0]-1.5,RevFireNum.shape[0]-1)[:,np.newaxis]    
            tr=np.sum(dr*dvr,axis=0)
            nr=np.sqrt(np.sum((dvr-tr)**2*dr,axis=0))
            thresholdsr[row,:]=tr
            noiser[row,:]=nr

            
            
            
            TotalOriFireNum.append(OriFireNum)
            TotalRevFireNum.append(RevFireNum)

        TotalOriFireNum = np.array(TotalOriFireNum).swapaxes(0,1)
        TotalOriFireNum = np.array(TotalOriFireNum).swapaxes(1,2)
        TotalRevFireNum = np.array(TotalRevFireNum).swapaxes(0,1)
        TotalRevFireNum = np.array(TotalRevFireNum).swapaxes(1,2)

        np.save('%s/%s_ori_firenum.npy'%(self.__outpath,self.__outfilename),TotalOriFireNum)
        np.save('%s/%s_rev_firenum.npy'%(self.__outpath,self.__outfilename),TotalRevFireNum)
        np.save('%s/%s_ori_thrs.npy'%(self.__outpath,self.__outfilename),thresholds)
        np.save('%s/%s_rev_thrs.npy'%(self.__outpath,self.__outfilename),thresholdsr)
        np.save('%s/%s_ori_noise.npy'%(self.__outpath,self.__outfilename),noise)
        np.save('%s/%s_rev_noise.npy'%(self.__outpath,self.__outfilename),noiser)
        


    def Run(self,target_list_json_file,target_list_raw_file):
        self.__SetTarget(target_list_json_file,target_list_raw_file)
        print('Number of Target : %d'%len(self.__target_list_json))
        
        if len(self.__target_list_json) != len(self.__target_list_raw):
            print("Error : Check target list fiel")
            return 0


        for i in range(len(self.__target_list_json)):
            self.SaveNpy(self.__target_list_json[i],self.__target_list_raw[i])
            
    def Combine(self,filepath):
        filelist = os.listdir()
        filelist = [file for file in filelist if file.endswith(".npy")]
        filelist.sort()
        
        totalnpy = []
        for file in filelist:
            onenp = np.load(file)
            totalnpy.append(onenp)
        totalnpy = np.array(totalnpy)
        
        np.save('{}/{}'.format(self.__outpath,self.__outfilename),totalnpy)
        


if __name__=="__main__":
    parser=argparse.ArgumentParser(description='The mighty threshold scanner')
    parser.add_argument('rawdata', metavar='RAWFILE',help='raw data file to be processed')
    parser.add_argument('params', metavar='JSONFILE',help='json file with scan setteing')
    parser.add_argument('--path',help='Output plots path', default='.' )
    parser.add_argument('--debug-plots',action='store_true',help='show debug plots: bad fit pixels, hitmap',default=False)
    parser.add_argument('--fit',  action='store_true',help='Fast (default) or fitted method',default=False)
    parser.add_argument('--output','-o',default='thresholds.npy',help='numpy output (default: thresholds.npy)')
    parser.add_argument('--quiet','-q',action='store_true',help="No plots, no terminal output, just npy file.")
    args=parser.parse_args()

    myen = AllExtractNpy()
    if args.path: myen.SetPath(args.path)
    if args.output: myen.SetName(args.output)
    
    # print(args.params)
    # print(args.rawdata)
    myen.SaveNpy(args.params,args.rawdata)
