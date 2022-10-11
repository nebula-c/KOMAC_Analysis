import numpy as np
import os,sys
import copy

class MergeNpy:
    __mytype = ''
    __mypath = './'
    __myoutput = 'new_'
    __mytarget = ''
    
    def SetPath(self,mypath) : self.__mypath = mypath
    def SetType(self,mytype) : self.__mytype = mytype
    def SetOutput(self,myoutput) : self.__myoutput = myoutput
    def SetTarget(self,mytarget) : self.__mytarget = mytarget
    
    def run(self,):
        filelist = os.popen('ls {} | grep {}'.format(self.__mypath,self.__mytype)).read().split()
        
        npylist = []
        for file in filelist:
            onenpy = np.load(self.__mypath+file)
            npylist.append(onenpy)
        np.save(self.__mypath+self.__myoutput,npylist)

    def extractNull(self,):
        originnpy = np.load(self.__mytarget)
        newone = copy.deepcopy(originnpy)
        np.set_printoptions(threshold=np.inf)
        for ith in range(len(newone)):
            for x in range(len(newone[ith])):
                for y in range(len(newone[ith][x])):
                    # if np.isnan(newone[ith][x][y]) :
                    #     print("{},{},{} : {}".format(ith,x,y,newone[ith][x][y]))
                    if newone[ith][x][y]==0 or np.isnan(newone[ith][x][y]):
                        newone[ith][x][y] = 1
                    else:
                        newone[ith][x][y] = 0
        np.save(self.__mypath+self.__myoutput,newone)
                        
            
            
        
    