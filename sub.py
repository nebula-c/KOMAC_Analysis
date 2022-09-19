#!/usr/bin/env python3

import os,sys
import argparse
import time 

# sys.path.append('/home/suchoi/CBTest/src')
# from src import test
from src import *
# import src

start = time.time()

parser=argparse.ArgumentParser(description='Submission program for Carrier Board Test')
parser.add_argument('--test',action='store_true',help='test')
parser.add_argument('--ms',action='store_true',help='Run analyses using MultiProcess')
parser.add_argument('-t','--target',help='Set target (list or not)')
parser.add_argument('-t1','--target1',help='Set target (list or not)')
parser.add_argument('-t2','--target2',help='Set target (list)')
parser.add_argument('-j','--json',help='Set json target list')
parser.add_argument('-r','--raw',help='Set raw target list')
parser.add_argument('-e','--extractnpy',action='store_true',help='Extract npy')
parser.add_argument('-f','--firenumana',action='store_true',help='Run analysis for Firenum')
parser.add_argument('-a','--allextractnpy',action='store_true',help='Extract npy')
args=parser.parse_args()


if args.test:
    test.Run(args.target)
    

if args.ms:
    mydir = './Sep'
    os.system('mkdir %s'%mydir)
    myms = Multisub.Multisub()
    myms.SetMode(5)
    myms.SetTarget2(args.json,args.raw)
    myms.SetPath(mydir)
    myms.Run()


if args.extractnpy:
    myen = ExtractNpy.ExtractNpy()
    # myen.Run(args.json,args.raw)
    
    myen.SetName("FireNum_ori_Jul_RAS.npy")
    myen.Combine_E(args.target,".npy")

    myen.SetName("Thrs_ori_Jul_RAS.npy")
    myen.Combine_E(args.target,"ori_thrs.npy")
    
    myen.SetName("Noise_ori_Jul_RAS.npy")
    myen.Combine_E(args.target,"ori_noise.npy")

    myen.SetName("FireNum_rev_Jul_RAS.npy")
    myen.Combine_E(args.target,"rev_firenum.npy")

    myen.SetName("Thrs_rev_Jul_RAS.npy")
    myen.Combine_E(args.target,"rev_thrs.npy")

    myen.SetName("Noise_rev_Jul_RAS.npy")
    myen.Combine_E(args.target,"rev_noise.npy")



if args.firenumana:
    myfna = FireNum.FireNumAna()
    Apr_ori = myfna.Thrsnpy("new_total_npy_dir/Apr/Thrs_ori_Apr.npy")
    Apr_rev = myfna.Thrsnpy("new_total_npy_dir/Apr/Thrs_rev_Apr.npy")
    Jun_ori = myfna.Thrsnpy("new_total_npy_dir/Jun/Thrs_ori_Jun.npy")
    Jun_rev = myfna.Thrsnpy("new_total_npy_dir/Jun/Thrs_rev_Jun.npy")
    RAS_ori = myfna.Thrsnpy("new_total_npy_dir/Jul_RAS/Thrs_ori_Jul_RAS.npy")
    RAS_rev = myfna.Thrsnpy("new_total_npy_dir/Jul_RAS/Thrs_rev_Jul_RAS.npy")
    RPI_ori = myfna.Thrsnpy("new_total_npy_dir/Jul_RPI/Thrs_ori_Jul_RPI.npy")
    RPI_rev = myfna.Thrsnpy("new_total_npy_dir/Jul_RPI/Thrs_rev_Jul_RPI.npy")

    a = RPI_ori
    a.DrawAllMaps()
    myfna.SaveImage("test.png")
    # myfna.SortPlot(a,b)
    


end = time.time()
print("=========================")
print("Total run-time : {0:00.2f} sec(sub)".format(end-start))
print("=========================")
