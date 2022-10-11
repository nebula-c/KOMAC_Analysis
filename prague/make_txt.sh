#!/bin/zsh

list=("r16" "r5" "r17" "r19" "r42" "r41" "r38" "qr16" "qr5" "qr17" "qr19" "qr42" "qr41" "qr38")

echo ${list[1]}
echo ${list[2]}

for i in ${list[@]}
do
    touch $i".txt"
done