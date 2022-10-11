import os,sys
import time
import copy

from multiprocessing import Process

class Multisub:
    __path = './'
    __resname = 'threshold_rev'
    __macro = './revision_thrscanana.py'
    __myargs = []
    __target = []
    __mode = 0
    __numoftarget = 0
    __newdir = []

    def SetPath(self,mypath): self.__path = mypath
    def SetName(self,myname): self.__resname = myname
    def SetMacro(self,mymacro): self.__macro = mymacro
    def SetArgs(self,myargs): self.__myargs.append(myargs)
    def SetTarget(self,mytarget): self.__target = mytarget
    def SetNewDir(self,mynewdir): self.__newdir = mynewdir

    def SetMode(self,mymode): 
        self.__mode = mymode
        
        ### Code for ExtractNpy(FireNum)
        if self.__mode == 1:
            self.__macro = "./src/ExtractNpy.py"
        
        ### Code for origin thrscanana
        if self.__mode == 2:
            self.__macro = "/home/suchoi/alpide-daq-software/analyses/thrscanana.py"
        
        ### Code for revision_thrscanana
        if self.__mode == 3:
            self.__macro = "./src/revision_thrscanana.py"

        ### Code for All extraction
        if self.__mode == 4:
            self.__macro = "./src/AllExtract.py"
        
        ### Code for mythrescanana
        if self.__mode == 5:
            self.__macro = "./src/mythrscanana.py"
        

    def SetTarget2(self, target_list_json_file, target_list_raw_file):
        targetnum1 = 0
        targetnum2 = 0

        target_list_json = []
        target_list_raw = []

        jsonfiles = open('%s'%(target_list_json_file))
        for onefile in jsonfiles:
            onefile = onefile.split()
            target_list_json.append(onefile[0])
            targetnum1 += 1


        rawfiles = open('%s'%(target_list_raw_file))
        for onefile in rawfiles:
            onefile = onefile.split()
            target_list_raw.append(onefile[0])
            targetnum2 += 1
        
        if not targetnum1 == targetnum2:
            print("Check targets!!!!")
            return
        
        else: self.__numoftarget = targetnum1

        self.__target.append(target_list_raw)
        self.__target.append(target_list_json)
        
        
    
    def OneJob(self, i):
        if self.__mode ==0:
            print("Check Mode")
            return

        ### Code for ExtractNpy
        if self.__mode == 1:
            mycode = '''python3 {} {} {} --path {} -o {}_{}.npy'''.format(self.__macro,self.__target[0][i],self.__target[1][i],self.__path,self.__resname,i) 

        ### Code for revision_thrscanana
        if self.__mode == 2:
            mycode = '''python3 {} {} {} --path {} -o {}_{}.npy'''.format(self.__macro,self.__target[0][i],self.__target[1][i],self.__path,self.__resname,i) 


        ### Code for revision_thrscanana
        if self.__mode == 3:
            mycode = '''python3 {} {} {} --path {} -o {}_{}.npy'''.format(self.__macro,self.__target[0][i],self.__target[1][i],self.__path,self.__resname,i) 
        
        ### Code for All ExtractNpy
        if self.__mode == 4:
            mycode = '''python3 {} {} {} --path {} -o {}_{}'''.format(self.__macro,self.__target[0][i],self.__target[1][i],self.__path,self.__resname,i) 
        
        ### Code for mythrescanana
        if self.__mode == 5:
            # os.system('mkdir %s'mydir)    
            mycode = '''python3 {} {} {} --path {} -s -r -q'''.format(self.__macro,self.__target[0][i],self.__target[1][i],self.__path,self.__resname,i) 
        
        ### For test
        if self.__mode == 100:
            print(self.__target[0])
        
        os.system(mycode)


    def Run(self,):
        process_list = []
        for i in range(self.__numoftarget):
        # for i in range(5):
            
            myprocess = Process(target = self.OneJob,args=(i,))
            process_list.append(myprocess)
            process_list[i].start()


        for i in range(self.__numoftarget):
        # for i in range(5):
            process_list[i].join()
        




if __name__ == '__main__':
    start = time.time()
    multisub = Multisub()
    multisub.Run(sys.argv[1])

    end = time.time()
    print("=========================")
    print("{} sec(sub)".format(end-start))
    print("=========================")