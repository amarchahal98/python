#!/bin/bash

# VARS 
hostname="vcn.bc.ca"

# SCRIPT

Nameservers()
{
while IFS='' read -r line || [[ -n "$line" ]];
do
    ns1=$line
    dig -t NS $hostname | grep $line
    echo $?
done  < "$1"
}
Nameservers $1

#DNS_Resolver()
#{
#    for var in "$@"
#    do
#        dig -t NS $var | grep $nameserver
#        echo $?
#    done
#}
#
#DNS_Resolver $@
