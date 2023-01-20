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
# parser.add_argument('-e','--extractnpy',action='store_true',help='Extract npy')
parser.add_argument('-f','--firenumana',action='store_true',help='Run analysis for Firenum')
parser.add_argument('-e','--allextract',action='store_true',help='Extract npy')
parser.add_argument('-m','--merge',action='store_true',help='Merge numpy files')
parser.add_argument('-p','--path',help='path')
parser.add_argument('-a','--anta',action='store_true',help='Analyzing Numpy-files for Threshold of ALPIDE(ANTA)')
parser.add_argument('-o','--output',help='output name')
parser.add_argument('-v1','--value1',type=float,help='value1 for parameter')
parser.add_argument('-v2','--value2',type=float,help='value2 for parameter')
parser.add_argument('-c','--cpprun',action='store_true',help='Running some cpp file with root')
parser.add_argument('--mode',type=int,help='Set mode(int)')
parser.add_argument('--hitmap',action='store_true',help='hitmap')
parser.add_argument('-mc','--mapctrl',action='store_true',help='Map control')
parser.add_argument('-ro','--rowhit',action='store_true',help='rowhit')
parser.add_argument('-ss','--subsub',action='store_true',help='Subsub')
args=parser.parse_args()


if args.test:
    test.Run()
    

if args.ms:
    myms = Multisub.Multisub()
    myms.SetMode(args.mode)
    myms.SetTarget2(args.json,args.raw)
    myms.SetPath(args.path)
    myms.SetName(args.output)
    myms.Run()


if args.allextract:
    myae = AllExtract.AllExtractNpy()
    
    # myae.SetPath(args.path)
    myae.SetName(args.output)
    # myae.Run(args.json,args.raw)
    
    myae.DrawHitmap(args.raw)
    
if args.merge:
    mymn = MergeNpy.MergeNpy()
    mymn.SetPath('temp/')
    mymn.SetType(args.target)
    mymn.SetOutput(args.output)
    mymn.run()

    # mymn = MergeNpy.MergeNpy()
    # mymn.SetPath(args.path)
    # mymn.SetType(args.target1)
    # mymn.SetOutput(args.target2)
    # mymn.run()
    # mymn.SetTarget(args.target1)
    # mymn.SetOutput(args.target2)
    # mymn.extractNull()

if args.anta:
    mythrs = ANTA.Thrs()
    
    # PCB_data    = args.path
    # PCB_data    = "processed/totalnpy/Apr_threshold_revision_total.npy"
    PCB_data    = "processed/totalnpy/Nov_threshold_revision_total.npy"
    dosedata    = "doseinfo/Nov_dose.txt"
    mythrs.load(PCB_data)
    mythrs.loaddose(dosedata)
    # mythrs.SetAllMonthsData()
    # mythrs.printshape()
    
    # mythrs.OddEvenRowThrs_all()
    # mythrs.projectionY()
    # mythrs.All0kradThrsProj("Y")

    

    # mythrs.pltshow()
    # mythrs.pltsave("All_OddEven_thrs_dose")
    # mythrs.pltsave("All_thrs_ProjY_Pad")

if args.cpprun:
    cppfile = './dose_thrs.cpp'
    dosetxt = args.target1
    thrstxt = args.target2
    mycommand = """root '{}("{}","{}","{}")' -l -q""".format(cppfile,dosetxt,thrstxt,args.output)
    os.system(mycommand)


if args.mapctrl:
    mymapctrl = MapCtrl.MapCtrl()
    
    # mymapctrl.SetOutput("test.png")
    
    # mymapctrl.loadtotalmap("processed/totalnpy/Jun_threshold_revision_total.npy")
    mymapctrl.loadtotalmap("processed/totalnpy/Nov_threshold_origin_total.npy")
    mymapctrl.loadonemap(0)

    
    mymapctrl.TestSlice(10)
    # mymapctrl.ShowExtractLEdge()
    
    
    mymapctrl.pltshow()
    # mymapctrl.pltsave("test")
    
    

if args.rowhit:
    myrha   = Rowhitsana.Rowhits()
# 
# 
    myrha.load(args.target)
    # myrha.printshape()
    myrha.SetOutput(args.path)
    myrha.projectionY()
    # myrha.reshape(1,2,True)
    # myrha.reshape(2,3,True)
    
    # myrha.rh1stvalmap(1)
    # myrha.valNst(1)
    # myrha.val1_10st(1)


if args.subsub:
    mysubsub    = Subsub.Subsub()
    
    NoPCB_data  = "processed/totalnpy/Jul_RPI_threshold_origin_total.npy"
    PCB_data    = "processed/totalnpy/Nov_threshold_origin_total.npy"
    
    mysubsub.loadthrs1(NoPCB_data)
    mysubsub.loadthrs2(PCB_data)
    mysubsub.SetMap1(0)
    mysubsub.SetMap2(0)
    # mysubsub.PutNullas0()
    
    # mysubsub.SubThrsMap()
    # mysubsub.SubThrsMap_3D()
    
    # mymode = args.target
    # mysubsub.NullPackPartHisto_All()
    mysubsub.NullPackPartHistoForArea_All()
    # mysubsub.ThrsMapPackPartHisto_All()
    
    
    # myoutput = args.output
    myoutput = "Nov_NullNum_AllRegion_perc"
    # mysubsub.pltshow()
    mysubsub.pltsave(myoutput)
    


end = time.time()
print("=========================================")
print("Total run-time : {0:00.2f} sec(sub)".format(end-start))
print("=========================================")

