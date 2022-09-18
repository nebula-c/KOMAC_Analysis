from cProfile import label
# from turtle import down
import numpy as __np
import pandas
from collections import Counter
import matplotlib.pyplot as __plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors


import sys as __sys
import os as __os
# from sklearn.preprocessing import scale

# from sqlalchemy import false, true



# __nanNum = list()
# __datalist = list()


# __npydir = "/home/suchoi/KOMAC/analysis/npy/threshold_each"
# __newnpydir = "/home/suchoi/KOMAC/analysis/npy"
# # __plotdir = "/Users/hipex/KOMAC/result/plot/"
# __filelist=__os.listdir(__npydir)
# __filelist.sort()


# totalnpy = __np.load("./npy/total_data.npy")
# for i in range(0,9):
#     __datalist.append(totalnpy[i])

### ----------------------------------------------------------------------                        
### count val
def __CountValue(mynpy,val):
    count=0
    if __np.isnan(val):
        for i in range(0,512):
            for j in range(0,1024):
                if __np.isnan(mynpy[i][j]) :
                    count = count + 1
        print('number of "nan" : %d'%(count))   
    
    else:
        for i in range(0,512):
            for j in range(0,1024):
                if mynpy[i][j] == val:
                    count = count + 1            
        print('number of "%d" : %d'%(val,count))
    return count    


### ----------------------------------------------------------------------
### opem all numpy
def open_all():
    for __np_file in __filelist:
        if __np_file[len(__np_file)-1] =='y':
            print('file %s is open'%(__np_file))
            __data = __np.load(__npydir + '/' + __np_file)
            __datalist.append(__data)
            
            __count = __CountValue(__data,__np.nan)
            __nanNum.append(__count)

### ----------------------------------------------------------------------
### save total numpy
def save_total_numpy():
    total_np_list = []
    
    __npydir = "./temp"
    __filelist=__os.listdir(__npydir)
    __filelist.sort()
    __newnpydir = "/home/suchoi/KOMAC/analysis/npy"

    i=0
    for __np_file in __filelist:
        if __np_file[len(__np_file)-1] =='y':
            __data = __np.load(__npydir + '/' +__np_file)
            total_np_list.append(__data)
    total_np = __np.array(total_np_list)
    filename="total_data_rev2.npy"
    __np.save("%s/%s"%(__newnpydir,filename),total_np)


### ----------------------------------------------------------------------            
### count num of nan on whole maps
def __HistNpy(totalnp, targetnpy):
    for i in range(0,512):
        for j in range(0,1024):
            if not(__np.isnan(targetnpy[i][j])):
                totalnp[i][j] = totalnp[i][j] + 1       

### ----------------------------------------------------------------------                        
### Draw all each maps
def DrawAllMaps_old():
    i=0
    for data in __datalist: 
        __plt.figure(1,figsize=(8,12),facecolor='white')
        if i==0:
            __plt.figure(1).add_subplot(5,2,i+1)
            i=i+2
        else:
            __plt.figure(1).add_subplot(5,2,i)
            i=i+1
        __plt.imshow(data*10,cmap='viridis',interpolation='none',vmin=0.1)
        __plt.clim(0,200)
        __plt.colorbar()
        __plt.xlabel('column')
        __plt.ylabel('row')
        __plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.1)

### ----------------------------------------------------------------------                        
### Draw all each thresholdhisto
def DrawAllThrsHisto():
    i=0
    
    __datadir = "/home/suchoi/KOMAC/data/exp1/data_exp1"
    __plt.figure(1,figsize=(4,7),facecolor='white')
    for data in __os.listdir(__datadir):
        if data[0] != '.':
            mydir = __datadir + '/' + data + '/thrscan'
            for mydata in __os.listdir(mydir):
                if mydata.endswith("threshold.png"):
                    if i==0:
                        __plt.figure(1).add_subplot(5,2,i+1)
                        i=i+2
                    else:
                        __plt.figure(1).add_subplot(5,2,i)
                        i=i+1
                    
                    mypic = __plt.imread(mydir+'/'+mydata)
                    __plt.axis('off')
                    __plt.imshow(mypic)
                    
        
    __plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0., hspace=0.)
    
