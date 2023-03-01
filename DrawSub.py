#!/usr/bin/env python3

import os,sys
import argparse
import time 
import numpy as np

start = time.time()

# import sub


parser=argparse.ArgumentParser(description='Submission program for Carrier Board Test')
parser.add_argument('-o','--order',action='store_true',help='Show order of image(imglist.txt)')
parser.add_argument('-n','--number',type=int, help='Number of image(imglist.txt)')
parser.add_argument('--name', help='Set imagefile name(if you need)')

args=parser.parse_args()


imglistfilepath = "./imglist.txt"
imglistfile = open(imglistfilepath, 'r')
imglist = imglistfile.read()    
imglist = imglist.strip()

cmdlistfilepath = "./cmdlist.txt"
cmdlistfile = open(cmdlistfilepath, 'r')
cmdlist = cmdlistfile.read()    
cmdlist = cmdlist.strip()


if args.order:    
    print(imglist)
    
if args.number:
    inputnum = args.number
    imglist = imglist.split("\n")
    target_img_info = imglist[inputnum]
    target_num = target_img_info.split(",")[0].strip()
    target_filename = target_img_info.split(",")[1].strip()
    
    cmdlist = cmdlist.split("\n")
    target_cmd_info = cmdlist[inputnum]
    if target_num != target_cmd_info.split(",")[0].strip():
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("There is no relate cmd")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    target_cmd = target_cmd_info.split(",")[1].strip()
    os.system(target_cmd)
    
    
    

end = time.time()
print("=========================================")
print("Total run-time : {0:00.2f} sec(sub)".format(end-start))
print("=========================================")
