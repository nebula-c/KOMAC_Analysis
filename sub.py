#!/usr/bin/env python3

import os,sys
import argparse
import time 
import numpy as np

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
parser.add_argument('-p','--path',help='path',default='.')
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
parser.add_argument('-aa','--analognpyana',action='store_true',help='anlognpyana')
args=parser.parse_args()


if args.test:
    # test.Run()
    print("Hello, this is the test part of sub.py")
    

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
    mypath = args.path
    
    # mypath = "/home/suchoi/sourcetest/png/Vbb0V"
    # # PCB_data    = args.path
    # # PCB_data    = "processed/totalnpy/Apr_threshold_revision_total.npy"q
    # # PCB_data    = "processed/totalnpy/Nov_threshold_revision_total.npy"
    # # dosedata    = "doseinfo/Nov_dose.txt"
    
    # stpath = "/home/suchoi/sourcetest/day3/npys/threshold_origin_20230203_170804.npy"
    # mythrs.load(stpath)
    
    ### Vbb=3V
    hitnpypath = "/home/suchoi/sourcetest/day3/npys/hitmap_fhrscan-20230203_171421.npy"         ### Fe55
    
    
    
    
    # reverse_thrs_ori_path = "/home/suchoi/day8_2/thresholds.npy"
    reverse_thrs_path = "/home/suchoi/day8/thresholds.npy"
    # mythrs.load(reverse_thrs_ori_path)
    # mythrs.OneMap_OneNpy()
    
    
    # fullarea_hitmap = "/home/suchoi/KOMAC/analysis/processed/npys/sourcetest/fullarea/hitmap_fhrscan-20230209_194059.npy"
    # fullarea_thrs = "/home/suchoi/KOMAC/analysis/processed/npys/sourcetest/fullarea/threshold_origin_20230209_194200.npy"
    mythrs.Sub_FHR_Thrs(hitnpypath,reverse_thrs_path)

    # mythrs.pltshow()
    myoutput = "ST_boolsub_Fe55_upstream"
    mythrs.pltsave(mypath+'/'+myoutput)

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

    
    # mymapctrl.SliceRow(10,3)
    # mymapctrl.ShowExtractLEdge()
    testrows = [50,200,280,350,550,800,1003]
    mymapctrl.SliceRowWithMapsAll(testrows)
    # mymapctrl.SlicesPositionMap(testrows)
    
    mymapctrl.pltshow()
    # mymapctrl.pltsave("Slice7rowsMap")
    
    

if args.rowhit:
    myrha   = Rowhitsana.Rowhits()

    mypath = "/home/suchoi/KOMAC/analysis/processed/totalnpy/Apr_rowhits_origin_total.npy"
    # mypath = "/home/suchoi/sourcetest/totalnpys/total_rowhits_origin.npy"
    # mypath = "/home/suchoi/sourcetest/totalnpys/total_rowhits_revision.npy"
    # mypath = "/home/suchoi/sourcetest/totalnpys/total_threshold_origin.npy"
    # mypath = "/home/suchoi/sourcetest/totalnpys/total_threshold_reviison.npy"
    
    myrha.load(mypath)
    myrha.printshape()
    # myrha.printshape()
    # myrha.reshape(0,1,False)
    # myrha.reshape(1,2,True)
    # myrha.printshape()
    
    # myrha.SetOutput(args.path)
    # myrha.projectionY()
    
    
    # myrha.rh1stvalmap()
    # myrha.valNst(6)
    # myrha.val1_10st(3)
    myrha.Nst(3,0)
    
    mytitle = "Histogram of number of detection, when #e=0"
    myrha.plttitle(mytitle)
    myrha.pltshow()
    # myrha.pltsave(mytitle)

if args.subsub:
    # x = [1,2,np.nan,4,np.nan]
    # y = [np.nan,7,8,9,np.nan]
    # idx = np.isfinite(x) & np.isfinite(y)
    # x=np.array(x)
    # print(x[idx])
    
    mysubsub    = Subsub.Subsub()
    
    NoPCB_data  = "processed/totalnpy/Jul_RPI_threshold_origin_total.npy"
    PCB_data    = "processed/totalnpy/Nov_threshold_origin_total.npy"
    
    
    # mysubsub.loadthrs1(NoPCB_data)
    # mysubsub.SetMap1(0)
    mysubsub.loadthrs2(PCB_data)
    # mysubsub.SetMap2(2)
    # mysubsub.PutNullas0()
    
    mysubsub.DrawMap2()
    # mysubsub.NullThrs_all()
    
    # testarray = [1,2,3,4,5,6,7,8,9,10,11,12]
    # mysubsub.RebinFor1Row(testarray,4)
    
    
    # myoutput = args.output
    myoutput = "Nov_Thrs_Null_Area"
    mysubsub.pltshow()
    # mysubsub.pltsave(myoutput)
    
if args.analognpyana:
    myaa = analognpyana.Analognpyana()
    
    mypath1 = "/home/suchoi/day7/analog50"
    mypath2 = "/home/suchoi/KOMAC/analysis/processed/analognpy/each/ana50"
    # onepath = mypath2 + "/" + "analog-20230210_182543.npy"
    
    # myaa.make_each_analog_npy(mypath1)
    myaa.Draw_total_analog_npy(mypath2,'.',0,50)
    # myaa.DrawOneNpy(onepath)
    
    # myaa.pltshow()
    myaa.pltsave("test")


if __name__ == "__main__":
    end = time.time()
    print("=========================================")
    print("Run-time(sub.py) : {0:00.2f} sec(sub)".format(end-start))
    print("=========================================")