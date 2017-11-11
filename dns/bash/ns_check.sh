#!/bin/bash

# usage 1: cat "domain" | bash ns_check.sh
# usage 2: bash ns_check.sh (type one at a time in shell)

#VCN's Nameservers
ns_array=( "ns2.vancouvercommunity.net." "ns1.vcn.bc.ca." "ns2.vcn.bc.ca." "ns3.vcn.bc.ca" "ns4.vcn.bc.ca." "ns1.vancouvercommunity.net." )


while read domain
do
dig=$(dig -t NS +short $domain)
  for line in $dig;
    do
	  if [[ $line == ${ns_array[@]} ]]; then
        echo "match: $line"
      else
        echo "no match: $line"

      fi

   done
done

#echo ${ns_array[@]}

