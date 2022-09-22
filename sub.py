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
# parser.add_argument('-a','--allextractnpy',action='store_true',help='Extract npy')
parser.add_argument('-m','--merge',action='store_true',help='Merge numpy files')
parser.add_argument('-p','--path',help='path')
parser.add_argument('-a','--anta',action='store_true',help='Analyzing Numpy-files for Threshold of ALPIDE(ANTA)')
parser.add_argument('-o','--output',help='output name')
parser.add_argument('-v1','--value1',type=float,help='value1 for parameter')
parser.add_argument('-v2','--value2',type=float,help='value2 for parameter')
parser.add_argument('-c','--cpprun',action='store_true',help='Running some cpp file with root')
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


# if args.extractnpy:
#     myen = ExtractNpy.ExtractNpy()
#     # myen.Run(args.json,args.raw)
    
#     myen.SetName("FireNum_ori_Jul_RAS.npy")
#     myen.Combine_E(args.target,".npy")

#     myen.SetName("Thrs_ori_Jul_RAS.npy")
#     myen.Combine_E(args.target,"ori_thrs.npy")
    
#     myen.SetName("Noise_ori_Jul_RAS.npy")
#     myen.Combine_E(args.target,"ori_noise.npy")

#     myen.SetName("FireNum_rev_Jul_RAS.npy")
#     myen.Combine_E(args.target,"rev_firenum.npy")

#     myen.SetName("Thrs_rev_Jul_RAS.npy")
#     myen.Combine_E(args.target,"rev_thrs.npy")

#     myen.SetName("Noise_rev_Jul_RAS.npy")
#     myen.Combine_E(args.target,"rev_noise.npy")



# if args.firenumana:
#     myfna = FireNum.FireNumAna()
#     Apr_ori = myfna.Thrsnpy("new_total_npy_dir/Apr/Thrs_ori_Apr.npy")
#     Apr_rev = myfna.Thrsnpy("new_total_npy_dir/Apr/Thrs_rev_Apr.npy")
#     Jun_ori = myfna.Thrsnpy("new_total_npy_dir/Jun/Thrs_ori_Jun.npy")
#     Jun_rev = myfna.Thrsnpy("new_total_npy_dir/Jun/Thrs_rev_Jun.npy")
#     RAS_ori = myfna.Thrsnpy("new_total_npy_dir/Jul_RAS/Thrs_ori_Jul_RAS.npy")
#     RAS_rev = myfna.Thrsnpy("new_total_npy_dir/Jul_RAS/Thrs_rev_Jul_RAS.npy")
#     RPI_ori = myfna.Thrsnpy("new_total_npy_dir/Jul_RPI/Thrs_ori_Jul_RPI.npy")
#     RPI_rev = myfna.Thrsnpy("new_total_npy_dir/Jul_RPI/Thrs_rev_Jul_RPI.npy")

#     a = RPI_ori
#     a.DrawAllMaps()
#     myfna.SaveImage("test.png")
#     # myfna.SortPlot(a,b)
    
if args.merge:
    # mymn = MergeNpy.MergeNpy()
    # mymn.SetPath('eachdata/Apr/')
    # mymn.SetType('rowhits_origin')
    # mymn.SetOutput('Apr_rowhits_origin_total.npy')
    # mymn.run()

    mymn = MergeNpy.MergeNpy()
    mymn.SetPath(args.path)
    mymn.SetType(args.target1)
    mymn.SetOutput(args.target2)
    mymn.run()

if args.anta:
    # mythrs = ANTA.Thrs()
    # mypath = './totalnpy/Apr_threshold_origin_total.npy'
    # mythrs.load(mypath)
    # mythrs.printshape()
    # mythrs.testshow()

    mythrs = ANTA.Thrs()
    mythrs.load(args.path)
    # mythrs.allmaps(args.output,args.value)
    # mythrs.allhist(args.output,args.value1,args.value2)
    mythrs.meanthrs()

if args.cpprun:
    # cppfile = './src/test.cpp'
    cppfile = './src/dose_thrs.cpp'
    dosetxt = '/home/suchoi/KOMAC/analysis/processed/dose/Apr_dose.txt'
    thrstxt = 'hello'
    mycommand = """root '{}("{}","{}")' -l""".format(cppfile,dosetxt,thrstxt)
    os.system(mycommand)

# end = time.time()
# print("=========================================")
# print("Total run-time : {0:00.2f} sec(sub)".format(end-start))
# print("=========================================")
