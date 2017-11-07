#!/bin/bash

# vars

array=( felix.vcn.bc.ca sylvester.vcn.bc.ca fexlix.vcn.bc.ca ns1.vancouvercommunity.net )
#IFS=$'\r\n' GLOBIGNORE='*' command eval  'ns=($(cat nameserver.txt))'


for arg in $@
do
  counter=$((counter+1))
  echo "${array[$counter]}"
  #dig -t NS +short $arg | grep "${array[@]}"

done


