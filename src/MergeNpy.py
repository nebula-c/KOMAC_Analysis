import numpy as np
import os

class MergeNpy:
    __mytype = ''
    __mypath = './'
    __myoutput = 'new_'
    
    def SetPath(self,mypath) : self.__mypath = mypath
    def SetType(self,mytype) : self.__mytype = mytype

    def run(self,):
        filelist = os.popen('ls {} | grep {}'.format(self.__mypath,self.__mytype)).read()
        print(filelist)


    