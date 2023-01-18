#!/bin/bash

# ./sub.py -a -p processed/totalnpy/Apr_threshold_origin_total.npy      -o Thrs_projX_Apr
# ./sub.py -a -p processed/totalnpy/Jun_threshold_origin_total.npy      -o Thrs_projX_Jun
# ./sub.py -a -p processed/totalnpy/Jul_RPI_threshold_origin_total.npy  -o Thrs_projX_Jul_RPI
# ./sub.py -a -p processed/totalnpy/Jul_RAS_threshold_origin_total.npy  -o Thrs_projX_Jul_RAS
# ./sub.py -a -p processed/totalnpy/Sep_threshold_origin_total.npy      -o Thrs_projX_Sep
# ./sub.py -a -p processed/totalnpy/Nov_threshold_origin_total.npy      -o Thrs_projX_Nov

./sub.py -a -p processed/totalnpy/Apr_threshold_revision_total.npy      -o Thrs_projX_Apr_
./sub.py -a -p processed/totalnpy/Jun_threshold_revision_total.npy      -o Thrs_projX_Jun_
./sub.py -a -p processed/totalnpy/Jul_RPI_threshold_revision_total.npy  -o Thrs_projX_Jul_RPI_
./sub.py -a -p processed/totalnpy/Jul_RAS_threshold_revision_total.npy  -o Thrs_projX_Jul_RAS_
./sub.py -a -p processed/totalnpy/Sep_threshold_revision_total.npy      -o Thrs_projX_Sep_
./sub.py -a -p processed/totalnpy/Nov_threshold_revision_total.npy      -o Thrs_projX_Nov_




# ./src/myhitmap.py 
# /home/suchoi/KOMAC/data/selected/KOMAC_2022_11/RPI


#---------------------------------------------------------------------------------------------------
### Extract numpy
# ./sub.py -ms --mode 4 -r /home/suchoi/KOMAC/analysis/datapath/Nov_raw.txt -j /home/suchoi/KOMAC/analysis/datapath/Nov_json.txt -p temp -o Nov
# ./sub.py -ms --mode 2 -r /home/suchoi/KOMAC/analysis/datapath/Nov_raw.txt -j /home/suchoi/KOMAC/analysis/datapath/Nov_json.txt -p temp
# ./sub.py -ms --mode 3 -r /home/suchoi/KOMAC/analysis/datapath/Nov_raw.txt -j /home/suchoi/KOMAC/analysis/datapath/Nov_json.txt -p temp


# #---------------------------------------------------------------------------------------------------
# ./sub.py -a -p processed/totalnpy/Apr_null_origin_total.npy        -o nullprojectionY_Apr.png
# ./sub.py -a -p processed/totalnpy/Jun_null_origin_total.npy        -o nullprojectionY_Jun.png
# ./sub.py -a -p processed/totalnpy/Jul_RPI_null_origin_total.npy    -o nullprojectionY_Jul_RPI.png
# ./sub.py -a -p processed/totalnpy/Jul_RAS_null_origin_total.npy    -o nullprojectionY_Jul_RAS.png
# ./sub.py -a -p processed/totalnpy/Sep_null_origin_total.npy        -o nullprojectionY_Sep.png






# #-------------------------------------------------------------------------------------------------
# ### Calculate mean of threshold
# ./sub.py -c -t1 ./processed/dose/Apr_dose.txt       -t2 ./processed/datainfo/mean_Apr_orign.txt         -o dose_thrs_Apr_origin.png
# ./sub.py -c -t1 ./processed/dose/Apr_dose.txt       -t2 ./processed/datainfo/mean_Apr_revision.txt      -o dose_thrs_Apr_revision.png
# ./sub.py -c -t1 ./processed/dose/Jun_dose.txt       -t2 ./processed/datainfo/mean_Jun_origin.txt        -o dose_thrs_Jun_origin.png
# ./sub.py -c -t1 ./processed/dose/Jun_dose.txt       -t2 ./processed/datainfo/mean_Jun_revision.txt      -o dose_thrs_Jun_revision.png
# ./sub.py -c -t1 ./processed/dose/Jul_RPI_dose.txt   -t2 ./processed/datainfo/mean_Jul_RPI_origin.txt    -o dose_thrs_Jul_RPI_origin.png
# ./sub.py -c -t1 ./processed/dose/Jul_RPI_dose.txt   -t2 ./processed/datainfo/mean_Jul_RPI_revision.txt  -o dose_thrs_Jul_RPI_revision.png
# ./sub.py -c -t1 ./processed/dose/Jul_RAS_dose.txt   -t2 ./processed/datainfo/mean_Jul_RAS_origin.txt    -o dose_thrs_Jul_RAS_origin.png
# ./sub.py -c -t1 ./processed/dose/Jul_RAS_dose.txt   -t2 ./processed/datainfo/mean_Jul_RAS_revision.txt  -o dose_thrs_Jul_RAS_revision.png
# ./sub.py -c -t1 ./processed/dose/Sep_dose.txt       -t2 ./processed/datainfo/mean_Sep_origin.txt        -o dose_thrs_Sep_origin.png
# ./sub.py -c -t1 ./processed/dose/Sep_dose.txt       -t2 ./processed/datainfo/mean_Sep_revision.txt      -o dose_thrs_Sep_revision.png