### ----------------------------------------------------------------------                        
### Draw all each noisehisto
def DrawAllNoiseHisto():
    i=0
    
    __datadir = "/home/suchoi/KOMAC/data/exp1/data_exp1"
    __plt.figure(1,figsize=(4,7),facecolor='white')
    for data in __os.listdir(__datadir):
        if data[0] != '.':
            mydir = __datadir + '/' + data + '/thrscan'
            for mydata in __os.listdir(mydir):
                if mydata.endswith("noise.png"):
                    if i==0:
                        __plt.figure(1).add_subplot(5,2,i+1)
                        i=i+2
                    else:
                        __plt.figure(1).add_subplot(5,2,i)
                        i=i+1
                    
                    mypic = __plt.imread(mydir+'/'+mydata)
                    __plt.axis('off')
                    __plt.imshow(mypic)
                    
        
    __plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0., hspace=0.)


#-------------revision line------------------------------------------

### ----------------------------------------------------------------------                        
### Hisotgram of nulled pixels
def NullHisto():
    __plt.figure(3,facecolor='white')
    __plt.title('Histogram of NULL pixels')
    __plt.xlabel('dose(krad)')
    __plt.ylabel('# of null pixels')
    __plt.xlim(-5,50)
    __plt.yscale('log')
    # KOMACdir = "/Users/hipex/KOMAC/"
    filename = "dose.txt"
    dosefile = open(filename,'r')
    totaldose = 0
    i = 0
    
    for line in dosefile:
        dose = line.split()
        totaldose = totaldose + float(dose[1])
        __plt.plot(totaldose,__nanNum[i],'ob')
        i=i+1

### ----------------------------------------------------------------------                        
### projection to X of thresholds    
def ThrsProjectionX():
    i=0
    
    for data in __datalist:
        if i==0:
            __plt.figure(8,facecolor='white')
            __plt.title('Threshold Projection to X')
        else:
            __plt.figure(9,figsize=(10,8),facecolor='white')
            __plt.figure(9).add_subplot(4,2,i)
            

        __plt.ylim(80,120)
        __plt.xlabel('column')
        __plt.ylabel('threshold')

        meanthrs = list()
        for j in range(0,1024):
            meanthrs.append(__np.nanmean(data[:,j])*10)
        __plt.plot(range(0,1024),meanthrs)
        i=i+1
        
    
### ----------------------------------------------------------------------
### projection to Y of thresholds    
def ThrsProjectionY():
    i=0
    for data in __datalist:
        if i==0:
            __plt.figure(10,facecolor='white')
            __plt.title('Threshold Projection to Y')

        else:
            __plt.figure(11,figsize=(10,8),facecolor='white')
            __plt.figure(11).add_subplot(4,2,i)
            
        __plt.ylim(80,120)
        __plt.xlabel('row')
        __plt.ylabel('threshold')
        
        meanthrs = list()
        for j in range(0,512):
            meanthrs.append(__np.nanmean(data[j])*10)
        __plt.plot(range(0,512),meanthrs)

        i=i+1
            
### ----------------------------------------------------------------------
### make firedtime.npy
def MakeFiredTime():
    newnpydir = "/home/suchoi/KOMAC/analysis/npy"
    __os.system("rm %s*npy"%newnpydir)
    
    totalnp = __np.zeros((512,1024))
    
    i=0
    for data in __datalist:
        __HistNpy(totalnp, data)
            
    __np.save("%sHitNum.npy"%newnpydir,totalnp)
    
def ShowPLT():
    # __plt.show()
    # __plt.savefig("./temp.png")
    __plt.savefig("./temp.png",dpi=300)

