import numpy as np
import os

class MergeNpy:
    __mytype = ''
    __mypath = './'
    __myoutput = 'new_'
    
    def SetPath(self,mypath) : self.__mypath = mypath
    def SetType(self,mytype) : self.__mytype = mytype
    def SetOutput(self,myoutput) : self.__myoutput = myoutput

    def run(self,):
        filelist = os.popen('ls {} | grep {}'.format(self.__mypath,self.__mytype)).read().split()
        
        npylist = []
        for file in filelist:
            onenpy = np.load(self.__mypath+file)
            npylist.append(onenpy)
        np.save(self.__mypath+self.__myoutput,npylist)


    