# #-------------------------------------------------------------------------------------------------
# ### Draw Maps
# ./sub.py -a -p ./totalnpy/Apr_threshold_origin_total.npy        -o Apr_origin_hist.png          -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Apr_threshold_revision_total.npy      -o Apr_revision_hist.png        -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Jun_threshold_origin_total.npy        -o Jun_origin_hist.png          -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Jun_threshold_revision_total.npy      -o Jun_revision_hist.png        -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Jul_RPI_threshold_origin_total.npy    -o Jul_RPI_origin_hist.png      -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Jul_RPI_threshold_revision_total.npy  -o Jul_RPI_revision_hist.png    -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Jul_RAS_threshold_origin_total.npy    -o Jul_RAS_origin_hist.png      -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Jul_RAS_threshold_revision_total.npy  -o Jul_RAS_revision_hist.png    -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Sep_threshold_origin_total.npy        -o Sep_origin_hist.png          -v1 0.5 -v2 0.4
# ./sub.py -a -p ./totalnpy/Sep_threshold_revision_total.npy      -o Sep_revision_hist.png        -v1 0.5 -v2 0.4






# #-------------------------------------------------------------------------------------------------
# ### Merge numpys

# ./sub.py -m -p ./eachdata/Apr/ -t1 rowhits_origin -t2       Apr_rowhits_origin_total.npy
# ./sub.py -m -p ./eachdata/Apr/ -t1 noise_origin -t2         Apr_noise_origin_total.npy
# ./sub.py -m -p ./eachdata/Apr/ -t1 threshold_origin -t2     Apr_threshold_origin_total.npy
# ./sub.py -m -p ./eachdata/Apr/ -t1 rowhits_revision -t2     Apr_rowhits_revision_total.npy
# ./sub.py -m -p ./eachdata/Apr/ -t1 noise_revision -t2       Apr_noise_revision_total.npy
# ./sub.py -m -p ./eachdata/Apr/ -t1 threshold_revision -t2   Apr_threshold_revision_total.npy

# ./sub.py -m -p ./eachdata/Jun/ -t1 rowhits_origin -t2       Jun_rowhits_origin_total.npy
# ./sub.py -m -p ./eachdata/Jun/ -t1 noise_origin -t2         Jun_noise_origin_total.npy
# ./sub.py -m -p ./eachdata/Jun/ -t1 threshold_origin -t2     Jun_threshold_origin_total.npy
# ./sub.py -m -p ./eachdata/Jun/ -t1 rowhits_revision -t2     Jun_rowhits_revision_total.npy
# ./sub.py -m -p ./eachdata/Jun/ -t1 noise_revision -t2       Jun_noise_revision_total.npy
# ./sub.py -m -p ./eachdata/Jun/ -t1 threshold_revision -t2   Jun_threshold_revision_total.npy

# ./sub.py -m -p ./eachdata/Jul/RPI/ -t1 rowhits_origin -t2       Jul_RPI_rowhits_origin_total.npy
# ./sub.py -m -p ./eachdata/Jul/RPI/ -t1 noise_origin -t2         Jul_RPI_noise_origin_total.npy
# ./sub.py -m -p ./eachdata/Jul/RPI/ -t1 threshold_origin -t2     Jul_RPI_threshold_origin_total.npy
# ./sub.py -m -p ./eachdata/Jul/RPI/ -t1 rowhits_revision -t2     Jul_RPI_rowhits_revision_total.npy
# ./sub.py -m -p ./eachdata/Jul/RPI/ -t1 noise_revision -t2       Jul_RPI_noise_revision_total.npy
# ./sub.py -m -p ./eachdata/Jul/RPI/ -t1 threshold_revision -t2   Jul_RPI_threshold_revision_total.npy

# ./sub.py -m -p ./eachdata/Jul/RAS/ -t1 rowhits_origin -t2       Jul_RAS_rowhits_origin_total.npy
# ./sub.py -m -p ./eachdata/Jul/RAS/ -t1 noise_origin -t2         Jul_RAS_noise_origin_total.npy
# ./sub.py -m -p ./eachdata/Jul/RAS/ -t1 threshold_origin -t2     Jul_RAS_threshold_origin_total.npy
# ./sub.py -m -p ./eachdata/Jul/RAS/ -t1 rowhits_revision -t2     Jul_RAS_rowhits_revision_total.npy
# ./sub.py -m -p ./eachdata/Jul/RAS/ -t1 noise_revision -t2       Jul_RAS_noise_revision_total.npy
# ./sub.py -m -p ./eachdata/Jul/RAS/ -t1 threshold_revision -t2   Jul_RAS_threshold_revision_total.npy

# ./sub.py -m -p ./eachdata/Sep/ -t1 rowhits_origin -t2       Sep_rowhits_origin_total.npy
# ./sub.py -m -p ./eachdata/Sep/ -t1 noise_origin -t2         Sep_noise_origin_total.npy
# ./sub.py -m -p ./eachdata/Sep/ -t1 threshold_origin -t2     Sep_threshold_origin_total.npy
# ./sub.py -m -p ./eachdata/Sep/ -t1 rowhits_revision -t2     Sep_rowhits_revision_total.npy
# ./sub.py -m -p ./eachdata/Sep/ -t1 noise_revision -t2       Sep_noise_revision_total.npy
# ./sub.py -m -p ./eachdata/Sep/ -t1 threshold_revision -t2   Sep_threshold_revision_total.npy
# #-------------------------------------------------------------------------------------------------