### ----------------------------------------------------------------------
### Thrs projection to X
def SubThrsProj_X():
    origin_thrs = list()
    
    comp_thrs = list()
    i=0
    for data in __datalist:
        temp_thrs = list()
        if i==0:
            for j in range(0,1024):
                origin_thrs.append(__np.nanmean(data[:,j])*10)
        else:
            for j2 in range(0,1024):
                temp_thrs.append(__np.nanmean(data[:,j2])*10-origin_thrs[j2])
            comp_thrs.append(temp_thrs)
        i=i+1
    print(__np.shape(comp_thrs))
    __plt.figure(12,figsize=(10,8),facecolor='white')
    
    for k in range(1,9):
        __plt.figure(12).add_subplot(4,2,k)
        __plt.plot(range(0,1024),comp_thrs[k-1])
        
        __plt.ylim(-5,20)
        __plt.xlabel('column')
        __plt.ylabel('threshold')
        
### ----------------------------------------------------------------------
### Thrs projection to Y
def SubThrsProj_Y():
    origin_thrs = list()
    comp_thrs = list()
    i=0
    for data in __datalist:
        temp_thrs = list()
        if i==0:
            for j in range(0,512):
                origin_thrs.append(__np.nanmean(data[j])*10)
        else:
            for j2 in range(0,512):
                temp_thrs.append(__np.nanmean(data[j2])*10-origin_thrs[j2])
            comp_thrs.append(temp_thrs)
        i=i+1
    print(__np.shape(comp_thrs))
    __plt.figure(13,figsize=(10,8),facecolor='white')
    
    for k in range(1,9):
        __plt.figure(13).add_subplot(4,2,k)
        __plt.plot(range(0,512),comp_thrs[k-1])
        
        __plt.ylim(-5,20)
        __plt.xlabel('row')
        __plt.ylabel('threshold')
        
### ----------------------------------------------------------------------
### Map subtract
def SubMap():
    __plt.figure(14,figsize=(10,8),facecolor='white')
    for i in range(1,9):
        __plt.figure(14).add_subplot(4,2,i)
        resnp = __np.subtract(totalnpy[i],totalnpy[0])
        resnp = resnp*10
        __plt.imshow(resnp,interpolation='none')
        __plt.clim(-30,70)
        __plt.colorbar()
        print("%dth maximum is %f"%(i,__np.nanmax(resnp)))
        print("%dth minimum is %f"%(i,__np.nanmin(resnp)))

### ----------------------------------------------------------------------
### Origin thrs of each pixels
def ThresholdNOM():
    __plt.figure(15,figsize=(10,8),facecolor='white')
    __plt.xlim(-10,210)
    mybin=[]
    for i in range(0,30):
        mybin.append(i*10)
        
    nomnpy = __np.load("./npy/HitNum.npy")
    for i in range(0,10):
        count = []
        for x in range(0,512):
            for y in range(0,1024):
                if nomnpy[x][y] == i :
                    if __np.isnan(totalnpy[0][x][y]):
                        count.append(0)
                    else:
                        count.append(totalnpy[0][x][y]*10)
        mycolor = {0:'black',1:'red', 2:'darkorange', 3:'yellow',4:'greenyellow',5:'green',6:'cyan',7:'deepskyblue',8:'blue', 9:'blueviolet'}
        __plt.hist(count,bins=mybin,histtype='step',label='NOM = %d'%i,color=mycolor[i])
        
    __plt.legend()
    __plt.yscale('symlog')
    __plt.xlabel("Thresholds of each pixel")
    __plt.title("Threshold and NOM(Number of Measurement)")



