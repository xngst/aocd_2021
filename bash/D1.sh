#!/usr/bin/bash

: '
GNU bash, version 5.0.3(1)-release (x86_64-pc-linux-gnu)
https://adventofcode.com/2021/day/1
D1 res1: 1139
D1 res1: 1103
'

if [ -z $1 ]; then
  echo "no input file!"
  exit
fi

arr=()

while IFS= read -r line; do
    arr+=("$line")
  done < $1

#RES1
res_1=0
for i in $(seq 1 "${#arr[@]}"); do
  if (( arr[i] < arr[i+1] )); then
    let "res_1+=1"
  fi
done

#RES2
res_2=0
for i in $(seq 1 "${#arr[@]}"); do

  sub_array_1="${arr[@]:i:3}"
  sub_tot_1=0

  for j in ${sub_array_1[@]}; do
    let sub_tot_1+=$j
  done

  sub_array_2="${arr[@]:$(($i+1)):3}"
  sub_tot_2=0

  for j in ${sub_array_2[@]}; do
    let sub_tot_2+=$j
  done

  if ((sub_tot_1 < sub_tot_2)); then
    let "res_2+=1"
  fi
done

#***
echo "D1 res1: $res_1"
echo "D1 res1: $res_2"
