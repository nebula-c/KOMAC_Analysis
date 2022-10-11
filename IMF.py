#!/usr/bin/env python3

### Iridium Multi-threading File

import os,sys
import time
import copy
import argparse

from multiprocessing import Process


class Multisub:
    def GetCommand(self,myfile):
        myfilslist = open('%s'%(myfile))
        mycommand = []
        for onecommand in myfilslist:
            onecommand = onecommand.split()
            mycommand.append(onecommand)
    
    def OneJob(self,command):
        os.system(command)
            
    def Run(self,corenum,command_list):
        myfilslist = open('%s'%(command_list))

        process_list = []
        for onecommand in myfilslist:
            onecommand = onecommand.split('\n')[0]
            myprocess = Process(target = self.OneJob,args=(onecommand,))
            process_list.append(myprocess)
        


        totalnum = len(process_list)
        print('Total Number of Runs : {}'.format(totalnum))
        print('Number of Cores to use : {}'.format(corenum))
        donenum = 0
        while(True):

            for i in range(corenum):    
                process_list[donenum + i].start()
                if donenum + i + 1 == totalnum: break                
            for i in range(corenum):
                process_list[donenum + i].join()
                donenum = donenum + i + 1    
                if donenum + i + 1 == totalnum:break    
            
            donenum = donenum + corenum
            if donenum >= totalnum: break
        
        

            
        


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Iridium Multi-threading File')
    parser.add_argument('command_list', metavar='command_list',help='command list file')
    parser.add_argument('--corenum','-c', type = int ,help='number of core')
    args=parser.parse_args()

    if args.corenum >= 20 :
        print("too many core")
        sys.exit()

    start = time.time()

    multisub = Multisub()
    multisub.Run(args.corenum,args.command_list)

    end = time.time()
    print("=========================================")
    print("Total run-time : {0:00.2f} sec(sub)".format(end-start))
    print("=========================================")