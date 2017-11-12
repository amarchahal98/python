#!/bin/bash

# usage 1: cat "domain" | bash ns_check.sh
# usage 2: bash ns_check.sh (type one at a time in shell)

#VCN's Nameservers
ns_array=(ns1.vancouvercommunity.net. ns2.vancouvercommunity.net. ns1.vcn.bc.ca. ns2.vcn.bc.ca. ns3.vcn.bc.ca ns4.vcn.bc.ca. )

# Will check to see if argument matches any of VCN's Nameservers.
while read domain 
do 
  echo $domain

done
