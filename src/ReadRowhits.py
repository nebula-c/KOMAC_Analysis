#!/usr/bin/env python3

import argparse
import json
import numpy as np
from tqdm import tqdm
from scipy import optimize
from scipy import special
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import copy

def sigmoid(x,threshold,noise,ntrg):
    y=(ntrg / 2) * (1 + special.erf( ((x - threshold) / (np.sqrt(2) *noise))  ) )
    return (y)

def mythrscanana(args):
    outfilename=args.rawdata.split("/")[-1].split(".")[0]
    
    try:
        with open('%s'%(args.params),'r') as f:
            params=json.loads(f.read())
    except IOError:
        print('ERROR: File %s could not be read!'%(args.params))
        raise SystemExit(1)

    try:
        with open('%s'%(args.rawdata),'rb') as f:
            data=f.read()
    except IOError:
        print('ERROR: File %s could not be read!'%(args.rawdata))
        raise SystemExit(1)


    f = open("output.txt", 'w')



    dvmin,dvmax=params['dvmin'],params['dvmax']
    if params['row']==None: params['row']=range(512)
    ntrg = params['ntrg']
    pbar=tqdm(total=len(data), leave=not args.quiet)
    thresholds=np.zeros((512,1024))
    noise=np.zeros((512,1024))
    dead=[]
    bad=[]

    rev_thresholds=np.zeros((512,1024))
    rev_noise=np.zeros((512,1024))

    totalrowhits = []
    rev_totalrowhits = []

    i=0
    for row in params['row']:
        # f.write("\n==================== {}th row ====================\n".format(row))
        rowhits=np.zeros((dvmax-dvmin+1,1024))
        for dv in range(dvmin,dvmax+1):
            # f.write("========= dv : {}========".format(dv))
            for itrg in range(params['ntrg']):
                hits,iev,tev,j=decoder.decode_event(data,i)
                pbar.update(j-i)
                i=j
                # f.write("\n----- {}th trig -----\n".format(itrg))
                for x,y in hits:
                    pixellist = []
                    if y!=row:
                        print('warning: hit from bad row: hit=(%d,%d) row=%d \n'%(x,y,row))
                    else:
                        # f.write("({},{}) ".format(x,y))
                        # f.write("pixel : {},{} -->  ".format(x,y))
                        # pixellist.append("1")
                        rowhits[dv-dvmin,x]+=1
                        # f.writelines(pixellist)
                        # f.write("\n")
                        
        # if row == 5 :
            # break
        ### ------------------------------------------
        ### revision
        if args.revision: 
            rev_rowhits = copy.deepcopy(rowhits)
            for mynum in range(1024):
                if (rev_rowhits[0,mynum] != 0) & (rev_rowhits[0,mynum] != 50):
                    rev_rowhits[0,mynum]=0
        ### ------------------------------------------


        totalrowhits.append(np.swapaxes(rowhits,0,1))
        if args.revision:
            rev_totalrowhits.append(np.swapaxes(rev_rowhits,0,1))


        


        if not args.fit:
            d=np.diff(rowhits,axis=0)
            nhits = np.sum(d,axis=0)
            
            if args.revision: 
                rev_d=np.diff(rev_rowhits,axis=0) # revision
                rev_nhits = np.sum(rev_d,axis=0)  # revision

            if np.any(nhits<ntrg):
                bad.extend([(col,row) for col in np.where(nhits<ntrg)[0]])
            if np.any(nhits==0):
                dead.extend([(col,row) for col in np.where(nhits==0)[0]])
            

            nhits[nhits<ntrg] = np.nan # exclude from calculation
            if args.revision: 
                rev_nhits[rev_nhits<ntrg] = np.nan # exclude from calculation, revision

            d/=nhits
            dv=np.linspace(0.5,rowhits.shape[0]-1.5,rowhits.shape[0]-1)[:,np.newaxis]    
            t=np.sum(d*dv,axis=0)
            n=np.sqrt(np.sum((dv-t)**2*d,axis=0))
            thresholds[row,:]=t
            noise[row,:]=n

            if args.revision:
                rev_d/=rev_nhits
                rev_dv=np.linspace(0.5,rev_rowhits.shape[0]-1.5,rev_rowhits.shape[0]-1)[:,np.newaxis]    
                rev_t=np.sum(rev_d*rev_dv,axis=0)
                rev_n=np.sqrt(np.sum((rev_dv-rev_t)**2*rev_d,axis=0))
                rev_thresholds[row,:]=rev_t
                rev_noise[row,:]=rev_n
            ### ------------------------------------------

        else:
            dvx=np.linspace(0,rowhits.shape[0]-1,rowhits.shape[0])[:,np.newaxis]
            for index in range(rowhits.shape[1]):
                if rowhits[:,index].max()==0:
                    dead.append((index,row))
                    continue        
                p0 = [(dvmax-dvmin)/2,0.5]  # initial guess 
                try:
                    popt,pcov = optimize.curve_fit(lambda x,t,n: sigmoid(x,t,n,params['ntrg']), \
                        dvx[:,0],rowhits[:,index] ,p0,method='lm')
                    thresholds[row,index]=popt[0]
                    noise[row,index]=popt[1]
                except RuntimeError:
                    if args.debug_plots:
                        plt.plot(dvx[:,0],rowhits[:,index],'ro')
                        plt.title('Warning: Bad Fit for a pixel at row %d column %d'%(row,index))
                        plt.xlabel('dV')
                        plt.ylabel('Successful triggers from %d'%(params['ntrg']))
                        plt.savefig('%s/%s-BadPixel_%d_%d.png'%(args.path,outfilename,row,index))
                        plt.clf()
                    bad.append((index,row))
    
    f.close()
    # raise SystemExit(1)
    pbar.close()
    np.save('%s/threshold_origin_%s'%(args.path,outfilename.split("-")[1]),thresholds)
    np.save('%s/noise_origin_%s'%(args.path,outfilename.split("-")[1]),noise)
    
    if args.revision:
        np.save('%s/threshold_revision_%s'%(args.path,outfilename.split("-")[1]),rev_thresholds)
        np.save('%s/noise_revision_%s'%(args.path,outfilename.split("-")[1]),rev_noise)


    if args.scurve:
        np.save('%s/rowhits_origin_%s'%(args.path,outfilename.split("-")[1]),totalrowhits)
        if args.revision:
            np.save('%s/rowhits_revision_%s'%(args.path,outfilename.split("-")[1]),rev_totalrowhits)



    if args.quiet:
        return

    cmap = copy.copy(plt.cm.get_cmap("viridis"))
    cmap.set_under(color='white')
    im = plt.imshow(thresholds, cmap=cmap, vmin=0.1)
    plt.xlabel("Column")
    plt.xticks([0,256,512,768,1023])
    plt.ylabel("Row")
    plt.yticks([0,256,511])
    plt.title(f"{len(bad)} bad pixels (with <{ntrg} hits)")
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = plt.colorbar(im,cax=cax)
    cbar.set_label("Hits")
    plt.savefig('%s/%s-thresholdmap.png'%(args.path,outfilename))
    plt.clf()

    thresholds[thresholds==0]=np.nan
    print('Threshold: %.2f +/- %.2f DAC (based on %d pixels)'%(np.nanmean(thresholds),np.nanstd(thresholds),int(np.sum(~np.isnan(thresholds)))))
    thresholds_draw = thresholds.ravel()
    n, bins, patches = plt.hist(thresholds_draw,bins=5*dvmax,range=(0,dvmax))
    plt.xlim(0,dvmax)
    plt.title('Threshold: $\mu=%.2f,\ \sigma=%.2f$'%(np.nanmean(thresholds),np.nanstd(thresholds)))
    plt.xlabel('Threshold (DAC)')
    plt.ylabel('Pixels')
    plt.savefig('%s/%s-threshold.png'%(args.path,outfilename))
    plt.clf()

    noise[noise==0]=np.nan
    print('Noise: %.2f +/- %.2f DAC (based on %d pixels)'%(np.nanmean(noise),np.nanstd(noise),int(np.sum(~np.isnan(noise)))))
    noise_draw = noise.ravel()
    n, bins, patches = plt.hist(noise_draw,bins=100,range=(0,5))
    plt.xlim(0,5)
    plt.title('Noise: $\mu=%.2f,\ \sigma=%.2f$'%(np.nanmean(noise),np.nanstd(noise)))
    plt.xlabel('Noise (DAC)')
    plt.ylabel('Pixels')
    plt.savefig('%s/%s-noise.png'%(args.path,outfilename))
    plt.clf()

    print(f"Found {len(bad)} bad pixels (with <{ntrg} hits)")
    print(f"  of which {len(dead)} dead (with 0 hits).")
    
    

if __name__=="__main__":
    import decoder
    parser=argparse.ArgumentParser(description='The mighty threshold scanner')
    parser.add_argument('rawdata', metavar='RAWFILE',help='raw data file to be processed')
    parser.add_argument('params', metavar='JSONFILE',help='json file with scan setteing')
    parser.add_argument('--path','-p',help='Output plots path', default='.' )
    parser.add_argument('--debug-plots',action='store_true',help='show debug plots: bad fit pixels, hitmap',default=False)
    parser.add_argument('--fit',  action='store_true',help='Fast (default) or fitted method',default=False)
    parser.add_argument('--output','-o',default='thresholds.npy',help='numpy output (default: thresholds.npy)')
    parser.add_argument('--quiet','-q',action='store_true',help="No plots, no terminal output, just npy file.")
    parser.add_argument('--scurve','-s',action='store_true',help="Save Scurve npy file")
    parser.add_argument('--revision','-r',action='store_true',help="revision version")
    args=parser.parse_args()

    # print(args)

    mythrscanana(args)