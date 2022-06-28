#!/usr/bin/bash

: '
GNU bash, version 5.0.3(1)-release (x86_64-pc-linux-gnu)
https://adventofcode.com/2021/day/2
res_1: 1746616
res_2: 1741971043
'

#check if no input file
if [ -z $1 ]; then
  echo "no input file!"
  exit
fi

#read data
arr=()
while IFS= read -r line ; do
  arr+=("$line")
done < $1

#RES1
#SUMIF function
function sumif () {
  array=$1[@]
  crit=$2
  a=("${!array}")

  sum=0
  for i in "${a[@]}" ; do
    if [ "${i:0:1}" = "$crit" ] ; then
      let sum+="${i: -1}"
    fi
  done

  echo $sum
}

res_1=$(( ( $(sumif arr "d") - $(sumif arr "u") ) * $(sumif arr "f") ))

#RES2

h=0
d=0
a=0

for i in "${arr[@]}" ; do
  if [ "${i:0:1}" = "f" ] ; then
    let h+="${i: -1}"
    let d+=$(( a * "${i: -1}" ))
  elif [ "${i:0:1}" = "u" ] ; then
    let a-="${i: -1}"
  elif [ "${i:0:1}" = "d" ] ; then
    let a+="${i: -1}"
  fi
done

res_2=$(( h * d ))

echo "res1: $res_1"
echo "res2: $res_2"
