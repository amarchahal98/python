#!/bin/bash

# vars
nameserver=$@

IFS=$'\r\n' GLOBIGNORE='*' command eval  'ns=($(cat nameserver.txt))'

if [[ $nameserver != ${ns[0]} && $nameserver != ${ns[1]} && $nameserver != ${ns[2]} && $nameserver != ${ns[3]} ]] ; then
  echo "no match"

  else 
    echo "match";

fi
