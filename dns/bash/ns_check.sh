#!/bin/bash

# usage: cat "domain" | bash ns_check.sh

#vars
ns1=felix.vcn.bc.ca
ns2=sylvester.vcn.bc.ca
ns3=fexlix.vcn.bc.ca
ns4=ns1.vancouvercommunity.net

while read domain 
do 

  ns=$(dig -t NS $domain)

  echo $ns  | grep -o $ns1
  var1=$?

  if [[ $var1 == 0 ]]; then
    echo "$domain: match=yes"
    continue
  fi

  echo $ns | grep -o $ns2
  var2=$?
  if [[ $var2 == 0 ]]; then
    echo "$domain: match=yes"
    continue
  fi

  echo $ns | grep -o $ns3
  var3=$?
  if [[ $var3 == 0 ]]; then
    echo "$domain: match=yes"
    continue

  fi

  echo $ns | grep -o $ns4
  var4=$?
  if [[ $var4 == 0 ]]; then
    echo "$domain: match=yes"
    continue
  fi

  echo "$domain: match=no"  

done


