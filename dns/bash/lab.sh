#!/bin/bash

# usage 1: cat "domain" | bash ns_check.sh
# usage 2: bash ns_check.sh (type one at a time in shell)

#VCN's Nameservers
ns1=felix.vcn.bc.ca
ns2=sylvester.vcn.bc.ca
ns3=fexlix.vcn.bc.ca
ns4=ns1.vancouvercommunity.net


# Will check to see if argument matches any of VCN's Nameservers.
while read domain 
do 
  nslist=$(dig -t NS +short $domain)

  if [[ $nslist != *$ns1* && $nslist != *$ns2* && $nslist != *$ns3* && $nslist != *$ns4* ]]; then
    echo "no match: $domain"
    
  fi
  
done


