#!/bin/bash


while read p; do
  counter=$((counter+1))
  eval ns$counter=$p
done < nameserver.txt


for i in {1..5}; 
do 
  count=$i
  echo "${ns${count}}"
done