### ----------------------------------------------------------------------
### Threshold histogram of each pixels
def ThresholdHisto():
    __plt.figure(16,figsize=(10,8),facecolor='white')
    __plt.figure(17,figsize=(10,8),facecolor='white')
    __plt.figure(18,figsize=(10,8),facecolor='white')
    
    __plt.figure(16)
    __plt.xlim(-10,210)
    __plt.figure(17)
    __plt.xlim(-10,210)
    __plt.figure(18)
    __plt.xlim(-10,210)

    mybin=[]
    for i in range(0,100):
        mybin.append(i*3)

    mycolor = {0:(0,0,0),1:(1,0,0,0.9), 2:(1,0,0,0.6), 3:(1,0,0,0.3),4:(0,0,1,1.0),5:(0,0,1,0.8),6:(0,0,1,0.6),7:(0,0,1,0.4),8:(0,0,1,0.2)}

    for i in range(0,9):
        count = []
        for x in range(0,512):
            for y in range(0,1024):
                    
                
                if __np.isnan(totalnpy[i][x][y]):
                    count.append(0)
                else:
                    count.append(totalnpy[i][x][y]*10)
        
        if i==0:
            __plt.figure(16)
            __plt.hist(count,bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
            __plt.figure(17)
            __plt.hist(count,bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
            __plt.figure(18)
            __plt.hist(count,bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
        if i>=1 and i<=3:
            __plt.figure(16)
            __plt.hist(count,bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
            __plt.figure(17)
            __plt.hist(count,bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
        if i>=4 and i<=8:
            __plt.figure(16)
            __plt.hist(count,bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
            __plt.figure(18)
            __plt.hist(count,bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
        
    __plt.figure(16)
    __plt.legend()
    __plt.yscale('symlog')
    __plt.xlabel("Thresholds of each pixel")
    __plt.title("Thresholds Histogram of each Map")
        
    __plt.figure(17)
    __plt.legend()
    __plt.yscale('symlog')
    __plt.xlabel("Thresholds of each pixel")
    __plt.title("Thresholds Histogram of each Map")
    
    __plt.figure(18)
    __plt.legend()
    __plt.yscale('symlog')
    __plt.xlabel("Thresholds of each pixel")
    __plt.title("Thresholds Histogram of each Map")
    
### ----------------------------------------------------------------------
### Subtract threshold Map Histogram
def SubThrsDist():
    mybin=[]
    for i in range(0,200):
        mybin.append(-50+i*1)
    
    mycolor = {0:(0,0,0),1:(1,0,0,0.9), 2:(1,0,0,0.6), 3:(1,0,0,0.3),4:(0,0,1,1.0),5:(0,0,1,0.8),6:(0,0,1,0.6),7:(0,0,1,0.4),8:(0,0,1,0.2)}
    __plt.figure(19,figsize=(10,8),facecolor='white')
    __plt.xlim(-70,70)
    
    for i in range(1,9):
        resnp = __np.subtract(totalnpy[i],totalnpy[0])
        resnp = resnp*10
        __plt.hist(__np.ravel(resnp),bins=mybin,histtype='step',label='%d'%i,color=mycolor[i])
        
    __plt.legend()
    __plt.yscale('symlog')
    __plt.xlabel("Thresholds Gap")
    __plt.title("Thresholds Subtract with at 0krad of Each Pixel")
    
       
### ----------------------------------------------------------------------
### Check Each thrs-dose plot of pixels
def __CheckThrsDose(mythrs):
    IsFirstMax = False
    IsFirstMin = False
    
    nancount = 0
    predata = 0
    IsDecrease = False
    for i in range(0,9):
        if __np.isnan(mythrs[i]):
            nancount = nancount+1
        if i>=1:
            if mythrs[i] < predata:
                IsDecrease = True
            predata=mythrs[i]
                
    if nancount==9:
        return "f"      # bad pixel
    if (__np.isnan(mythrs[0])) and not(nancount==9) :
        return "g"      # alive after irradiation    
    
    if __np.nanmax(mythrs)==mythrs[0]:
        IsFirstMax = True
    if __np.nanmin(mythrs)==mythrs[0]:
        IsFirstMin = True
        
    
        
    if (not IsFirstMax) and (not IsFirstMin) :
        return "a"      # typical curve decrease
    if (not IsFirstMax) and IsFirstMin:
        if IsDecrease:
            return "b"  # typical curve before recover
        else :
            return "c"  # typical curve without decrease
    if IsFirstMax and (not IsFirstMin):
        return "d"      # just decrease
    if IsFirstMax and IsFirstMin:
        return "e"      # all die after irradiation
    
    return "what"
    
### ----------------------------------------------------------------------
### All Pixel Thrs-dose curve type
def AllPixelThresholdDose():
    # __plt.figure(20,figsize=(10,8),facecolor='white')
    # fig = __plt.figure()
    
    KOMACdir = "/Users/hipex/KOMAC/result/exp1/"
    filename = "dose.txt"
    dosefile = open(KOMACdir+filename,'r')
    totaldose = 0
    
    dose = []
    totaldose = 0
    for line in dosefile:
        mydose = line.split()
        totaldose = totaldose + float(mydose[1])
        dose.append(round(totaldose,2))
    
    ### Draw 3D
    # ax = fig.add_subplot(111, projection='3d')
    # pixelnum = 0
    # for x in range(0,512):
    #     for y in range(0,1024):
    #         mythrs = []
    #         for i in range(0,9):
    #             mythrs.append(totalnpy[i][x][y])
    #         __plt.plot(dose,__np.ones(9)*pixelnum,mythrs)
    #         pixelnum = pixelnum + 1
    #         break
    
    
    
    typecount = []
    
    
    for x in range(0,512):
        for y in range(0,1024):                
                mythrs = []
                for j in range(0,9):
                    mythrs.append(totalnpy[j][x][y])
                typecount.append(__CheckThrsDose(mythrs))
    
    __np.save("%s/CurveType.npy"%("/Users/hipex/KOMAC/analysis/npy"),typecount)
    letter_counts = Counter(list(__np.sort(typecount)))
    df = pandas.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar',logy=True, legend=None)

### ----------------------------------------------------------------------
### Check the tjreshold-dose curve type for die pixels
def CheckCurve():
    nomnpy = __np.load("./npy/HitNum.npy")
    Curvenpy = __np.load("./npy/CurveType.npy")
    Curvenpy = Curvenpy.reshape(512,1024)

    
    typecount = __np.zeros((10,7))

    typedict = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6}
    for x in range(0,512):
        for y in range(0,1024):
            x_nom = nomnpy[x][y]
            y_type = typedict[Curvenpy[x][y]]
            typecount[int(x_nom)][int(y_type)] = typecount[int(x_nom)][int(y_type)] + 1
    
    typecount = typecount.astype(int)
    # print(typecount)
    
    __plt.figure(20,figsize=(10,8),facecolor='white')
    for i in range(0,7):
        __plt.plot(typecount.T[:][i], marker='o', label="type %d"%i)
        if i==3 : break
    __plt.legend()
    __plt.xlabel("Number of measurement")
    __plt.title("Number of Measuremenst for each type")
    __plt.yscale('symlog')

    __plt.figure(21,figsize=(10,8),facecolor='white')
    cutmatrix = __np.zeros((4,10))
    for x in range(0,4):
        for y in range(0,10):
            cutmatrix[x][y] = typecount[y][x]
    __plt.imshow(cutmatrix, norm=colors.LogNorm(),extent=[0,9,0,3])
    ax=__plt.gca()
    __plt.colorbar()
    
### ----------------------------------------------------------------------
### Check the thrs before pixels die
def ThrsBeforeDie():
    mybin=[]
    for i in range(0,20):
        mybin.append(i*10)
        
    # __plt.figure(22,figsize=(10,8),facecolor='white')
    # __plt.title("Histogram of Threshold before Null Pixel")
    
    DiePixelThrs=[]
    AllPixelThgrs=[]
    
    for i in range(0,8):
        
        for x in range(0,512):
            for y in range(0,1024):
                if __np.isnan(totalnpy[i+1][x][y]):
                    if __np.isnan(totalnpy[i][x][y]):
                        DiePixelThrs.append(0)
                    else :
                        DiePixelThrs.append(totalnpy[i][x][y]*10)
                else:
                    if __np.isnan(totalnpy[i][x][y]):
                        AllPixelThgrs.append(0)
                    else :
                        AllPixelThgrs.append(totalnpy[i][x][y]*10)
        
        if not i==8:
            __plt.figure(22).add_subplot(4,2,i+1)
            __plt.hist(AllPixelThgrs,histtype='step',label="All pixels",bins=mybin)
            __plt.hist(DiePixelThrs,histtype='step',label="Die pixels",bins=mybin)
            __plt.yscale('symlog')
            # if i==0:
            #     __plt.legend()    
        
        
        
        DiePixelThrs=[]
        AllPixelThgrs=[]
        
    
### ----------------------------------------------------------------------
### Check the high thrs outside 1 sigma
def HighThrs():
    
    
    for i in range(0,9):
        __plt.figure(23,figsize=(10,9),facecolor='white')        
        if i==0:
            __plt.figure(23).add_subplot(5,2,1)
        else :
            __plt.figure(23).add_subplot(5,2,i+2)
        # thrsCut = __np.nanmean(totalnpy[i])+__np.nanstd(totalnpy[i])
        mymean = __np.nanmean(totalnpy[i])
        mystd = __np.nanstd(totalnpy[i])
        out_count = []
        up_count = []
        down_count = []
        in_count = []
        for x in range(0,512):
            out_count_row = 0
            up_count_row = 0
            down_count_row = 0
            in_count_row = 0
            for y in range(0,1024):
                mygap = totalnpy[i][x][y]-mymean
                
                if abs(mygap) >=  mystd:    out_count_row = out_count_row +1
                if mygap >=  mystd:         up_count_row = up_count_row +1
                if mygap < -1 * mystd:      down_count_row = down_count_row + 1
                if abs(mygap) <  mystd:     in_count_row = in_count_row +1
            out_count.append(out_count_row)
            up_count.append(up_count_row)
            down_count.append(down_count_row)
            in_count.append(in_count_row)

    
        sum_out =  0
        sum_up  =  0
        sum_down=  0
        sum_in  =  0
        new_out_count = []
        new_up_count = []
        new_down_count = []
        new_in_count = []
        xbin = []
        for row_bin in range(0,64):
            count_sum = 0
            for j in range(0,8):
                sum_out = sum_out + out_count[row_bin*8+j]
                sum_up = sum_up + up_count[row_bin*8+j]
                sum_down = sum_down + down_count[row_bin*8+j]
                sum_in = sum_in + in_count[row_bin*8+j]
            for j in range(0,8):
                xbin.append(row_bin*8+j)
                new_out_count.append(sum_out/8)
                new_up_count.append(sum_up/8)
                new_down_count.append(sum_down/8)
                new_in_count.append(sum_in/8)
            sum_out = 0
            sum_up  = 0
            sum_down= 0
            sum_in  = 0
        __plt.plot(xbin,new_out_count,label="outside 1 sigma")
        __plt.plot(xbin,new_up_count,label="higher than 1 sigma")
        __plt.plot(xbin,new_down_count,label="lower than 1 sigma")
        __plt.plot(xbin,new_in_count,label="inside 1 sigma")
        __plt.legend(fontsize=5,loc='center left')  
        # __plt.ylim(100,350)
        # __plt.ylim(50,250)
        # __plt.ylim(000,200)
        # __plt.ylim(300,800)
        __plt.ylim(0,800)
    # __plt.figure(23).add_subplot(5,2,2)
    
    # y=__np.zeros(512)
    
    

    # __plt.plot(up_count,label="up")
    # __plt.plot(down_count,label="down")
    
### ----------------------------------------------------------------------
### Draw All Thresholds Histo
def AllTHrsHisto():
    __plt.figure(24,figsize=(10,8),facecolor='white')
    dvmax=20
    # totalnpy=totalnpy*10
    totalnpy[totalnpy==0]=__np.nan
    for i in range(0,9):
        print('Threshold: %.2f +/- %.2f DAC (based on %d pixels)'%(__np.nanmean(totalnpy[i]),__np.nanstd(totalnpy[i]),__np.sum(~__np.isnan(totalnpy[i]))))
        thresholds_draw = totalnpy[i].ravel()
        mylabel = 'Threshold of data%d: $\mu=%.2f,\ \sigma=%.2f$'%(i,__np.nanmean(totalnpy[i]),__np.nanstd(totalnpy[i]))
        mycolor = {0:'black',1:'red', 2:'darkorange', 3:'yellow',4:'greenyellow',5:'green',6:'cyan',7:'deepskyblue',8:'blue', 9:'blueviolet'}
        n, bins, patches = __plt.hist(thresholds_draw,bins=5*dvmax,range=(0,dvmax), histtype='step', label=mylabel, color=mycolor[i])
        __plt.xlim(0,dvmax)
        # __plt.title('Threshold: $\mu=%.2f,\ \sigma=%.2f$'%(__np.nanmean(totalnpy[i]),__np.nanstd(totalnpy[i])))
        __plt.xlabel('Threshold(DAC)')
        __plt.ylabel('Pixels')
        __plt.legend()


### ----------------------------------------------------------------------
### Read NPY
def ReadNPY(inpy):
    __np.set_printoptions(threshold=__sys.maxsize)
    # print(totalnpy[inpy][0][0])
    
    npyfiledir = "./npy/RawHits"
    for file in os.listdir():
        __np.load("%s/"%(npyfiledir))


### ----------------------------------------------------------------------
### Count number of NULL
def CountNull(somenpy):
    count=0
    for i in range(0,512):
        for j in range(0,1024):
            if __np.isnan(somenpy[i][j]) :
                count = count + 1
    return count

### ----------------------------------------------------------------------
### Count number of zero
def CountZero(somenpy):
    count=0
    for i in range(0,512):
        for j in range(0,1024):
            if somenpy[i][j]==0. :
                count = count + 1
    return count


### ----------------------------------------------------------------------
### Compare number of Null(old, new)
def CompareNull():
    totalnpy_old = __np.load("./npy/total_data_old.npy")
    totalnpy_fit = __np.load("./npy/total_data_fit.npy")
     
    __plt.figure(3,facecolor='white')
    __plt.title('Number of NULL pixels')
    __plt.xlabel('dose(krad)')
    __plt.ylabel('# of null pixels')
    __plt.xlim(-5,50)
    __plt.yscale('log')
    filename = "dose.txt"
    dosefile = open(filename,'r')
    
    totaldose=0
    i=0
    doseval=[]
    nullval=[]
    nullval_fit=[]
    nullval_old=[]
    for line in dosefile:
        dose = line.split()
        totaldose = totaldose + float(dose[1])
        doseval.append(totaldose)
        nullval.append(CountNull(totalnpy[i]))
        nullval_fit.append(CountNull(totalnpy_fit[i]))
        nullval_old.append(CountNull(totalnpy_old[i]))
        # nullval.append(CountZero(totalnpy[i]))
        # nullval_old.append(CountZero(totalnpy_old[i]))
        # nullval_fit.append(CountZero(totalnpy_fit[i]))
        i=i+1

    print(nullval_old)
    __plt.plot(doseval,nullval_old,'or',label="Origin")
    __plt.plot(doseval,nullval_fit,'og',label="Fitted")
    # __plt.plot(doseval,nullval,'ob',label="Revision of Origin")
    __plt.legend()

def DrawAllMaps(mynpy):
    __plt.figure(1,figsize=(10,8),facecolor='white')
    for idata in range(0,9): 
        __plt.figure(1).add_subplot(5,2,idata+1)
        __plt.imshow(mynpy[idata]*10,cmap='viridis',interpolation='none',vmin=0.1)
        __plt.clim(0,200)
        __plt.colorbar()
        __plt.xlabel('column')
        __plt.ylabel('row')
        __plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.25)